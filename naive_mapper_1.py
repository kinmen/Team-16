#!/usr/bin/env python

import sys

for line in sys.stdin:

    # setting default parameters for sorting
    uid = -1
    age = -1
    click = -1
    impression = -1
    typeofdata = -1

    # eliminate entrailing white spaces
    line = line.strip()

    # split for indexing
    line = line.split('\t')

    # for data
    if len(line) > 3:
        typeofdata = line[1]
        click = line[2]
        impression = line[3]
        uid = line[-1]
        print '%s\t%s\t%s\t%s\t%s' % (uid, click, impression, age, typeofdata)
    else:
        uid = line[0]
        age = line[-1]
        print '%s\t%s\t%s\t%s\t%s' % (uid, click, impression, age, typeofdata)
