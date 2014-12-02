#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    keyid, ktoken, descrid, dtoken, qid, qtoken, titleid, ttoken, click, imp = line.split('\t')
    print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' %  (keyid, ktoken, descrid, dtoken, qid, qtoken, titleid, ttoken, click, imp)
