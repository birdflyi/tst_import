#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python 3.9

from tst_imp_pkg.utils import util1
# from tst_imp_pkg import top_abc  # circular import
from tst_imp_pkg import top_var
from tst_imp_pkg.top_var import top_var_a
# from .. import top_var
# from .. import top_abc  # circular import
# from ..utils import util1
# from ..top_var import top_var_a


def call_util():
    print(f"get {util1.util1_var}!")
    # print(f"get {top_abc}")
    print(f"get {top_var.top_var_a}!")
    print(f"get {top_var_a} directly!")


if __name__ == '__main__':
    call_util()
