#!/usr/bin/env python

import sys

for line in sys.stdin:

    # setting default parameters for sorting
    queryid = -1
    titleid = -1
    query_tokens = -1
    title_tokens = -1
    click = -1
    impression = -1

    # eliminate entrailing white spaces
    line = line.strip()

    # split for indexing
    line = line.split('\t')

    # for data
    if len(line) > 3:
        click = line[2]
        impression = line[3]
        queryid = line[9]
        titleid = line [11]
        print '%s\t%s\t%s\t%s\t%s\t%s' % (queryid, query_tokens, titleid, title_tokens, click, impression)
    elif line[0] == 'title':
        titleid = line[1]
        title_tokens = line[2]
        print '%s\t%s\t%s\t%s\t%s\t%s' % (queryid, query_tokens, titleid, title_tokens, click, impression)
    elif line[0] == 'query':
    	queryid = line[1]
    	query_tokens = line[2]
    	print '%s\t%s\t%s\t%s\t%s\t%s' % (queryid, query_tokens, titleid, title_tokens, click, impression)
    else:
        continue
#we need to append the query and title token files with an initial
#column that identifies which file it is because they are
#indistinguishable otherwise
