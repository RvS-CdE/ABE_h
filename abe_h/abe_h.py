# -*- coding: utf-8 -*-
from importlib import import_module
import sys, os
sys.path = [os.path.abspath(os.path.dirname(__file__))] + sys.path


def tangle( Input, Format):
    tangler = get_tangler(Format)

def get_tangler(Format):
    tangler = import_module('abe_formats.' + Format)
    return tangler
