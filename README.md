Team-16 Project
=============


Introduction
-------------
The objective of this project is to predict the empirical CTR through statistical models with the categorical features of the given data.

The data we are provided with is the Track 2 data of the [KDD cup 2012](https://www.kddcup2012.org/c/kddcup2012-track2), which includes 12 categorical features in the main data file, and five additional data files: query_tokensid.txt, purchasekeywordid_tokensid.txt, titleid_tokensid.txt, description_tokensid.txt, and userid_profile.txt.

The main data was divided into three sections: training, testing, and validation. The training portion of the data is used to train the statistical model, while the testing data is used to test the model. The validation set then acts to validate the model, where the model attempts to predict data that is completely unknown to us.

The categorical features we chose to employ were gender, age, and the token similarity for QueryId, TitleId, Keyword, and Description. The statistical model we decided to utilize for this project was the Naive-Bayes classifier.


Features
-------------
## Aggregating the data
#### Prediction Based on Age


We aggregate our data using MapReduce, which is run on the Amazon Web Service System. Since age is in a separate file from the instance file, our first step is to join these files together. To do this, we need to run a MapReduce sorted by the key <code>userid</code>. To begin our process, we need to place <code>userid_profile.txt</code> with our training data so that everything can be called at once. So that things will be easier to call when introducing our inputs, <code>userid_profile.txt</code>will be renamed<code>part-uid</code> and placed together in the training data folder.

MapReduce is then run with <code>mapper_age_1.py</code> and <code>reducer_age_1.py</code> with the inputs coming from the "training-60" folder including our userid_profile data. The output data is in the form:
    <blockquote>
        <code>'age \t click \t impression'</code>.
    </blockquote>

The results of the MapReduce is then used as inputs for the second MapReduce, using the mapper and reducer <code>mapper_age_2.py</code> and <code>reducer_age_2.py</code>. This outputs data in the form:
    <blockquote>
        <code>'feature value \t feature name \t clicks \t impressions'</code>.
    </blockquote>


#### Prediction Based on Gender

Like with age, gender is also in a separate file from the instances file. The process to aggregate this data is done in a similar manner to the aggregation of data based on age. Using the same initial input file as our MapReduce for age, we run <code>mapper_gender_1.py</code> and <code>reducer_gender_1.py</code>. The output data is in the form:
    <blockquote>
        <code>'gender \t click \t impression'</code>.
    </blockquote>

The results of this MapReduce, like with Age, is then used as inputs for the second MapReduce using the mapper and reducer <code>mapper_gender_2,py</code> and reducer_gender_2.py</code>. This outputs data in the form:
    <blockquote>
        <code>'feature value \t feature name \t clicks \t impression'</code>
    </blockquote>

#### Prediction By Similarity Index

<!--We use a similarity ratio to measure the similarity between ids through their token-->



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

