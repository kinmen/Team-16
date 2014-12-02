#!/usr/bin/env python

# This mapper is pretty much pointless

import sys

for line in sys.stdin:
    line = line.strip()
    titleid, ttoken, keyid, ktoken, descrid, dtoken, qid, qtoken, click, imp = line.split('\t')
    print '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (titleid, ttoken, keyid, ktoken, descrid, dtoken, qid, qtoken, click, imp)
