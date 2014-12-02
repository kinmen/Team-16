#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.split('\t')
    print '%s\t%s\t%s' % ('query', line[0], line[1])
