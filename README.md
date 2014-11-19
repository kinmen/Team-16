Team-16 Project Proposal
=============

Model: Naive Bayes
-------------
## Prediction Based on Age
#### Aggregating the data

We aggregate our data using MapReduce, which is run on the Amazon Web Service System. In our first step, we need to place <code>userid_profile.txt</code> with our training data so that everything can be called at once. So that things will be easier to call, <code>userid_profile.txt</code>will be renamed<code>part-userid</code> in the training data folder.

MapReduce is then run with <code>mapper_ctr_1.py</code> and <code>reducer_ctr_1.py</code> with the inputs coming from the training-60 folder and our userid_profile data. The output data is in the form <code>'age \t click \t impression'</code>.

The results of the MapReduce is then used as inputs for the second MapReduce, using the mapper and reducer <code>mapper_ctr_2.py</code> and <code>reducer_ctr_2.py</code>. This outputs data in the form <code>'feature value \t feature name \t clicks \t impressions'</code>. The output is downloaded then concatenated locally.

The outputs for both MapReduce jobs are located in the Outputs directory in this repository.



#### Naive Bayes

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
