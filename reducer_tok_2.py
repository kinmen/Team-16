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
current_ids = []


for line in sys.stdin:

    # eliminate entrailing white spaces
    line = line.strip()

    # split for indexing
    titleid, ttoken, keyid, ktoken, descrid, dtoken, qid, qtoken, click, impression = line.split('\t')
    try:
        click = int(click)
        impression = int(impression)
    except ValueError:
        continue
    if titleid == 'z':
        print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (keyid, ktoken, descrid, dtoken, qid, qtoken, titleid, ttoken, click, impression)
        continue
    if current_titleid == titleid:
        if ttoken != 'z':
            current_ttoken = ttoken
        if current_qid != qid or current_keyid != keyid or current_descrid != descrid:
            if current_click != 'z':
                current_ids.append((current_keyid, current_ktoken, current_descrid, current_dtoken, current_qid, current_qtoken, current_titleid, current_ttoken, current_click, current_imp))
                #print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' %  (current_keyid, current_ktoken, current_descrid, current_dtoken, current_qid, current_qtoken, current_titleid, current_ttoken, current_click, current_imp)
            current_titleid = titleid
            current_qid = qid
            current_qtoken = qtoken
            current_keyid = keyid
            current_ktoken = ktoken
            current_descrid = descrid
            current_dtoken = dtoken
            current_click = click
            current_imp = impression


    else:
        if current_titleid:
            for i in current_ids:
                f = i[:7] + (current_ttoken,) + i[8:]
                print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % f
            #print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' %  (current_keyid, current_ktoken, current_descrid, current_dtoken, current_qid, current_qtoken, current_titleid, current_ttoken, current_click, current_imp)
        current_ids = []
        current_titleid = titleid
        current_ttoken = ttoken
        current_qid = qid
        current_qtoken = qtoken
        current_keyid = keyid
        current_ktoken = ktoken
        current_descrid = descrid
        current_dtoken = dtoken
        if click != -1 and impression != -1:
            current_click = click
            current_imp = impression

if current_titleid:
    for i in current_ids:
        f = i[:7] + (current_ttoken,) + i[8:]
        print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % f
     #print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' %  (current_keyid, current_ktoken, current_descrid, current_dtoken, current_qid, current_qtoken, current_titleid, current_ttoken, current_click, current_imp)
