#!/usr/bin/env python

"""
Input:
    Output of naive_mapper_tok_4.py and naive_reducer_tok_4.py
Output:
    'UserID, Age, Gender, QT_ratio, QK_ratio, QD_ratio, QTK_ratio, QTD_ratio, QKD_ratio, QTDK_ratio, Click, Impression'
"""

import sys

for line in sys.stdin:

    line = line.strip()
    #qid, qtoken, titleid, ttoken, keyid, ktoken, descrid, dtoken, click, imp, uid, age, gender
    qid, query_token, titleid, title_token, keyid, key_token, descrid, descr_token, click, impression, uid, age, gender = line.split('\t')

    ### this creates a list of the tokens, splitting on the | they are
    ### separated by in the original data
    qtokens = query_token.split('|')
    ttokens = title_token.split('|')
    ktokens = key_token.split('|')
    dtokens = descr_token.split('|')
    tk_tokens = ttokens + ktokens
    td_tokens = ttokens + dtokens
    kd_tokens = ktokens + dtokens
    tkd_tokens = ttokens + ktokens + dtokens

    ### This loops through the ttok with the qtok to find and return
    ### any matching values as a list
    qt_matched = list(set(qtokens).intersection(ttokens))
    qk_matched = list(set(qtokens).intersection(ktokens))
    qd_matched = list(set(qtokens).intersection(dtokens))
    qtk_matched = list(set(qtokens).intersection(tk_tokens))
    qtd_matched = list(set(qtokens).intersection(td_tokens))
    qkd_matched = list(set(qtokens).intersection(kd_tokens))
    qtkd_matched = list(set(qtokens).intersection(tkd_tokens))

    ### this calculates the ratio of matching tokens to the query
    ### len(qtok) tell us how many tokens are in the query
    qt_ratio = float(len(qt_matched))/float(len(qtokens))
    qk_ratio = float(len(qk_matched))/float(len(qtokens))
    qd_ratio = float(len(qd_matched))/float(len(qtokens))
    qtk_ratio = float(len(qtk_matched))/float(len(qtokens))
    qtd_ratio = float(len(qtd_matched))/float(len(qtokens))
    qkd_ratio = float(len(qkd_matched))/float(len(qtokens))
    qtkd_ratio = float(len(qtkd_matched))/float(len(qtokens))

    ### this prints the user, age, gender, qt_simi, qk_simi, qd_simi, qtk_simi, qtd_simi, qkd_simi, qtkd_simi, trueclicks, impressions

    print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (uid, age, gender, qt_ratio, qk_ratio, qd_ratio, qtk_ratio, qtd_ratio, qkd_ratio, qtkd_ratio, click, impression)

