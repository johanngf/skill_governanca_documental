#!/usr/bin/env python3
"""Auditoria OOXML parcial: títulos, bookmark/pPr, destinos de hyperlinks e sumário.

Não substitui validação de schema completa, renderização, leitura semântica ou teste Word Web.
"""
import argparse, json, re, sys, zipfile
from pathlib import Path
import xml.etree.ElementTree as ET

W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'


def get_style_outline(styles_xml):
    root=ET.fromstring(styles_xml)
    styles={}
    for s in root.findall(W+'style'):
        sid=s.get(W+'styleId')
        if not sid: continue
        ppr=s.find(W+'pPr')
        outline=ppr.find(W+'outlineLvl') if ppr is not None else None
        based=s.find(W+'basedOn')
        styles[sid]={'outline':int(outline.get(W+'val')) if outline is not None and outline.get(W+'val') is not None else None,
                     'based':based.get(W+'val') if based is not None else None}
    def level(sid,visited=None):
        visited=visited or set()
        if sid in visited or sid not in styles: return None
        info=styles[sid]
        if info['outline'] is not None:return info['outline']
        if info['based'] is not None:return level(info['based'],visited|{sid})
        return None
    return level


def audit(path):
    errors=[]; warnings=[]; heading=[]; name_to_ids={}; start_ids=[]; end_ids=[]; anchors=[]; fields=[]
    with zipfile.ZipFile(path) as z:
        root=ET.fromstring(z.read('word/document.xml'))
        style_level=get_style_outline(z.read('word/styles.xml')) if 'word/styles.xml' in z.namelist() else (lambda s: None)
    for p in root.iter(W+'p'):
        children=list(p)
        positions=[i for i,ch in enumerate(children) if ch.tag==W+'pPr']
        if positions and positions != [0]:
            errors.append('w:pPr não é o primeiro filho de w:p no parágrafo: '+''.join((x.text or '') for x in p.iter(W+'t'))[:65])
        if len(positions)>1:errors.append('Mais de um w:pPr no mesmo parágrafo')
        pp=p.find(W+'pPr')
        ps=pp.find(W+'pStyle') if pp is not None else None
        st=ps.get(W+'val') if ps is not None else None
        ol=pp.find(W+'outlineLvl') if pp is not None else None
        lev=int(ol.get(W+'val')) if ol is not None and ol.get(W+'val') else (style_level(st) if st else None)
        content=''.join(x.text or '' for x in p.iter(W+'t')).strip()
        if lev is not None and lev <= 8 and content: heading.append({'text':content[:160], 'style':st, 'outlineLvl':lev})
        elif st and re.match(r'^Heading[1-9]$',st,re.I):
            warnings.append('Título visual/nominativo sem outlineLvl resolvido: '+content[:100])
    for b in root.iter(W+'bookmarkStart'):
        nm=b.get(W+'name');bid=b.get(W+'id')
        if bid is not None: start_ids.append(bid)
        if nm: name_to_ids.setdefault(nm,[]).append(bid)
    for b in root.iter(W+'bookmarkEnd'):
        bid=b.get(W+'id')
        if bid is not None:end_ids.append(bid)
    for h in root.iter(W+'hyperlink'):
        if h.get(W+'anchor'):anchors.append(h.get(W+'anchor'))
    for el in root.iter():
        if el.tag == W+'instrText' and el.text:
            fields.append(el.text.strip())
    for nm,ids in name_to_ids.items():
        if len(ids)>1: errors.append('Bookmark duplicado: '+nm)
    missing_starts=set(end_ids)-set(start_ids)
    missing_ends=set(start_ids)-set(end_ids)
    if missing_starts:errors.append('bookmarkEnd sem start: '+', '.join(sorted(missing_starts)))
    if missing_ends:errors.append('bookmarkStart sem end: '+', '.join(sorted(missing_ends)))
    for anchor in sorted(set(anchors)):
        if anchor not in name_to_ids:errors.append('Hyperlink interno sem bookmark: '+anchor)
    for field in fields:
        m=re.search(r'\bPAGEREF\s+(\S+)',field,re.I)
        if m and m.group(1) not in name_to_ids:
            errors.append('PAGEREF sem bookmark: '+m.group(1))
    if not heading:warnings.append('Nenhum título com nível estrutural reconhecido; verificar se o documento requer títulos')
    return {'file':str(path),'ok':not errors,'errors':errors,'warnings':warnings,'heading_count':len(heading),
            'headings':heading,'bookmark_count':len(start_ids),'internal_hyperlink_count':len(anchors),
            'toc_field_detected':any(re.search(r'\bTOC\b',f,re.I) for f in fields),
            'pageref_field_count':sum(bool(re.search(r'\bPAGEREF\b',f,re.I)) for f in fields),
            'scope':'Auditoria OOXML parcial; requer gate semântico, renderização e teste no ambiente consumidor quando aplicável.'}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('docx',type=Path)
    ap.add_argument('--json',action='store_true')
    args=ap.parse_args()
    try:
        result=audit(args.docx)
    except (OSError,KeyError,ET.ParseError,zipfile.BadZipFile) as exc:
        print('ERRO de leitura:',exc,file=sys.stderr);return 2
    if args.json:print(json.dumps(result,ensure_ascii=False,indent=2))
    else:
        print('OK' if result['ok'] else 'REPROVADO','—',args.docx)
        print('Títulos:',result['heading_count'],'bookmarks:',result['bookmark_count'],'TOC:',result['toc_field_detected'])
        for x in result['errors']:print('ERRO:',x)
        for x in result['warnings']:print('AVISO:',x)
    return 0 if result['ok'] else 1

if __name__=='__main__':
    sys.exit(main())
