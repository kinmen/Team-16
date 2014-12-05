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
    keyid, key_token, descrid, descr_token, qid, query_token, titleid, title_token, click, impression = line.split('\t')
    if keyid == "-1":
        print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' %  (descrid, descr_token, qid, query_token, titleid, title_token, keyid, key_token, click, impression)
        continue
    if current_keyid == keyid:
        if key_token != 'z':
            current_ktoken = key_token
        if current_titleid != titleid or current_qid != qid or current_descrid != descrid:
            if current_click != 'z':
                current_ids.append((current_descrid, current_dtoken, current_qid, current_qtoken, current_titleid, current_ttoken, current_keyid, current_ktoken, current_click, current_imp))
                #print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' %  (current_descrid, current_dtoken, current_qid, current_qtoken, current_titleid, current_ttoken, current_keyid, current_ktoken, current_click, current_imp)
            current_titleid = titleid
            current_ttoken = title_token
            current_qid = qid
            current_qtoken = query_token
            current_keyid = keyid
            current_descrid = descrid
            current_dtoken = descr_token
            current_click = click
            current_imp = impression


    else:
        if current_keyid:
            for i in current_ids:
                f = i[:7] + (current_ktoken,) + i[8:]
                print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % f
            #print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' %  (current_descrid, current_dtoken, current_qid, current_qtoken, current_titleid, current_ttoken, current_keyid, current_ktoken, current_click, current_imp)
        current_ids = []
        current_titleid = titleid
        current_ttoken = title_token
        current_qid = qid
        current_qtoken = query_token
        current_keyid = keyid
        current_ktoken = key_token
        current_descrid = descrid
        current_dtoken = descr_token
        current_click = click
        current_imp = impression

if current_keyid:
    for i in current_ids:
        f = i[:7] + (current_ktoken,) + i[8:]
        print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % f
    #print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' %  (current_descrid, current_dtoken, current_qid, current_qtoken, current_titleid, current_ttoken, current_keyid, current_ktoken, current_click, current_imp)
