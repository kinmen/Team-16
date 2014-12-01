#!/usr/bin/env python

import sys

current_titleid = None
current_queryid = None
current_qtokens = None
current_ttokens = []
current_click = 0
current_imp = 0

for line in sys.stdin:
    line = line.strip()
    titleid, ttoken, queryid, qtokens, click, impression = line.split('\t')
    try:
        qtoken = eval(qtoken)
        ttoken = eval(ttoken)
        click = int(click)
        imp = int(impressions)
    if current_titleid == titleid:
        # cumulate title tokens, clicks, and impressions
        current_ttoken = current_ttoken + token
        current_click += click
        current_imp += imp
        # the rest are already set from the previous mapreduce
        current_queryid = queryid
        current_qtokens = qtokens

    else:
        if current_titleid:
            print '%s\t%s\t%s\t%s\t%s\t%s' % (current_titleid, current_ttokens,\
                current_queryid, current_qtokens, current_click, current_imp)
        current_titleid = titleid
        current_queryid = None
        current_qtokens = None
        current_click = 0
        current_imp = 0
        current_ttokens = ttokens