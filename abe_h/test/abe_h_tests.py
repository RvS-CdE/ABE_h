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

JsonTestFormat = 'sharedbooks_json'

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"

def test_simplejson():
    Out = abe_h.unite('tst2_json', '''{"b_a": "Lawrence Snyder","b_n": "mi sit","ls": 232 }''')
    Expected = u'''\
Lawrence Snyder *mi sit*, 232 likes

```json
{"b_a": "Lawrence Snyder","b_n": "mi sit","ls": 232 }
```
'''
    eq_(Expected,Out)

def test_simplearbitrary():
    Out = abe_h.unite('tst2_json'
                     ,'qwe!@#)98QweNOT_EVEN_CODE2019874)(!@!('
                     ,'{"author": "Lawrence Snyder","title": "mi sit","likes": 232 }')
    Expected= u'''\
Lawrence Snyder *mi sit*, 232 likes

```json
qwe!@#)98QweNOT_EVEN_CODE2019874)(!@!(
```
'''
    eq_(Expected,Out)

def test_simplearbitrary_reverse_text():
    TextFull= u'''\
Lawrence Snyder *mi sit*, 232 likes

```json
qwe!@#)98QweNOT_EVEN_CODE2019874)(!@!(
```
'''
    TextClean = u'''Lawrence Snyder *mi sit*, 232 likes\n'''
    eq_(TextClean,abe_h.text(TextFull))

def test_simplearbitrary_reverse_code():
    TextFull= u'''\
Lawrence Snyder *mi sit*, 232 likes

```json
qwe!@#)98QweNOT_EVEN_CODE2019874)(!@!(
```
'''
    CodeClean = u'qwe!@#)98QweNOT_EVEN_CODE2019874)(!@!('
    eq_(CodeClean,abe_h.code(TextFull))
