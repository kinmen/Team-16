#!/usr/bin/env python

import sys

current_titleid = None
current_ttoken = None
current_qid = None
current_qtoken = None
current_click = 0
current_imp = 0


for line in sys.stdin:

    # eliminate entrailing white spaces
    line = line.strip()

    # split for indexing
    titleid, title_token, queryid, query_token, click, impression = line.split('\t')
    try:
        click = int(click)
        impression = int(impression)
    except ValueError:
        continue
    if current_titleid == titleid:
        if title_token != "-1":
            current_ttoken = title_token
        if click != -1 and impression != -1:
            current_click += click
            current_imp += impression

    else:
        if current_titleid:
            print '%s\t%s\t%s\t%s\t%s\t%s' %  (current_titleid, current_ttoken, current_qid, current_qtoken, current_click, current_imp)
        current_titleid = titleid
        current_ttoken = title_token
        current_qid = queryid
        current_qtoken = query_token
        current_click = 0
        current_imp = 0

if current_titleid:
    print '%s\t%s\t%s\t%s\t%s\t%s' %  (current_titleid, current_ttoken, current_qid, current_qtoken, current_click, current_imp)