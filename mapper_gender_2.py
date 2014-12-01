#!/usr/bin/env python

import sys

for line in sys.stdin:

    # remove entrailing white spaces
    line = line.strip()

    # assign variables
    gender, click, impression  = line.split('\t')

    # print stdout
    print '%s\t%s\t%s' % (gender, click, impression)
