"""Verifica identidade canônica na distribuição e portabilidade no diretório instalado."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

REPO=Path(__file__).resolve().parents[1]
SOURCE=REPO/'skills'/'governanca-documental-institucional'


def verify(path,*args):
    return subprocess.run([sys.executable,str(path/'scripts'/'verify_package.py'),*args],
                          text=True,capture_output=True)


class PackageTest(unittest.TestCase):
    def test_packaged_skill_name_must_match_directory(self):
        result=verify(SOURCE,'--strict-dir-name')
        self.assertEqual(0,result.returncode,result.stdout+result.stderr)

    def test_runtime_renamed_directory_warns_but_verifies_contents(self):
        with tempfile.TemporaryDirectory() as temp:
            location=Path(temp)/'runtime-renamed-skill-123'
            shutil.copytree(SOURCE,location)
            result=verify(location)
            self.assertEqual(0,result.returncode,result.stdout+result.stderr)
            self.assertIn('AVISO: diretório de instalação',result.stdout)
            self.assertIn('OK: SKILL.md',result.stdout)

    def test_runtime_renamed_directory_fails_in_strict_distribution_mode(self):
        with tempfile.TemporaryDirectory() as temp:
            location=Path(temp)/'runtime-renamed-skill-123'
            shutil.copytree(SOURCE,location)
            result=verify(location,'--strict-dir-name')
            self.assertNotEqual(0,result.returncode)
            self.assertIn('ERRO: diretório de instalação',result.stdout)

    def test_stable_release_requires_stable_status(self):
        with tempfile.TemporaryDirectory() as temp:
            location=Path(temp)/'governanca-documental-institucional'
            shutil.copytree(SOURCE,location)
            manifest=location/'manifest.json'
            data=json.loads(manifest.read_text(encoding='utf-8'))
            data['release_status']='candidate'
            manifest.write_text(json.dumps(data),encoding='utf-8')
            result=verify(location,'--strict-dir-name')
            self.assertNotEqual(0,result.returncode)
            self.assertIn('exige release_status',result.stdout)

    def test_frontmatter_version_must_match_manifest(self):
        with tempfile.TemporaryDirectory() as temp:
            location=Path(temp)/'governanca-documental-institucional'
            shutil.copytree(SOURCE,location)
            skill=location/'SKILL.md'
            skill.write_text(skill.read_text(encoding='utf-8').replace('version: "1.0.0"','version: "1.0.1"'),encoding='utf-8')
            result=verify(location,'--strict-dir-name')
            self.assertNotEqual(0,result.returncode)
            self.assertIn('Versão do frontmatter diferente',result.stdout)

    def test_manifest_identity_must_match_frontmatter_even_in_runtime_mode(self):
        with tempfile.TemporaryDirectory() as temp:
            location=Path(temp)/'runtime-renamed-skill-123'
            shutil.copytree(SOURCE,location)
            manifest=location/'manifest.json'
            data=json.loads(manifest.read_text(encoding='utf-8'))
            data['skill_name']='outro-nome'
            manifest.write_text(json.dumps(data),encoding='utf-8')
            result=verify(location)
            self.assertNotEqual(0,result.returncode)
            self.assertIn('Nome canônico do frontmatter diferente do manifesto',result.stdout)


if __name__=='__main__':unittest.main()
