#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    descrid, dtoken, qid, qtoken, titleid, ttoken, keyid, ktoken, click, imp = line.split('\t')
    print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' %  (descrid, dtoken, qid, qtoken, titleid, ttoken, keyid, ktoken, click, imp)
