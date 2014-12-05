Team-16 Project
=============

For our project, we are looking at the [2012 kaggle competition](https://www.kddcup2012.org/c/kddcup2012-track2) where we are trying to predict click-through-rates (CTRs) based on different features. We use a Naive Bayes Model to predict our CTRs.


Features
-------------
## Aggregating the data
#### Prediction Based on Age


We aggregate our data using MapReduce, which is run on the Amazon Web Service System. In our first step, we need to place <code>userid_profile.txt</code> with our training data so that everything can be called at once. So that things will be easier to call when introducing our inputs, <code>userid_profile.txt</code>will be renamed<code>part-uid</code> and placed together in the training data folder.

MapReduce is then run with <code>mapper_age_1.py</code> and <code>reducer_age_1.py</code> with the inputs coming from the "training-60" folder including our userid_profile data. The output data is in the form:<br><br>
    <code style='text-align:center;'>'age \t click \t impression'</code>.

The results of the MapReduce is then used as inputs for the second MapReduce, using the mapper and reducer <code>mapper_age_2.py</code> and <code>reducer_age_2.py</code>. This outputs data in the form:<br><br>
    <code>'feature value \t feature name \t clicks \t impressions'</code>.


#### Prediction Based on Gender

This data is done in a similar manner to the aggregation of data based on age. using the same initial input file as our MapReduce for Age, we run <code>mapper_gender_1.py</code> and <code>reducer_gender_1.py</code>. The output data is in the form: <br><br>
    <code>'age \t click \t impression'</code>.

The results of this MapReduce, like with Age, is then used as inputs for the second MapReduce using the mapper and reducer <code>mapper_gender_2,py</code> and reducer_gender_2.py</code>. This outputs data in the form:<br><br>
    <code>'feature value \t feature name \t clicks \t impression'</code>

#### Prediction By Similarity Index

We use a similarity ratio to measure the similarity between ids through their token



Model
-------------
## Naive Bayes

After getting our output from the Aggregating Data MapReduce, <code>naive.py</code> is run locally. This file calculates the probabilities:
<ul>
    <li><code>P(feature = value | click)</code></li>
    <li><code>P(feature = value | noclick)</code></li>
    <li><code>p(click)</code></li>
    <li><code>p(noclick)</code></li>
    <li><code>p(feature="UNK" | click)</code></li>
    <li><code>p(feature="UNK" | noclick)</code></li>
</ul>
where UNK refers to the unknown values for the feature.

After building the dictionary of conditional probabilities, we go back to using MapReduce for prediction. <code>naive_mapper_1.py</code> and <code>naive_reducer_1.py</code> are run to clean up validation data into the format we want for our second mapreduce job for prediction. It combines the userid, age, clicks, and impressions for each instance in the validation data and returns an output in the form of: <code>'uid \t click \t impression \t age'</code>.

