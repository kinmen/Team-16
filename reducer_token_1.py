#!/usr/bin/env python

import sys


current_queryid = None
current_qtokens = list()
current_click = 0
current_impression = 0
title_dic = dict()


for line in sys.stdin:

    # eliminate entrailing white spaces
    line = line.strip()

    # split for indexing
    queryid, query_tokens, titleid, title_tokens, click, impression = line.split('\t')

    # if current query
    if current_queryid == queryid:
        # cumulate clicks and impressions
        if click != "-1" and impression != "-1":
            current_click += float(int(click))
            current_impression += float(int(impression))

        # cumulate query tokens
        if query_tokens != "-1":
            current_qtokens = query_tokens + current_qtokens
        # titleid and tokens are all scrambled
        if titleid != "-1" and title_tokens != "-1":
            title_dic[titleid] = title_dic.get(titleid, []) + eval(title_tokens)


    else:
        # print output
        if current_queryid:

            current_titleid = title_dic.keys()
            # print such that each titleid gets an output
            # this way, we can run a second mapreduce to
            # cumulate the titleid tokens
            for i in range(len(current_titleid)):

                print '%s\t%s\t%s\t%s\t%s\t%s' % (current_titleid, title_dic.get(current_titleid[i]), current_queryid, current_qtokens, current_click, current_impression)
                # so that we don't recount, set to zero
                # for the rest of the iterations
                current_click = 0
                current_impression = 0
        # reset parameters
        if click != "-1" and impression != "-1":
            current_click = float(int(click))
            current_impression = float(int(impression))
        else:
            current_click = 0
            current_impression = 0
        current_queryid = queryid
        current_titleid = "-1"

# print last line
if current_queryid:
    current_titleid = title_dic.keys()
    # print such that each titleid gets an output
    # this way, we can run a second mapreduce to
    # cumulate the titleid tokens
    for i in range(len(current_titleid)):
        print '%s\t%s\t%s\t%s\t%s\t%s' % (current_titleid, title_dic.get(current_titleid[i]), current_queryid, current_qtokens, current_click, current_impression)
        # so that we don't recount, set to zero
        # for the rest of the iterations
        current_click = 0
        current_impression = 0

