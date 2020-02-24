import os
import numpy as np
from .lib import get_matix
from string import ascii_uppercase

DATA_FILE = os.path.dirname(__file__) + '/data/encode_matrix.txt'

def _convert(i):
    # make sure that the number is an ASCII letter.
    return chr((int(i) % (26*2)) + ord(ascii_uppercase[0]))
    

def run(text):
    encode_matrix = get_matix(DATA_FILE)
    result = ""
    for c in text:
        if c == ' ':
            result += ' '
            continue
        binary_rep = np.array([int(i) for i in f"{ord(c):016b}"])
        result_matrix = np.array(binary_rep* encode_matrix)
        result += ''.join(_convert(i) for i in result_matrix[0])
    return result

