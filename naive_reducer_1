#!/usr/bin/env python

import sys


current_uid = None
current_click = 0
current_impression = 0
current_age = None


for line in sys.stdin:

    # remove entrailing white spaces
    line = line.strip()

    # split line to variables
    uid, click, impression, age = line.split('\t')


    if current_uid == uid:

        # if data exists, cumulate
        if click != "-1" and impression != "-1":
            current_click += float(int(click))
            current_impression += float(int(impression))

        # each user should have one age
        if age != "-1":
            current_age = age

    else:
        if current_uid:
            # print stdout
            print '%s\t%s\t%s\t%s' % (current_uid, current_age, current_click, current_impression)
        # reset parameters
            current_click = 0
            current_impression = 0
        current_age = age
        current_uid = uid

# print last line
if current_uid:
    print '%s\t%s\t%s\t%s' % (current_uid, current_age, current_click, current_impression)
