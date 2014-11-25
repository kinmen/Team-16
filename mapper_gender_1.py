#!/usr/bin/env python

import sys

for line in sys.stdin:

    # setting default parameters for sorting
    uid = -1
    gender = -1
    click = -1
    impression = -1

    # eliminate entrailing white spaces
    line = line.strip()

    # split for indexing
    line = line.split('\t')

    # for data
    if len(line) > 3:
        click = line[2]
        impression = line[3]
        uid = line[-1]
        print '%s\t%s\t%s\t%s' % (uid, click, impression, gender)
    else:
        uid = line[0]
        gender = line[1]
        print '%s\t%s\t%s\t%s' % (uid, click, impression, gender)
        #gender is 1 for male, 2 for female, 0 for unknown
