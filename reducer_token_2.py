#!/usr/bin/env python

import sys

current_titleid = None
current_queryid = None
current_qtoken = None
current_ttoken = None
current_click = 0
current_imp = 0

for line in sys.stdin:

    line = line.strip()

    titleid, ttoken, queryid, qtoken, click, impression = line.split('\t')

    # just in case they are still around
    if click != "-1" and impression != "-1":
        try:
            click = int(click)
            imp = int(impression)
        except:
            continue
    else:
        click = 0
        imp = 0

    if current_titleid == titleid:
        # cumulate title tokens, clicks, and impressions
        current_ttoken = ttoken
        current_click += click
        current_imp += imp
        # the rest are already set from the previous mapreduce
        current_queryid = queryid
        current_qtoken = qtoken

    else:
        if current_titleid:
            print '%s\t%s\t%s\t%s\t%s\t%s' % (current_titleid, current_ttoken, current_queryid, current_qtoken, current_click, current_imp)
        # reset parameters
        current_titleid = titleid
        current_queryid = queryid
        current_qtoken = qtoken
        current_click = click
        current_imp = imp
        current_ttoken = ttoken

# print out last line
if current_titleid:
    print '%s\t%s\t%s\t%s\t%s\t%s' % (current_titleid, current_ttoken, current_queryid, current_qtoken, current_click, current_imp)