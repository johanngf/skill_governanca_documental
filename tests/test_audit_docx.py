"""Testes do auditor parcial. Execute `python -m unittest discover -s tests -v`."""
import sys
import tempfile
from pathlib import Path
import unittest
import zipfile
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
SK=ROOT/'skills'/'governanca-documental-institucional'
sys.path.insert(0,str(SK/'scripts'))
from audit_docx import audit, W

CANON=SK/'references'/'normativas'/'Diretriz_Padronizacao_Documental_Institucional_v3.4.docx'

class AuditTest(unittest.TestCase):
    def test_canonical_has_no_order_violation(self):
        result=audit(CANON)
        self.assertFalse([x for x in result['errors'] if 'w:pPr' in x],result['errors'])

    def test_malformed_bookmark_before_ppr_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            fixture=Path(tmp)/'bad.docx'
            with zipfile.ZipFile(CANON,'r') as inp,zipfile.ZipFile(fixture,'w') as out:
                for record in inp.infolist():
                    data=inp.read(record.filename)
                    if record.filename=='word/document.xml':
                        root=ET.fromstring(data)
                        candidate=None
                        for p in root.iter(W+'p'):
                            if p.find(W+'pPr') is not None:
                                candidate=p;break
                        self.assertIsNotNone(candidate)
                        element=ET.Element(W+'bookmarkStart',{W+'id':'999888',W+'name':'test_bad_order'})
                        candidate.insert(0,element)
                        data=ET.tostring(root,encoding='utf-8',xml_declaration=True)
                    out.writestr(record,data)
            result=audit(fixture)
            self.assertFalse(result['ok'])
            self.assertTrue(any('w:pPr' in x for x in result['errors']),result['errors'])

if __name__=='__main__':unittest.main()
