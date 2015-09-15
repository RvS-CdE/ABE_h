from abe_h import tangle_lib
import json

template = u'''\
**$title**,  *$author* (isbn:$isbn), $pagecount pages 
 - Record ID : $recguid
 - Shared by $user ($usertitle)
   - *$usermail*
   - $userfriends friends
 - **$likes** likes\
 '''

################################################################## API FUNCTIONS
################################################################################

def get_template():
    return template

def get_translated_data(Input):
    Data = json.loads(Input)
    if (type(Data) is 'list':
        return Data
    else:
        return [Data]

def get_refined_element(rawdata):
    return sub_dict = element_to_dict(rawdata)

############################################################# INTERNAL FUNCTIONS
################################################################################

def element_to_dict(element):
    value_table = [ [u'b_n', 'title']
                   ,[u'b_a', 'author']
                   ,[u'b_isbn', 'isbn']
                   ,[u'ps', 'pagecount']
                   ,[u'id', 'recguid']
                   ,[u'p_j', 'usertitle']
                   ,[u'p_e', 'usermail']
                   ,[u'ls', 'likes'] ]

    return tangle_lib.subdict_build(element, value_table) 

