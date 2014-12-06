#!/usr/bin/env python

"""
Input:
    Output of naive_mapper_tok_2.py and naive_reducer_tok_2.py
Output:
    'KeyID \t Key_Tokens \t DescriptionID \t Description_Tokens \t QueryID \t Query_Tokens \t TitleID \t Title_Tokens \t Clicks \t Impressions \t UserID \t Age \t Gender'
"""

import sys

for line in sys.stdin:
    line = line.strip()
    keyid, ktoken, descrid, dtoken, qid, qtoken, titleid, ttoken, click, imp, uid, age, gender = line.split('\t')
    print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' %  (keyid, ktoken, descrid, dtoken, qid, qtoken, titleid, ttoken, click, imp, uid, age, gender)
