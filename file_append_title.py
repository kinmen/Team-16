#!/usr/bin/env python

"""
Input:
    titleid_tokensid.txt
Output:
    "'title' \t TitleID \t Title_Token"
"""


import sys

for line in sys.stdin:
    line = line.split('\t')
    # so that we can identify when its the titleid_tokensid.txt file
    print '%s\t%s\t%s' % ('title', line[0], line[1])
