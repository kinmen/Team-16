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
### Aggregating the data
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

To begin, the files <code>titleid_tokensid.txt, queryid_tokensid.txt, descriptionsid_tokensid.txt, and purchasedkeywordid_tokensid.txt</code> were each run in MapReduce with their corresponding <code>file_append_*.py</code> file (e.g. <code>file_append_title.py</code> was run with <code>titleid_tokensid.txt</code> file and an identity reducer). This was done because otherwise, each of the token files were indistinguishable from one another.

Using the outputs from the above MapReduce along with the training data, we ran four MapReduce jobs to append the tokens to their subsequent ids. The Map-Reduce files are as follows:
<ul>
    <li><code>mapper_tok_1.py, reducer_tok_1.py</code></li>
    <li><code>mapper_tok_2.py, reducer_tok_2.py</code></li>
    <li><code>mapper_tok_3.py, reducer_tok_3.py</code></li>
    <li><code>mapper_tok_4.py, reducer_tok_4.py</code></li>
</ul>

After all MapReduce jobs are completed, a final map reduce is run by using the file <code>token_simi.py</code> as the mapper and an identity reducer. The final map reduce calculates similarity ratios for the number of matching tokens between:
<blockquote>
    <ul>
        <li>query to title</li>
        <li>query to description</li>
        <li>query to key</li>
        <li>query to title and description</li>
        <li>query to title and key</li>
        <li>query to description and key</li>
        <li>query to title, key, description</li>
    </ul>
</blockquote>



Model
-------------
### Naive Bayes


<code>naive_train_model.py</code> is run locally with its inputs as the output from the Aggregating Data MapReduce. This file calculates the probabilities:
<ul>
    <li><code>P(feature = value | click)</code></li>
    <li><code>P(feature = value | noclick)</code></li>
    <li><code>p(click)</code></li>
    <li><code>p(noclick)</code></li>
    <li><code>p(feature="UNK" | click)</code></li>
    <li><code>p(feature="UNK" | noclick)</code></li>
</ul>
where UNK refers to the unknown values for the feature.
The output of this is called <code>naive_probabilities.txt</code>



After building the dictionary of conditional probabilities, we go back to using MapReduce for prediction.
The following files are run to clean up validation data into the format that we want to finally do our predictions. They are run with <code>validation-20, titleid_tokensid.txt, queryid_tokensid.txt, descriptionsid_tokensid.txt, and purchasedkeywordid_tokensid.txt (appended as in Prediction By Similarity Index), userid_profile.txt</code>:

<ol>
    <li><code>naive_mapper_tok_1.py, naive_reducer_tok_1.py</code></li>
    <li><code>naive_mapper_tok_2.py, naive_reducer_tok_2.py</code></li>
    <li><code>naive_mapper_tok_3.py, naive_reducer_tok_3.py</code></li>
    <li><code>naive_mapper_tok_4.py, naive_reducer_tok_4.py</code></li>
    <li><code>naive_mapper_agegender_5.py, naive_reducer_agegender_5.py</code></li>
    <li><code>naive_token_simi.py, identity reducer</code></li>
</ol>

The final output of these MapReduce jobs is then run through the the final MapReduce. The following files are run with <code>naive_probabilities.txt</code> as a cache file. They will give our model's output predictions.
<ol>
    <li><code>naive_pred_mapper.py, identity reducer</code></li>
    <li><code>naive_pred_agender_mapper.py, identity reducer</code></li>
    <li><code>naive_pred_agqtkdsimi_mapper.py, identity reducer</code></li>
    <li><code>naive_pred_simi_mapper.py, identity reducer</code></li>
</ol>

1. Runs predictions using age, gender, and every similarity ratio
2. Runs predictions using only age and gender
3. Runs predictions using age, gender, and the query to key, description, title ratio
4. Runs predictions using only all of the similarity ratios

The outputs are downloaded and concatenated locally then run in R and the R script <code>auc.R</code> to get our AUC score.

*Note: A more detailed explanation of our project can be found in the <code>Final Report.pdf</code>
