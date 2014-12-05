#!/usr/bin/env python

"""
Input:
    Output of mapper_tok_3.py and reducer_tok_3.py
Output:
    'DescriptionID \t Description_Tokens \t QueryID \t Query_Tokens \t TitleID \t Title_Tokens \t KeyID \t Key_Tokens \t Clicks \t Impressions'
"""

import sys

for line in sys.stdin:
    line = line.strip()
    descrid, dtoken, qid, qtoken, titleid, ttoken, keyid, ktoken, click, imp = line.split('\t')
    print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' %  (descrid, dtoken, qid, qtoken, titleid, ttoken, keyid, ktoken, click, imp)
