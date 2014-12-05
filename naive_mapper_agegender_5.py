#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    qid, qtoken, titleid, ttoken, keyid, ktoken, descrid, dtoken, click, imp, uid, age, gender = line.split('\t')
    #make uid as key, for gender/age
    print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' %  (uid, age, gender, descrid, dtoken, qid, qtoken, titleid, ttoken, keyid, ktoken, click, imp, uid, age, gender)
