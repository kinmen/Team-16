#!/usr/bin/env python
"""
Input:
    descriptionid_tokensid.txt
Output:
    "'descr' \t DescriptionID \t Description_Token"
"""

import sys

for line in sys.stdin:
    line = line.split('\t')
    # so that we can identify when its the descriptionid_tokensid.txt file
    print '%s\t%s\t%s' % ('descr', line[0], line[1])
