#!/usr/bin/env python

import sys
import os.path
sys.path.append(os.path.dirname(__file__))

# -cacheFile s3://stat157-uq85def/shared/track2/userid_profile.txt#userid_profile.txt

## if testing on personal comp:
# with(open('smalluser.txt', 'r')) as f:
with(open('userid_profile.txt', 'r')) as f:
        lines = f.readlines()
for each in lines:

    # set default parameters
    uid = -1
    age = -1
    click = -1
    impression = -1

    # remove empty white spaces
    each = each.strip()

    # split for indexing
    each = each.split('\t')

    # for userid_profile.txt
    uid = each[0]
    age = each[-1]
    print '%s\t%s\t%s\t%s' % (uid, click, impression, age)



for line in sys.stdin:

    # setting default parameters for sorting
    uid = -1
    age = -1
    click = -1
    impression = -1

    # eliminate entrailing white spaces
    line = line.strip()

    # split for indexing
    line = line.split('\t')

    # for data
    ## while testing on personal machine
    # click = line[0]
    # impression = line[1]
    click = line[2]
    impression = line[3]
    uid = line[-1]
    print '%s\t%s\t%s\t%s' % (uid, click, impression, age)

