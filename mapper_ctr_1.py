import sys


for line in sys.stdin:

    # setting default parameters for sorting
    uid = -1
    age = -1
    click = -1
    impression = -1

    # eliminate entrailing white spaces
    line = line.strip()

    # split for indexing
    line = line.split('\t')

    # if smallinstances.txt
    if len(line) > 3:
        click = line[0]
        impression = line[1]
        uid = line[-1]
        print '%s\t%s\t%s\t%s' % (uid, click, impression, age)
    # else smalluser.txt
    else:
        uid = line[0]
        age = line[-1]
        print '%s\t%s\t%s\t%s' % (uid, click, impression, age)