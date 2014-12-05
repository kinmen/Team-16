#!/usr/bin/env python
"""
Input:
    purchasedkeywordid_tokensid.txt
Output:
    "'key' \t KeyID \t Key_Token"
"""


import sys

for line in sys.stdin:
    line = line.split('\t')
    # so that we can identify when its the purchasedkeywordid_tokensid.txt file
    print '%s\t%s\t%s' % ('key', line[0], line[1])
