#!/usr/bin/env python

"""
Output:
    'KeyID \t Key_Tokens \t DescriptionID \t Description_Tokens \t QueryID \t Query_Tokens \t TitleID \t Title_Tokens \t Clicks \t Impressions'
"""


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

    if titleid == 'z': # these lines should be the other token files. We don't need to touch these in this job
        print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (keyid, ktoken, descrid, dtoken, qid, qtoken, titleid, ttoken, click, impression)
        continue

    if current_titleid == titleid:
        # the title token should be at the top for the repective key due to the "z" placeholder
        if ttoken != 'z':
            current_ttoken = ttoken

        # we want each unique instance
        if (current_qid != qid or current_keyid != keyid or current_descrid != descrid) and current_qid != 'z':
            if current_click != 'z':
                # make a list of tuples
                current_ids.append((current_keyid, current_ktoken, current_descrid, current_dtoken, current_qid, current_qtoken, current_titleid, current_ttoken, current_click, current_imp))
            # titleid and titletoken features should remain the same, but the other features should be updated
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
            # print out each tuple in the list
            for i in current_ids:
                f = i[:7] + (current_ttoken,) + i[8:]
                print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % f
        # reset parameters
        current_ids = []
        current_titleid = titleid
        current_ttoken = ttoken
        current_qid = qid
        current_qtoken = qtoken
        current_keyid = keyid
        current_ktoken = ktoken
        current_descrid = descrid
        current_dtoken = dtoken
        current_click = click
        current_imp = impression

# print last line
if current_titleid:
    for i in current_ids:
        f = i[:7] + (current_ttoken,) + i[8:]
        print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % f

