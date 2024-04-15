# -*- coding: utf-8 -*-

__version__ = '1.0.0'

import os

curPath = os.path.dirname(os.path.realpath(__file__))

os.add_dll_directory(os.path.join(curPath,'bin'))
os.environ["PATH"] += os.pathsep + os.path.join(curPath,'bin')
os.environ["GI_TYPELIB_PATH"] = os.path.join(curPath,'lib','girepository-1.0')