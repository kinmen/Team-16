Team-16 Project Proposal
=============

Prediction Based on Age
-------------
### MapReduce
#### Training

MapReduce is run on the Amazon Web Service System. In our first step, we need to place <code>userid_profile.txt</code> with our training data. For ease of access when we call our data, we will rename it <code>part-0</code> in the appropriate folder.

MapReduce is then run with <code>mapper_ctr_1.py</code> and <code>reducer_ctr_1.py</code> with the inputs coming from the training-60 folder and our userid_profile data. The output data is in the form <code>'age \t click \t impression'</code>.

The results of the MapReduce is then used as inputs for the second MapReduce, using the mapper and reducer <code>mapper_ctr_2.py</code> and <code>reducer_ctr_2.py</code>. This outputs data in the form <code>'feature value \t feature name \t clicks \t impressions'</code>.