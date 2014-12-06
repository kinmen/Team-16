#!/usr/bin/env python

"""
Input:
    Output of mapper_tok_4.py and reducer_tok_4.py
Output:
    query_token_ratio, 'qt_simi', Click, Impression
    query_key_ratio, 'qk_simi', Click, Impression
    query_description_ratio, 'qd_simi', Click, Impression
    query_token_key_ratio, 'qtk_simi', Click, Impression
    query_token_description_ratio, 'qtd_simi', Click, Impression
    query_key_dexcription_ratio, 'qkd_simi', Click, Impression
    query_token_key_description_ratio, 'qtkd_simi', Click, Impression
"""



import sys

for line in sys.stdin:

    line = line.strip()
    line = line.split('\t')

    query_token = line[1]
    title_token = line[3]
    key_token = line[5]
    descr_token = line[7]

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

    ### this prints the ratio, 'simil' type, clicks, impressions
    print '%s\t%s\t%s\t%s' % (qt_ratio, 'qt_simi', line[8], line[9])
    print '%s\t%s\t%s\t%s' % (qk_ratio, 'qk_simi', line[8], line[9])
    print '%s\t%s\t%s\t%s' % (qd_ratio, 'qd_simi', line[8], line[9])
    print '%s\t%s\t%s\t%s' % (qtk_ratio, 'qtk_simi', line[8], line[9])
    print '%s\t%s\t%s\t%s' % (qtd_ratio, 'qtd_simi', line[8], line[9])
    print '%s\t%s\t%s\t%s' % (qkd_ratio, 'qkd_simi', line[8], line[9])
    print '%s\t%s\t%s\t%s' % (qtkd_ratio, 'qtkd_simi', line[8], line[9])
