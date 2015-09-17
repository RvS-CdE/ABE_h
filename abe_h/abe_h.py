# -*- coding: utf-8 -*-
from importlib import import_module
import tangle_lib
import sys, os, json, re
sys.path = [os.path.abspath(os.path.dirname(__file__))] + sys.path


################################################################## API FUNCTIONS
################################################################################
def unite( Type, Code, RawFields=None):
    fitter = get_fitter(Type)

    if RawFields is None:
        fields = fitter.get_fields(Code)
    else:
        fields = get_fields(RawFields)

    template = fitter.get_template()
    fields[u'code'] = Code
    return template.format(**fields)

def code(Text):
    pattern = re.compile('```[^\s]*(.+?)```', re.DOTALL)
    buff = []
    for match in re.findall(pattern,Text):
        buff.append( match.strip()+'\n')
    return ''.join(buff)

def text(Text):
    return re.sub('```.+?```', '\n', Text,0,re.DOTALL).strip() + '\n'

############################################################# INTERNAL FUNCTIONS
################################################################################

def get_fitter(Format):
    fitter = import_module('abe_formats.' + Format)
    return fitter


def get_fields(RawJsonFields):
    u_fields = json.loads(RawJsonFields)
    return convert_keys_to_string(u_fields)

## Excerpt from:
## http://stackoverflow.com/questions/1254454/fastest-way-to-convert-a-dicts-keys-values-from-unicode-to-str
def convert_keys_to_string(dictionary):
    """Recursively converts dictionary keys to strings."""
    if not isinstance(dictionary, dict):
        return dictionary
    return dict((str(k), convert_keys_to_string(v)) 
        for k, v in dictionary.items())

#def tangle( Input, Format, Opts=None):
#    if Opts is None:
#        Opts = tangle_lib.default_settings
#
#    tangler = get_tangler(Format)
#    element_template = tangler.get_template()
#    element_data = tangler.get_translated_data(Input)
#
#    mix_code = Opts['code_align'] == 'mix'
#    output_buffer = tangle_lib.buffer_new()
#
#    if mix_code:
#        pass
#    else:
#        code_buffer = tangle_lib.buffer_new()
#        code_buffer.write(tangler.get_code_block(Input))
#        for raw_element in element_data:
#            refined_element = tangler.get_refined_element(raw_element,Opts)
#            if mix_code:
#            output_buffer.write( tangle_lib.arrange(element_template, refined_element,Opts) )
#        output_buffer.write(tangle_lib.buffer_read(code_buffer)
#
#    return tangle_lib.buffer_read(output_buffer)
