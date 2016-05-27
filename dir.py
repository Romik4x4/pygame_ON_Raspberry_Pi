#!/usr/bin/python

import os

for dirname, dirnames, filenames in os.walk('/home/romik/img/'):
    # print path to all subdirectories first.
    for subdirname in dirnames:
        print(os.path.join(dirname, subdirname))

    # print path to all filenames.
    for filename in filenames:
        print(os.path.join(dirname, filename))
