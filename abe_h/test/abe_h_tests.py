from nose.tools import *
from abe_h import abe_h

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"

def test_get_tangler():
    Out = abe_h.get_tangler('b64_json')
    eq_('module', type(Out).__name__)
    eq_('abe_formats.b64_json', Out.__name__)
