#!/usr/bin/env python

"""
Input:
    queryid_tokensid.txt
Output:
    "'query' \t QueryID \t Query_Token"
"""

import sys

for line in sys.stdin:
    line = line.split('\t')
    # so that we can identify when its the queryid_tokensid.txt file
    print '%s\t%s\t%s' % ('query', line[0], line[1])
