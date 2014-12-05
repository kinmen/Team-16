#!/usr/bin/env python

"""
Outputs:
    'TitleID \t Title_Tokens \t KeyID \t Key_Tokens \t DescriptionID \t Description_Tokens \t QueryID \t Query_Tokens \t Clicks \t Impressions'
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
current_qids = []

for line in sys.stdin:

    # eliminate entrailing white spaces
    line = line.strip()

    # split for indexing
    queryid, query_token, titleid, title_token, keyid, key_token, descrid, descr_token, click, impression = line.split('\t')

    if queryid == 'z': # these lines should be the other token files. We don't need to touch them in this job.
        print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (titleid, title_token, keyid, key_token, descrid, descr_token, queryid, query_token, click, impression)
        continue

    if current_qid == queryid:
        # the query token should be at the top for the respective key due to the "z" placeholder
        if query_token != 'z':
            current_qtoken = query_token

        # we want each unique instance
        if (current_titleid != titleid or current_keyid != keyid or current_descrid != descrid) and current_titleid != 'z':
            if current_click != 'z': # if its not a token file
                # make a list of tuples
                current_qids.append((current_titleid, current_ttoken, current_keyid, current_ktoken, current_descrid, current_dtoken, current_qid, current_qtoken, current_click, current_imp))
            # queryid and querytoken files should remain the same, but the other features should be updated
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
            # print out each tuple in the list
            for i in current_qids:
                f = i[:7] + (current_qtoken,) + i[8:]
                print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % f
        # reset parameters
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

# print last line
if current_qid:
    for i in current_qids:
        f = i[:7] + (current_qtoken,) + i[8:]
        print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % f

