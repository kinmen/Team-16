#!/usr/bin/env python

import sys

current_titleid = None
current_ttoken = None
current_keyid = None
current_ktoken = None
current_descrid = None
current_dtoken = None
current_qid = None
current_qtoken = None
current_click = 0
current_imp = 0


for line in sys.stdin:

    # eliminate entrailing white spaces
    line = line.strip()

    # split for indexing
    titleid, ttoken, keyid, ktoken, descrid, dtoken, qid, qtoken, click, imp = line.split('\t')
    try:
        click = int(click)
        impression = int(impression)
    except ValueError:
        continue
    if titleid == "-1":
        print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (keyid, ktoken, descrid, dtoken, qid, qtoken, titleid, ttoken, click, imp)
    if current_titleid == titleid:
        if title_token != "-1":
            current_ttoken = title_token
        if click != -1 and impression != -1:
            current_click += click
            current_imp += impression

    else:
        if current_titleid:
            print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' %  (current_keyid, current_ktoken, current_descrid, current_dtoken, current_qid, current_qtoken, current_titleid, current_ttoken, current_click, current_imp)
        current_titleid = titleid
        current_ttoken = title_token
        current_qid = queryid
        current_qtoken = query_token
        current_keyid = keyid
        current_ktoken = key_token
        current_descrid - descrid
        current_dtoken = descr_token
        current_click = 0
        current_imp = 0

if current_titleid:
     print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' %  (current_keyid, current_ktoken, current_descrid, current_dtoken, current_qid, current_qtoken, current_titleid, current_ttoken, current_click, current_imp)
