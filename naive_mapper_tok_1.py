#!/usr/bin/env python

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
    age = 'z'
    gender = 'z'
    uid = 'z'
    

    # eliminate entrailing white spaces
    line = line.strip()

    # split for indexing
    line = line.split('\t')

    # for data
    if len(line) > 3:
        click = line[2]
        impression = line[3]
        queryid = line[9]
        keyid = line[10]
        titleid = line [11]
        descrid = line[12]
        uid = line[-1]
        print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (queryid, query_tokens, titleid, title_tokens, keyid, key_tokens, descrid, descr_tokens, click, impression , uid, age, gender)
    elif line[0] == 'title':
        titleid = line[1]
        title_tokens = line[2]
        print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (queryid, query_tokens, titleid, title_tokens, keyid, key_tokens, descrid, descr_tokens, click, impression , uid, age, gender)
    elif line[0] == 'query':
    	queryid = line[1]
    	query_tokens = line[2]
    	print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (queryid, query_tokens, titleid, title_tokens, keyid, key_tokens, descrid, descr_tokens, click, impression , uid, age, gender)
    elif line[0] == 'key':
        keyid = line[1]
        key_tokens = line[2]
        print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (queryid, query_tokens, titleid, title_tokens, keyid, key_tokens, descrid, descr_tokens, click, impression , uid, age, gender)
    elif line[0] == 'descr':
        descrid = line[1]
        descr_tokens = line[2]
        print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (queryid, query_tokens, titleid, title_tokens, keyid, key_tokens, descrid, descr_tokens, click, impression , uid, age, gender)
    else:
        if len(line) == 3:
            uid = line[0]
            gender = line[1]
            age = line[2]
            print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (queryid, query_tokens, titleid, title_tokens, keyid, key_tokens, descrid, descr_tokens, click, impression , uid, age, gender)
        continue
#we need to append the query and title token files with an initial
#column that identifies which file it is because they are
#indistinguishable otherwise
