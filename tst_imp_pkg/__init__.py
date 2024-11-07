#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python 3.9

# @Time   : 2024/11/8 0:38
# @Author : 'Lou Zehua'
# @File   : __init__.py.py 

import os
import sys

if '__file__' not in globals():
    # !pip install ipynbname  # Remove comment symbols to solve the ModuleNotFoundError
    import ipynbname

    nb_path = ipynbname.path()
    __file__ = str(nb_path)
cur_dir = os.path.dirname(__file__)
pkg_rootdir = os.path.dirname(cur_dir)  # os.path.dirname()向上一级，注意要对应工程root路径
if pkg_rootdir not in sys.path:  # 解决ipynb引用上层路径中的模块时的ModuleNotFoundError问题
    sys.path.append(pkg_rootdir)
    print('-- Add root directory "{}" to system path.'.format(pkg_rootdir))

from tst_imp_pkg import utils, script  # sub-package needs to be imported and to extend __all__
from tst_imp_pkg.top_var import *   # var or func/module in other file needs to be imported from file

__all__ = [
    "script",  # sub-package needs to be imported and to extend __all__
    "utils",  # sub-package needs to be imported and to extend __all__
    "top_var",   # file in this package just list out
    "top_module",  # var or func/module in other file needs to be imported from file
    "top_var_a",    # var or func/module in other file needs to be imported from file
    "top_abc"  # var in this file just list out
]

# sub-package needs to be imported and to extend __all__
__all__.extend(script.__all__)
__all__.extend(utils.__all__)

top_abc = "top_abc"
