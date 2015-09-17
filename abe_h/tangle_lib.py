from __future__ import print_function
#from cStringIO import StringIO

def fielddict_build(raw_data, value_table):
    if type(raw_data) is not dict or type(value_table) is not list:
        print(raw_data)
        print(value_table)
        raise TypeError("Invalid parameter types")

    out = {}
    for rel in value_table:
        if rel[0] not in raw_data:
            warning("Raw data table did not contain key "+rel[0])
            continue
        out[rel[1]] = raw_data[rel[0]]
    return out

#default_settings = dict(
#    # mix : between text descriptions, bottom : all code bellow the text
#    code_align = 'mix'
#    # Base64 encode displayed code (if True, code_align becomes Bottom, no matter what)
#    ,code_b64encode = False
#    )
#
#if default_settings['code_b64encode'] is True:
#    default_settings['code_align'] = 'bottom'
#
#def buffer_new():
#    return StringIO()
#
#def buffer_read(b_file):
#    if type(b_file).__name__ != 'StringO':
#        raise TypeError("Output buffer must be of type StringIO")
#    return b_file.getvalue()
#
#def subdict_build(raw_data, value_table):
#    if type(raw_data) is not dict or type(value_table) is not list:
#        raise TypeError("Invalid parameter types")
#
#    out = {}
#    for rel in value_table:
#        if rel[0] not in raw_data:
#            warning("Raw data table did not contain key "+rel[0])
#            continue
#        out[rel[1]] = raw_data[rel[0]]
#    return out
#
#def arrange(template, subdict, Opts):
#    if not hasattr(template,'format'):
#        raise TypeError("Template must have a 'format' attribute")
#    if type(subdict) is not dict:
#        raise TypeError("Subdict must contain a valid dictionary")
#
#
#    return template.format(**subdict)



def warning(*objs):
    print("WARNING: ", *objs, file=sys.stderr)
