#!/usr/bin/env python
"""
Output:
    'UserId \t Age \t Gender \t DescriptionID \t Description_Tokens \t QueryID \t Query_Tokens \t TitleID \t Title_Tokens \t KeyID \t Key_Tokens \t Clicks \t Impressions'
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
current_uid = None
current_age = None
current_gender = None
current_ids = []



for line in sys.stdin:

    # eliminate entrailing white spaces
    line = line.strip()

    # split for indexing
    uid, age, gender, descrid, descr_token, qid, query_token, titleid, title_token, keyid, key_token, click, impression  = line.split('\t')

    if current_uid == uid:
        # the age and gender should be at the top due to "z" placeholder
        if age != 'z' and gender != 'z':
            current_age = age
            current_gender = gender
        else: # we want each unique instance
            if (current_titleid != titleid or current_keyid != keyid or current_qid != qid or current_descrid != descrid):
                if current_click != 'z':
                    # make a lsit of tuples
                    current_ids.append((current_qid, current_qtoken, current_titleid, current_ttoken, current_keyid, current_ktoken, current_descrid, current_dtoken, current_click, current_imp, current_uid, current_age, current_gender))
                # age, gender and userid features should remain the same, but the other features should be updated
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

    else:
        if current_uid:
            # print out each tuple in the list
            for i in current_ids:
                f = i[:11] + (current_age, current_gender)
                print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % f
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
        current_uid = uid
        current_age = age
        current_gender = gender

# print out last line
if current_uid:
    for i in current_ids:
        f = i[:11] + (current_age, current_gender)
        print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % f
