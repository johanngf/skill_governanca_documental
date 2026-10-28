#!/usr/bin/env python3
"""Gera pacotes ZIP reproduzíveis do repositório e da Skill (sem arquivos temporários)."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import zipfile

REPO=Path(__file__).resolve().parents[1]
SKILL=REPO/'skills'/'governanca-documental-institucional'
VERSION=json.loads((REPO/'manifest.json').read_text(encoding='utf-8'))['skill_version']
OUT=REPO/'dist'
EXCLUDES={'__pycache__','.git','dist','.DS_Store'}

def files_in(root):
    return sorted((p for p in root.rglob('*') if p.is_file() and not any(x in EXCLUDES for x in p.relative_to(root).parts) and p.suffix!='.pyc'),key=lambda p:p.as_posix())

def zip_tree(src,dest,prefix):
    with zipfile.ZipFile(dest,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for f in files_in(src):
            arc=Path(prefix)/f.relative_to(src)
            entry=zipfile.ZipInfo(arc.as_posix(),date_time=(2026,10,26,0,0,0))
            entry.compress_type=zipfile.ZIP_DEFLATED
            entry.external_attr=(0o100644<<16)
            z.writestr(entry,f.read_bytes(),compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
    return hashlib.sha256(dest.read_bytes()).hexdigest()

def main():
    audit=subprocess.run([sys.executable,str(SKILL/'scripts'/'verify_package.py'),'--strict-dir-name'],check=False)
    tests=subprocess.run([sys.executable,'-m','unittest','discover','-s',str(REPO/'tests')],check=False)
    if audit.returncode or tests.returncode:return 1
    OUT.mkdir(exist_ok=True)
    for src,name,prefix in [(REPO,f'governanca-documental-repositorio-v{VERSION}.zip','governanca-documental'),
                            (SKILL,f'governanca-documental-institucional-v{VERSION}.zip','governanca-documental-institucional')]:
        dest=OUT/name
        h=zip_tree(src,dest,prefix)
        print(f'{name} | {dest.stat().st_size} bytes | SHA-256 {h}')
    return 0

if __name__=='__main__':sys.exit(main())
