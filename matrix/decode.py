import numpy as np
import textwrap
from string import ascii_uppercase
import binascii
import os


DATA_FILE = os.path.dirname(__file__) + '/data/decode_matrix.txt'


def _convert(i):
    return ord(i) - ord(ascii_uppercase[0])
    
    
def run(text):
    decode_matrix = lib.get_matix(DATA_FILE)
    result = ""
    for word in text.split(' '):
        if word:
            for char in textwrap.wrap(word, 16):
                decoded_ords = np.array([_convert(i) for i in char])
                result_matrix = np.array(decoded_ords * decode_matrix)
                binary_rep = ''.join(str(int(i)) for i in result_matrix[0])
                n = int('0b' + binary_rep, 2)
                result += binascii.unhexlify('%x' % n).decode()
            result += ' '
    return result