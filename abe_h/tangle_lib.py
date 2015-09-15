from cStringIO import StringIO

default_settings = dict(
    # mix : between text descriptions, bottom : all code bellow the text
    code_align = 'mix'
    # Base64 encode displayed code (if True, code_align becomes Bottom, no matter what)
    ,code_b64encode = False
    )

if default_settings['code_b64encode'] is True:
    default_settings['code_align'] = 'bottom'

def output_buffer_new():
    return StringIO()

def output_buffer_read(b_file):
    return b_file.getvalue()

def subdict_build(raw_data, value_table):
    out = {}
    for rel in value_table:
        out[rel[1]] = raw_data[rel[0]]
    return out

def arrange(template, subdict):
    return template.format(**subdict)
