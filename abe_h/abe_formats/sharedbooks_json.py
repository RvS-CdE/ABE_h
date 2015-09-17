from abe_h import tangle_lib
import json

template = u'''\
**{title}**,  *{author}* (isbn:{isbn}), {pagecount} pages

- Record ID : {recguid}
- Shared by {user} ({usertitle})
  - *{usermail}*
  - {userfriends} friends
- **{likes}** likes

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

#def get_translated_data(Input):
#    Data = json.loads(Input)
#    if type(Data) is 'list':
#        return Data
#    else:
#        return [Data]
#
#def get_refined_element(rawdata):
#    return element_to_dict(rawdata)
#
#def get_codeblock(raw_code):
#    if type(raw_code) is str:
#        code_template.format({code = raw_code})
#    if type(raw_code) is list:


############################################################# INTERNAL FUNCTIONS
################################################################################
def read_data(Input):
    Data = json.loads(Input)
    return Data

def element_to_dict(element):
    value_table = [ [u'b_n', 'title']
                   ,[u'b_a', 'author']
                   ,[u'isbn', 'isbn']
                   ,[u'ps', 'pagecount']
                   ,[u'id', 'recguid']
                   ,[u'p_n', 'user']
                   ,[u'p_j', 'usertitle']
                   ,[u'p_e', 'usermail']
                   ,[u'p_s', 'userfriends']
                   ,[u'ls', 'likes'] ]

    return tangle_lib.fielddict_build(element, value_table)

