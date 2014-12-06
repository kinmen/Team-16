#!/usr/bin/env python

"""
Inputs:
    1. Training data files
Outputs:
    'Value \t feature \t Clicks \t Impressions'
"""

import sys

for line in sys.stdin:

    # eliminate entrailing white spaces
    line = line.strip()

    # split for indexing]
    line = line.split('\t')

    # for data
    if len(line) > 3: # if instances
        click = line[2]
        impression = line[3]
        uid = line[-1]
        depth = line[7]
        position = line[8]
        rel_pos = (depth - position)/depth
        print '%s\t%s\t%s\t%s' % (depth, 'depth', click, impression)
        print '%s\t%s\t%s\t%s' % (position, 'position', click, impression)
        print '%s\t%s\t%s\t%s' % (rel_pos, 'relpos', click, impression)
        #value, feature, click, imp
