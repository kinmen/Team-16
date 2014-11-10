import sys

for line in sys.stdin:

    # remove entrailing white spaces
    line = line.strip()

    # assign variables
    uid, age, click, impression  = line.split('\t')

    # print stdout
    print '%s\t%s\t%s' % (age, click, impression)