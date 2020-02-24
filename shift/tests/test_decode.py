from unittest import TestCase
from .. import decode

class TestDecode(TestCase):
    def test_decode_basic(self):
        self.assertEqual(decode.run("Khoor Zruog"), "Hello World") 
    
    def test_decode_edge(self):
        self.assertEqual(decode.run('ccc'), 'zzz')
        self.assertEqual(decode.run('bbb'), 'yyy')
        self.assertEqual(decode.run('aaa'), 'xxx')

        