#!/usr/bin/env python

"""
Input:
    Output of mapper_tok_2.py and reducer_tok_2.py
Output:
    'KeyID \t Key_Tokens \t DescriptionID \t Description_Tokens \t QueryID \t Query_Tokens \t TitleID \t Title_Tokens \t Clicks \t Impressions'
"""


import sys

for line in sys.stdin:
    line = line.strip()
    keyid, ktoken, descrid, dtoken, qid, qtoken, titleid, ttoken, click, imp = line.split('\t')
    print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' %  (keyid, ktoken, descrid, dtoken, qid, qtoken, titleid, ttoken, click, imp)
