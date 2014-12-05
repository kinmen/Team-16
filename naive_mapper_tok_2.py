#!/usr/bin/env python


import sys

for line in sys.stdin:
    line = line.strip()
    titleid, ttoken, keyid, ktoken, descrid, dtoken, qid, qtoken, click, imp, uid, age, gender = line.split('\t')
    print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (titleid, ttoken, keyid, ktoken, descrid, dtoken, qid, qtoken, click, imp, uid, age, gender)
