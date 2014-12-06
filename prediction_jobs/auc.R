
auc <- read.csv("auc_data.csv", header=FALSE) 
names(auc) <- c("prob", "response")
#install.packages("pROC")
library("pROC")
auc(auc$response, auc$prob)

## Area under the curve: 0.657

