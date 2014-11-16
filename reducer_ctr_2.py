import sys

current_click = 0
current_impression = 0
current_age = None

for line in sys.stdin:

    # remove entrailing white spaces
    line = line.strip()

    # assign variables
    age, click, impression = line.split('\t')

    # filter out bad data
    try:
        click = float(click)
        impression = float(impression)
    except ValueError:
        pass

    # cumulate data based on age
    if current_age == age:
        current_click += click
        current_impression += impression

    else:
        # print stdout
        if current_age:
            print '%s\t%s\t%f\t%f' % ('age', current_age, current_click, current_impression)
        # reset parameters
        current_click = click
        current_impression = impression
        current_age = age

# print last line
if current_age:
    print '%s\t%s\t%f\t%f' % ('age', current_age, current_click,current_impression)