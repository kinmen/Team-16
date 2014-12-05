#!/usr/bin/env python
"""
Note: the .txt files refer to the outputs after running their respective MapReduce Job
================================================================================================
Inputs:
    1. Training data files
    2. titleid_tokensid.txt
    3. queryid_tokensid.txt
    4. descriptionsid_tokensid.txt
    5. purchasedkeywordid_tokensid.txt

Outputs:
'QueryID \t Query_Tokens \t TitleID \t Title_Tokens \t KeyID \t Key_Tokens \t DescriptionID \t Description_Tokens \t Clicks \t Impressions'
================================================================================================
"""


import sys

for line in sys.stdin:

    # setting default parameters for sorting
    queryid = 'z'
    titleid = 'z'
    keyid = 'z'
    descrid = 'z'
    query_tokens = 'z'
    title_tokens = 'z'
    key_tokens = 'z'
    descr_tokens = 'z'
    click = 'z'
    impression = 'z'

    # eliminate entrailing white spaces
    line = line.strip()

    # split for indexing
    line = line.split('\t')

    # parse to accomodate for all inputs
    if len(line) > 3:
        # get clicks, impressions, and ids
        click = line[2]
        impression = line[3]
        queryid = line[9]
        keyid = line[10]
        titleid = line [11]
        descrid = line[12]
        print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (queryid, query_tokens, titleid, title_tokens, keyid, key_tokens, descrid, descr_tokens, click, impression)
    elif line[0] == 'title':
        # get title information
        titleid = line[1]
        title_tokens = line[2]
        print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (queryid, query_tokens, titleid, title_tokens, keyid, key_tokens, descrid, descr_tokens, click, impression)
    elif line[0] == 'query':
    	# get query information
        queryid = line[1]
    	query_tokens = line[2]
    	print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (queryid, query_tokens, titleid, title_tokens, keyid, key_tokens, descrid, descr_tokens, click, impression)
    elif line[0] == 'key':
        # get key information
        keyid = line[1]
        key_tokens = line[2]
        print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (queryid, query_tokens, titleid, title_tokens, keyid, key_tokens, descrid, descr_tokens, click, impression)
    elif line[0] == 'descr':
        # get description infomation
        descrid = line[1]
        descr_tokens = line[2]
        print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (queryid, query_tokens, titleid, title_tokens, keyid, key_tokens, descrid, descr_tokens, click, impression)
    else:
        continue

