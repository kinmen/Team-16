Team-16 Project Proposal
=============

Prediction Based on Age
-------------
### MapReduce

MapReduce is run on the Amazon Web Service System. MapReduce is run with <code> mapper_ctr_1.py </code> as the mapper and <code> org.apache.hadoop.mapred.lib.IdentityReducer </code> as the identity reducer. The inputs are <code>userid_profile.txt</code> and all the parts of the training-60 dataset. The results are downloaded and concatenated through running the following command in the terminal:
<code>sh -e concatenate_script.txt</code>

The second MapReduce is run with <code> mapper_ctr_1b.py </code> and <code> reducer_ctr_1.py </code> with the output of the prior as the input (i.e. <code> mapper1b.txt </code>). This outputs data in the form 'age \t click \t impression'.

The results of the second MapReduce are then used as inputs for the third MapReduce, using the mapper and reducer <code> mapper_ctr_2.py </code> and <code> reducer_ctr_2.py </code>. This outputs data in the form 'feature name \t feature value \t clicks \t impressions'.