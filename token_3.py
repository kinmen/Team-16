#!/usr/bin/env python

import sys

for line in sys.stdin:

    query_token = line[3]
    title_token = line[1]
    
    qtokens = query_token.strip('|')
    ttoken = title_token.strip('|')

    ### This loops through the ttok with the qtok to find and return
    ### any matching values as a list
    matched = list(set(qtokens).intersection(ttokens))

    ### len(qtok) tell us how many tokens are in the query
    ratio = float(len(matched))/float(len(qtokens))

    print '%s\t%s\t%s\t%s' % (ratio, 'simi', line[4], line[5])
    #prints ratio, 'simil', clicks, impressions
