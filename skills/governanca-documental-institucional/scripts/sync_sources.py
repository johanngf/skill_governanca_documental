#!/usr/bin/env python3
"""Transcrição determinística (não normativa) de DOCX canônico para consulta por agentes.

Somente biblioteca padrão. Preserva sequências de parágrafos/tabelas e textos de células;
não pretende transcrever sem perda todos os elementos visuais e diagramas.
"""
import argparse
from pathlib import Path
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'references' / 'normativas'
OUT = ROOT / 'references' / 'consulta'


def _text(node):
    parts = []
    for el in node.iter():
        if el.tag in {W+'t', W+'delText'}:
            parts.append(el.text or '')
        elif el.tag == W+'tab':
            parts.append('\t')
        elif el.tag in {W+'br', W+'cr'}:
            parts.append('\n')
    return ''.join(parts).strip()


def _paragraph(el):
    ppr=el.find(W+'pPr')
    style = None
    if ppr is not None:
        ps=ppr.find(W+'pStyle')
        if ps is not None:
            style=ps.get(W+'val','')
    content=_text(el)
    if not content:
        return ''
    if style and re.match(r'^Heading[1-6]$',style,re.I):
        level=int(re.search('[1-6]$',style).group())
        return '#'*(min(level+1,6))+' '+content.replace('\n',' ')
    if style and style.lower().startswith('list'):
        return '- '+content.replace('\n',' ')
    return content.replace('\n','  \n')


def _table(el):
    rows=[]
    for tr in el.findall(W+'tr'):
        cells=[]
        for tc in tr.findall(W+'tc'):
            content=[]
            for part in tc:
                if part.tag==W+'p':
                    v=_text(part)
                    if v: content.append(v)
                elif part.tag==W+'tbl':
                    for row in part.findall(W+'tr'):
                        vals=[_text(cell) for cell in row.findall(W+'tc')]
                        content.append(' / '.join(vals))
            cells.append(' / '.join(content).replace('|','\\|').replace('\n',' / '))
        if any(cells): rows.append(cells)
    if not rows: return ''
    width=max(map(len,rows))
    rows=[r+['']*(width-len(r)) for r in rows]
    ret=['| '+' | '.join(rows[0])+' |','| '+' | '.join(['---']*width)+' |']
    ret.extend('| '+' | '.join(r)+' |' for r in rows[1:])
    return '\n'.join(ret)


def convert(path):
    with zipfile.ZipFile(path) as z:
        xml=z.read('word/document.xml')
    body=ET.fromstring(xml).find(W+'body')
    chunks=[]
    for el in body:
        if el.tag==W+'p':
            content=_paragraph(el)
        elif el.tag==W+'tbl':
            content=_table(el)
        else:
            continue
        if content: chunks.append(content)
    stem=path.stem
    lead=(f'<!-- CÓPIA TEXTUAL DERIVADA AUTOMATICAMENTE de {path.name}. '
          'Sem autoridade normativa independente. Elementos visuais/diagramação devem ser consultados no DOCX canônico. '
          'Não editar manualmente; executar scripts/sync_sources.py --write. -->\n\n'
          f'# Transcrição de consulta — {stem}\n\n')
    return lead+'\n\n'.join(chunks)+'\n'


def main():
    ap=argparse.ArgumentParser()
    group=ap.add_mutually_exclusive_group(required=True)
    group.add_argument('--check',action='store_true')
    group.add_argument('--write',action='store_true')
    args=ap.parse_args()
    OUT.mkdir(parents=True,exist_ok=True)
    failures=[]
    docs=sorted(DOCS.glob('*.docx'))
    if len(docs)!=4:
        failures.append(f'Esperados 4 DOCX canônicos; encontrados {len(docs)}')
    for source in docs:
        p=OUT/(source.stem+'.md')
        result=convert(source)
        if args.write:
            p.write_text(result,encoding='utf-8')
            print('Gerado:',p.relative_to(ROOT))
        elif not p.exists() or p.read_text(encoding='utf-8') != result:
            failures.append(f'Transcrição ausente/divergente: {p.name}')
    expected={p.stem+'.md' for p in docs}
    actual={p.name for p in OUT.glob('*.md')}
    if actual!=expected:
        failures.append(f'Inventário de transcrições difere: extra={actual-expected}, ausente={expected-actual}')
    if failures:
        print('\n'.join(f'ERRO: {x}' for x in failures),file=sys.stderr)
        return 1
    print('OK — 4 referências e transcrições coerentes')
    return 0

if __name__=='__main__':
    sys.exit(main())
