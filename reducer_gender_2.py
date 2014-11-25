#!/usr/bin/env python

import sys

current_click = 0
current_impression = 0
current_gender = None

for line in sys.stdin:

    # remove entrailing white spaces
    line = line.strip()

    # assign variables
    gender, click, impression = line.split('\t')

    # filter out bad data
    try:
        click = float(click)
        impression = float(impression)
    except ValueError:
        continue

    # cumulate data based on gender
    if current_gender == gender:
        current_click += click
        current_impression += impression

    else:
        # print stdout
        if current_gender:
            print '%s\t%s\t%f\t%f' % (current_gender, 'gender', current_click, current_impression)
        # reset parameters
        current_click = click
        current_impression = impression
        current_gender = gender

# print last line
if current_gender:
    print '%s\t%s\t%f\t%f' % (current_gender, 'gender', current_click, current_impression)
