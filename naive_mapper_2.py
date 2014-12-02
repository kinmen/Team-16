#!/usr/bin/env python

import sys
import os.path
import math

sys.path.append(os.path.dirname(__file__))

feature_dict = { 5: "ad_id", 6: "advert_id" }
prob_dict = {}

# in order to access this file from s3 you need to add
# something like this to your job
# -cacheFile s3://stat157-uq85def/home/yannet/code/testing_nb/sample_prob.txt#sample_prob.txt
def read_probs():
    """ Reads the probability file and outputs a dictionary.
    The file has the form:
    advert_id 10040 0.00184842883549 0.00377969762419
    advert_id 1007 0.00184842883549 0.00107991360691
    ad_id 10110295 0.00109170305677 0.000898069151325
    ad_id 10110317 0.00109170305677 0.000898069151325
    ad_id UNK 0.00109170305677 0.000449034575662
    advert_id UNK 0.00184842883549 0.000539956803456
    Total Total 0.033185840708 0.966814159292
    """
    probs = {}
    # read prob file
    with open("sample_prob.txt", "r") as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip()
        feature, value, prob_click, prob_no_click = line.split('\t')
        key = "%s,%s" % (feature, value)
        probs[key] = (float(prob_click), float(prob_no_click))
    return probs
##
##def read_ages():
##    ages = {}
##    with open("user_age.txt", "r") as f:
##        lines = f.readlines()
##    for line in lines:
##        line = line.strip()
##        user, age = line.split('\t')
##        ages[user] = age
##    return ages
##

def get_prob_from_dict(feature, value):
    """ Given feature and value returns probs.
    Returns
    (Prob(feature = value | click), Prob(feature = value | no click))
    if value is not in the dictionary
    (Prob(feature = "UNK" | click), Prob(feature = "UNK" | no click))
    """
    key = "%s,%s" % (feature, value)
    if key in prob_dict:
        return prob_dict[key]
    key = "%s,%s" % (feature, "UNK")
    if key in prob_dict:
        return prob_dict[key]
    return None

def normpdf(x, mean, var):
    pi = 3.1415926
    denom = (2*pi*var)**.5
    num = math.exp(-(float(x)-float(mean))**2/(2*var))
    return num/denom


def calc_prob_for_simi(simi):
    clickmean, clickvar = get_prob_from_dict('simi', 'click')
    nclickmean, nclickvar = get_prob_from_dict('simi', 'noclick')
    clickprob = normpdf(simi, clickmean, clickvar)
    noclickprob = normpdf(simi, nclickmean, nclickvar)
    return clickprob,noclickprob

prob_dict = read_probs()
##age_dict = read_ages()

# Reading validation / test lines
# Input is format of "user age clicks impressions typeofdata"
for line in sys.stdin:
    line = line.strip()
    fields = line.split('\t')
    ### complete your code here
    ###
    user, age, gender, simi, trueclicks, impressions, typeofdata = fields
    ###
    trueclicks = int(float(trueclicks))
    impressions = int(float(impressions))
    probs_age = get_prob_from_dict("age", age)
    probs_gender = get_prob_from_dict("gender", gender)
    ###
    probs_simi = calc_prob_for_simi(simi)
    ###
    total = get_prob_from_dict("Total", "Total")
    probs = []
    probs[0] = float(probs_age[0]*probs_gender[0]*probs_simi[0])
    probs[1] = float(probs_age[1]*probs_gender[1]*probs_simi[1])
    pclickgivendata = float(probs[0]*total[0])/((probs[0]*total[0])+(probs[1]*total[1]))
    click = 0
    if pclickgivendata > 0.5:
        click = 1
    for i in xrange(trueclicks):
        print "%s\t%s\t%s\t%s" % (pclickgivendata, click, typeofdata, 1)
    for j in xrange(impressions - trueclicks):
        print "%s\t%s\t%s\t%s" % (pclickgivendata, click, typeofdata, 0)
