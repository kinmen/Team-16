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
current_ids = []


for line in sys.stdin:

    # eliminate entrailing white spaces
    line = line.strip()

    # split for indexing
    titleid, ttoken, keyid, ktoken, descrid, dtoken, qid, qtoken, click, impression, uid, age, gender = line.split('\t')
    if titleid == "z":
        print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (keyid, ktoken, descrid, dtoken, qid, qtoken, titleid, ttoken, click, impression, uid, age, gender)
        continue
    if current_titleid == titleid:
        if ttoken != 'z':
            current_ttoken = ttoken
        if (current_qid != qid or current_keyid != keyid or current_descrid != descrid) and current_qid != 'z':
            if current_click != 'z':
                current_ids.append((current_keyid, current_ktoken, current_descrid, current_dtoken, current_qid, current_qtoken, current_titleid, current_ttoken, current_click, current_imp, current_uid, current_age, current_gender))
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
            current_uid = uid
            current_age = age
            current_gender = gender


    else:
        if current_titleid:
            for i in current_ids:
                f = i[:7] + (current_ttoken,) + i[8:]
                print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % f
        current_titleid = titleid
        current_ids = []
        current_ttoken = ttoken
        current_qid = qid
        current_qtoken = qtoken
        current_keyid = keyid
        current_ktoken = ktoken
        current_descrid = descrid
        current_dtoken = dtoken
        current_click = click
        current_imp = impression
        current_uid = uid
        current_age = age
        current_gender = gender

if current_titleid:
    for i in current_ids:
        f = i[:7] + (current_ttoken,) + i[8:]
        print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % f