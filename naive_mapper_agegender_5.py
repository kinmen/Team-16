#!/usr/bin/env python

"""
Input:
    Output of naive_mapper_tok_4.py and naive_reducer_tok_4.py
Output:
    'UserID \t Age \t Gender \t DescriptionID \t Description_Tokens \t QueryID \t Query_Tokens \t TitleID \t Title_Tokens \t KeyID \t Key_Tokens \t Clicks \t Impressions'
"""

import sys

for line in sys.stdin:
    line = line.strip()
    qid, qtoken, titleid, ttoken, keyid, ktoken, descrid, dtoken, click, imp, uid, age, gender = line.split('\t')
    #make uid as key, for gender/age
    print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' %  (uid, age, gender, descrid, dtoken, qid, qtoken, titleid, ttoken, keyid, ktoken, click, imp)
