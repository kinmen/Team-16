#!/usr/bin/env python

"""
Outputs:
    'Gender \t Clicks \t Impressions'
"""

import sys


current_uid = None
current_click = 0
current_impression = 0
current_gender = None


for line in sys.stdin:

    # remove entrailing white spaces
    line = line.strip()

    # split line to variables
    uid, click, impression, gender = line.split('\t')


    if current_uid == uid:

        # if data exists, cumulate
        if click != "-1" and impression != "-1":
            current_click += float(int(click))
            current_impression += float(int(impression))

        # each user should have one gender
        if gender != "-1":
            current_gender = gender

    else:
        if current_uid:
            # print stdout
            # print '%s\t%s\t%s\t%s' % (current_uid, current_gender, current_click, current_impression)
            print '%s\t%s\t%s' % (current_gender, current_click, current_impression)
        # reset parameters
        if click != "-1" and impression != "-1":
            current_click = float(int(click))
            current_impression = float(int(impression))
        else:
            current_click = 0
            current_impression = 0
        current_gender = gender
        current_uid = uid

# print last line
if current_uid:
    # print '%s\t%s\t%s\t%s' % (current_uid, current_gender, current_click, current_impression)
    print '%s\t%s\t%s' % (current_gender, current_click, current_impression)
    ##gender is 1 for male, 2 for female, 0 for 'unknown'
