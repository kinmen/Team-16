#!/usr/bin/env python

import sys

current_titleid = None
current_queryid = None
current_qtokens = None
current_ttokens = None
current_click = 0
current_imp = 0

for line in sys.stdin:

    line = line.strip()

    titleid, ttoken, queryid, qtokens, click, impression = line.split('\t')

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
        current_qtokens = qtokens

    else:
        if current_titleid:
            print '%s\t%s\t%s\t%s\t%s\t%s' % (current_titleid, current_ttokens, current_queryid, current_qtokens, current_click, current_imp)
        # reset parameters
        current_titleid = titleid
        current_queryid = None
        current_qtokens = None
        current_click = 0
        current_imp = 0

# print out last line
if current_titleid:
    print '%s\t%s\t%s\t%s\t%s\t%s' % (current_titleid, current_ttokens, current_queryid, current_qtokens, current_click, current_imp)