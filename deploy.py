#!/usr/bin/python

import os

# Clean deployment folder, generate new site, serve via hyde webserver
os.system("rm -rf deploy/")
os.system("hyde gen")
os.system("hyde serve")