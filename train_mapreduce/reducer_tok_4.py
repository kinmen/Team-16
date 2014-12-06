#!/usr/bin/env python

"""
Output:
    'QueryID \t Query_Tokens \t TitleID \t Title_Tokens \t KeyID \t Key_Tokens \t DescriptionID \t Description_Tokens \t Clicks \t Impressions'
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
    descrid, descr_token, qid, query_token, titleid, title_token, keyid, key_token, click, impression = line.split('\t')

    if current_descrid == descrid:
        # the title token should be at the top for the respective key due to "z" placeholder
        if descr_token != 'z':
            current_dtoken = descr_token

        # we want each unique instance
        if (current_titleid != titleid or current_keyid != keyid or current_qid != qid) and current_titleid != 'z':
            if current_click != 'z':
                # make a list of tuples
                current_ids.append((current_qid, current_qtoken, current_titleid, current_ttoken, current_keyid, current_ktoken, current_descrid, current_dtoken, current_click, current_imp))
            # descriptionid and description token features should remain the same, but the other features should be updated
            current_titleid = titleid
            current_ttoken = title_token
            current_qid = qid
            current_qtoken = query_token
            current_keyid = keyid
            current_ktoken = key_token
            current_descrid = descrid
            current_click = click
            current_imp = impression


    else:
        if current_descrid:
            # print out each tuple in the list
            for i in current_ids:
                f = i[:7] + (current_dtoken,) + i[8:]
                print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % f
        # reset parameters
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

# print last line
if current_descrid:
    for i in current_ids:
        f = i[:7] + (current_dtoken,) + i[8:]
        print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % f
