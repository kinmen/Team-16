#!/usr/bin/env python

import sys


current_queryid = None
current_qtoken = None
current_click = 0
current_impression = 0
title_dic = dict()


for line in sys.stdin:

    # eliminate entrailing white spaces
    line = line.strip()

    # split for indexing
    queryid, query_token, titleid, title_token, click, impression = line.split('\t')

    # if current query
    if current_queryid == queryid:
        # cumulate clicks and impressions

        if click != "-1" and impression != "-1":
            current_click += float(int(click))
            current_impression += float(int(impression))

        # cumulate query tokens
        if query_token != "-1":
            current_qtoken = query_token

        # titleid and tokens are all scrambled
        if titleid != "-1" and title_token != "-1":
            title_dic[titleid] = title_dic.get(titleid, "") + title_token


    else:
        # print output

        if current_queryid:
            current_titleid = title_dic.keys()
            # print such that each titleid gets an output
            # this way, we can run a second mapreduce to
            # cumulate the titleid tokens
            if len(current_titleid) > 0:
                for i in range(len(current_titleid)):

                    print '%s\t%s\t%s\t%s\t%s\t%s' % (current_titleid[i], title_dic.get(current_titleid[i]), current_queryid, current_qtoken, current_click, current_impression)
                    # so that we don't recount, set to zero
                    # for the rest of the iterations
                    current_click = 0
                    current_impression = 0

            else:
                print '%s\t%s\t%s\t%s\t%s\t%s' % (current_titleid, [], current_queryid, current_qtoken, current_click, current_impression)


        # reset parameters
        if click != "-1" and impression != "-1":
            current_click = float(int(click))
            current_impression = float(int(impression))
        else:
            current_click = 0
            current_impression = 0
        if current_qtoken != "-1":
            current_qtoken = query_token
        else:
            current_qtoken = ""
        title_dic = dict()
        current_queryid = queryid

        current_titleid = titleid


# print last line