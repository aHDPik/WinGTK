# -*- coding: utf-8 -*-

__version__ = '1.0.0'

import os

curPath = os.path.dirname(os.path.realpath(__file__))

os.add_dll_directory(curPath)
os.environ["PATH"] += os.pathsep + curPath
os.environ["GI_TYPELIB_PATH"] = curPath