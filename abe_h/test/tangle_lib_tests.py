from nose.tools import *
from abe_h import tangle_lib

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_buffer_new():
    V = tangle_lib.output_buffer_new()
    eq_('StringO', type(V).__name__)

def test_subdict_build():
    RD = dict( first = 1, second = 2)
    VT = [ ['first','one'], ['second','two'] ]
    OK = dict( one = 1, two = 2)
    eq_(OK, tangle_lib.subdict_build(RD,VT))

def test_arrange():
    SD = dict( one = 1, two = 2)
    TP = u'**{one}** ain\'t _{two}_'
    OK = u'**1** ain\'t _2_'
    eq_(OK, tangle_lib.arrange(TP,SD))
