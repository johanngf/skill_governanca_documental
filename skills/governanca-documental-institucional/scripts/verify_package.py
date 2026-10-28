#!/usr/bin/env python3
"""Verifica inventário, hashes, metadados e transcrições do pacote de Skill."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
NAME=ROOT.name

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--strict-dir-name',action='store_true',
                        help='Exige que o diretório físico tenha o mesmo nome do frontmatter, obrigatório para validar o pacote distribuído.')
    args=parser.parse_args()
    errors=[]
    warnings=[]
    declared_name=None
    declared_version=None
    skill=ROOT/'SKILL.md'
    if not skill.is_file():errors.append('SKILL.md ausente')
    else:
        t=skill.read_text(encoding='utf-8')
        meta=re.match(r'\A---\s*\n(.*?)\n---\s*\n',t,re.S)
        if not meta:errors.append('SKILL.md sem frontmatter YAML')
        else:
            m=meta.group(1)
            n=re.search(r'^name:\s*(.+)$',m,re.M)
            d=re.search(r'^description:\s*(.+)$',m,re.M)
            v=re.search(r'^\s+version:\s*[\"\']?([^\"\'\s]+)',m,re.M)
            if v: declared_version=v.group(1)
            else:errors.append('version obrigatória em metadata no frontmatter')
            if n:
                declared_name=n.group(1).strip('"\' ')
                if len(declared_name)>64 or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',declared_name):
                    errors.append('name inválido no frontmatter')
                if declared_name!=NAME:
                    msg=f'diretório de instalação {NAME!r} difere do name canônico {declared_name!r}'
                    if args.strict_dir_name:errors.append(msg)
                    else:warnings.append(msg+'; validação do conteúdo continua')
            else:errors.append('name obrigatório no frontmatter')
            if not d or not d.group(1).strip():errors.append('description obrigatório')
            elif len(d.group(1))>1024:errors.append('description excede 1024 caracteres')
    manifest=ROOT/'manifest.json'
    if not manifest.is_file():
        errors.append('manifest.json ausente')
    else:
        meta=json.loads(manifest.read_text(encoding='utf-8'))
        if declared_name and meta.get('skill_name')!=declared_name:errors.append('Nome canônico do frontmatter diferente do manifesto')
        version=meta.get('skill_version')
        release_status=meta.get('release_status')
        if declared_version and declared_version!=version:
            errors.append('Versão do frontmatter diferente da versão do manifesto')
        if not isinstance(version,str) or not re.fullmatch(r'\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?',version):
            errors.append('Versão semântica inválida no manifesto')
        else:
            expected_status='candidate' if '-' in version else 'stable'
            if release_status!=expected_status:
                errors.append(f'Versão {version} exige release_status {expected_status!r}, recebido {release_status!r}')
        entries=meta.get('sources',[])
        if len(entries)!=4:errors.append('Manifesto deve ter 4 fontes')
        paths=set()
        for e in entries:
            for key in ['canonical','derived']:
                r=e.get(key,{})
                rel=r.get('path')
                if not rel or rel in paths:
                    errors.append('Caminho ausente ou repetido: '+str(rel));continue
                paths.add(rel)
                p=ROOT/rel
                if not p.is_file():errors.append('Arquivo ausente: '+rel)
                elif sha(p)!=r.get('sha256'):errors.append('SHA256 divergente: '+rel)
        intended={p.relative_to(ROOT).as_posix() for folder in ['references/normativas','references/consulta'] for p in (ROOT/folder).iterdir() if p.is_file()}
        if paths!=intended:errors.append('Manifesto não coincide com arquivos de fontes presentes')
    c=subprocess.run([sys.executable,str(ROOT/'scripts'/'sync_sources.py'),'--check'],capture_output=True,text=True)
    if c.returncode:errors.append('Transcrições divergentes: '+c.stderr.strip())
    # Opcionalmente manifesto de repositório deve ser idêntico ao empacotado.
    repofile=ROOT.parent.parent/'manifest.json'
    if repofile.exists() and manifest.exists() and repofile.read_bytes()!=manifest.read_bytes():
        errors.append('Manifesto do repositório diferente do da Skill')
    for warning in warnings:print('AVISO:',warning)
    for error in errors:print('ERRO:',error)
    if errors:return 1
    print('OK: SKILL.md, 4 fontes canônicas, espelhos derivados, hashes e manifesto')
    return 0

if __name__=='__main__':sys.exit(main())
