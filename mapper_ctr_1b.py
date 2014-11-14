#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    uid, click, imp, age = line.split('\t')
    print '%s\t%s\t%s\t%s' % (uid, click, imp, age)