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
current_uid = None
current_age = None
current_gender = None
current_qids = []

for line in sys.stdin:

    # eliminate entrailing white spaces
    line = line.strip()

    # split for indexing
    queryid, query_token, titleid, title_token, keyid, key_token, descrid, descr_token, click, impression, uid, age, gender = line.split('\t')
    if queryid == "z":
        print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (titleid, title_token, keyid, key_token, descrid, descr_token, queryid, query_token, click, impression, uid, age, gender)
        continue
    if current_qid == queryid:
        if query_token != 'z':
            current_qtoken = query_token
        if (current_titleid != titleid or current_keyid != keyid or current_descrid != descrid) and current_title != 'z':
            if current_click != 'z':
                current_qids.append((current_titleid, current_ttoken, current_keyid, current_ktoken, current_descrid, current_dtoken, current_qid, current_qtoken, current_click, current_imp))
                #print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' %  (current_titleid, current_ttoken, current_keyid, current_ktoken, current_descrid, current_dtoken, current_qid, current_qtoken, current_click, current_imp)
            current_titleid = titleid
            current_ttoken = title_token
            current_qid = queryid
            current_keyid = keyid
            current_ktoken = key_token
            current_descrid = descrid
            current_dtoken = descr_token
            current_click = click
            current_imp = impression
    else:
        if current_qid:
            for i in current_qids:
                f = i[:7] + (current_qtoken,) + i[8:]
                print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % f
        current_qids = []
        current_titleid = titleid
        current_ttoken = title_token
        current_qid = queryid
        current_qtoken = query_token
        current_keyid = keyid
        current_ktoken = key_token
        current_descrid = descrid
        current_dtoken = descr_token
        current_click = click
        current_imp = impression
        current_uid = uid
        current_age = age
        current_gender = gender

if current_qid:
    for i in current_qids:
        f = i[:7] + (current_qtoken,) + i[8:]
        print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % f