from abe_h import tangle_lib
import json

template = u'''\
{author} *{title}*, {likes} likes

```json
{code}
```
'''

################################################################## API FUNCTIONS
################################################################################

def get_template():
    return template


def get_fields(RawData):
    data = read_data(RawData)
    return element_to_dict(data)

############################################################# INTERNAL FUNCTIONS
################################################################################
def read_data(Input):
    Data = json.loads(Input)
    return Data

def element_to_dict(element):
    value_table = [ [u'b_a', 'author']
                   ,[u'b_n', 'title']
                   ,[u'ls', 'likes'] ]

    return tangle_lib.fielddict_build(element, value_table)
