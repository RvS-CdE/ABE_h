# -*- coding: utf-8 -*-
from importlib import import_module
import tangle_lib
import sys, os
sys.path = [os.path.abspath(os.path.dirname(__file__))] + sys.path


def tangle( Input, Format):
    tangler = get_tangler(Format)
    element_template = tangler.get_template()
    element_data = tangler.get_translated_data(Input)

    output_buffer = tangle_lib.output_buffer_new()

    for raw_element in element_data:
        refined_element = tangler.get_formatting_data(raw_element)
        output_buffer.write( tangle_lib.arrange(element_template, refined_element) )

    return tangle_lib.output_buffer_read(output_buffer)

def get_tangler(Format):
    tangler = import_module('abe_formats.' + Format)
    return tangler
