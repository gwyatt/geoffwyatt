#!/usr/bin/python

import os
from sys import argv

if len(argv) == 2:
    arg = argv[1]
else:
    arg = None

if arg == "prod":
    os.system("rm -rf deploy/")
    os.system("hyde gen -c prod.yaml")
    os.system("hyde serve")
else:
    os.system("rm -rf deploy/")
    os.system("hyde gen")
    os.system("hyde serve")