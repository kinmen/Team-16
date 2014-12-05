#!/usr/bin/env python

"""
Input:
    Output of mapper_tok_1.py and reducer_tok_1.py
Output:
    'TitleID \t Title_Tokens \t KeyID \t Key_Tokens \t DescriptionID \t Description_Tokens \t QueryID \t Query_Tokens \t Clicks \t Impressions'
"""


import sys

for line in sys.stdin:
    line = line.strip()
    titleid, ttoken, keyid, ktoken, descrid, dtoken, qid, qtoken, click, imp = line.split('\t')
    print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (titleid, ttoken, keyid, ktoken, descrid, dtoken, qid, qtoken, click, imp)
