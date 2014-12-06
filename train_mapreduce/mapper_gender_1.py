#!/usr/bin/env python

"""
Inputs:
    1. Training data files
    2. userid_profile.txt

Outputs:
    'UserID \t Clicks \t Impressions \t Gender'
"""

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
    if len(line) > 3: # if instances
        click = line[2]
        impression = line[3]
        uid = line[-1]
        print '%s\t%s\t%s\t%s' % (uid, click, impression, gender)
    else: # if userid_profile.txt file
        uid = line[0]
        gender = line[1]
        print '%s\t%s\t%s\t%s' % (uid, click, impression, gender)
        #gender is 1 for male, 2 for female, 0 for 'unknown'
