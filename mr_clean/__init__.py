# -*- coding: utf-8 -*-

__all__ = ['mr_clean',
'pre_clean','cleaner',
'mc_checks','mc_funcs',
'mc_stats','mc_utils']

dependencies = ['pandas','numpy']
missing_dependencies = []

for dependency in dependencies:
    try:
        __import__(dependency)
    except ImportError as e:
        missing_dependencies.append(dependency)

if missing_dependencies:
    raise ImportError("Missing required dependencies {0}".format(missing_dependencies))
del(dependencies)
del(dependency)
del(missing_dependencies)

from mr_clean.main.api import *
