from nose.tools import *
from abe_h import abe_h

JsonTestStr1 = '''{
                  "id": "33540dd9-093b-4428-b9fb-f2233262a0bf",
                  "p_i": "1146dc4e-533e-4e53-95c6-bb2775407fe6",
                  "b_a": "Lawrence Snyder",
                  "b_n": "mi sit",
                  "isbn": "968163323-7",
                  "ps": 993,
                  "ls": 232,
                  "p_s": 141,
                  "p_n": "Alan Black",
                  "p_e": "ablack9@woothemes.com",
                  "p_j": "VP Product Management"
                }'''

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"

def test_get_tangler():
    Out = abe_h.get_tangler('sharedbooks_json')
    eq_('module', type(Out).__name__)
    eq_('abe_formats.sharedbooks_json', Out.__name__)

def test_json_tangler():
    Out = abe_h.tangle(JsonTestStr1, 'sharedbooks_json')
