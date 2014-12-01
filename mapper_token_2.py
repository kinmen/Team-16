#!/usr/bin/env python

# This mapper is pretty much pointless

import sys

for line in sys.stdin:
    line = line.strip()
    tid, ttoken, qid, qtokens, click, impression = line.split('\t')
    print '%s\t%s\t%s\t%s\t%s\t%s' % (tid, ttoken, qid, qtokens, click, impression)