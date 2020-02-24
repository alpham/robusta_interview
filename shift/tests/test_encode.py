from unittest import TestCase
from .. import encode

class TestEncode(TestCase):
    def test_encode_basic(self):
        self.assertEqual(encode.run("Hello World"), "Khoor Zruog")
    
    def test_encode_edge(self):
        self.assertEqual(encode.run("zzz"), 'ccc')
        self.assertEqual(encode.run("yyy"), 'bbb')
        self.assertEqual(encode.run("xxx"), 'aaa')
        