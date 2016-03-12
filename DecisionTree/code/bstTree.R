library(ggplot2); library(caret); library(Hmisc); 
set.seed(1337)

#import data
training <- read.csv("data/adult.data", header = FALSE, na.strings = "?")
testing <- read.csv("data/adult.test", header = FALSE, na.strings = "?")

#Data description
# summary(training)
# describe(training)
# head(training)
#sapply(training, class)
#str(training)

# del row["native-country"]
# del row["fnlwgt"]
# del row["education-num"]
# del row["marital-status"]

# With no discretization Accuracy : 0.8628 BEST SO FAR!
#training$V1 <- cut(training$V1, 11)
#training$V13 <- cut(training$V13, 2)

#Without these variables Accuracy : 0.8359   
#With no discretization Accuracy : 0.8592 
#training$V11 <- cut(training$V11, 100)
#training$V12 <- cut(training$V12, 50)

#training <- training[,-c(3, 5:6, 14)]
#testing <- testing[,-c(3, 5:6, 14)]

# Split training data into train and test to do cross-validation
#inTrain <- createDataPartition(training$V15, p = 0.75, list = FALSE)
#train.train <- training[inTrain,]
#train.test <- training[-inTrain,]

# Accuracy 0.8539  without cv control
train.train <- training

#gives accuracy of 0.8553 
#myControl <- trainControl(method='cv', number=3, returnResamp='none')

# gives accuracy of 0.8554  
#myControl <- trainControl(method="repeatedcv", number=3, repeats=1, verboseIter=TRUE)
#myControl <- trainControl(method="cv", number=3)
#train the model
model <- train(V15 ~., data = train.train, method = 'bstTree')
#, trControl=myControl
#model <- train(V15 ~., data = train.train, method = 'gbm')

vari <- varImp(model)

#Make predictions
#rpartpred <- predict(model, train.test[,c(1:8)])
#rpartpred <- predict(model, train.test[,c(1:10)])

#Summarize results
#results <- confusionMatrix(rpartpred, train.test$V15)
#results

preds <- predict(model, testing)
indx <- data.frame(Id=1:length(preds), preds)
colnames(indx) <- c("Id", "Target")

# returns string w/o leading or trailing whitespace
trim <- function (x) gsub("^\\s+|\\s+$", "", x)

indx$Target <- trim(indx$Target)
write.table(indx, "output/task4_bstTree.out", row.names=FALSE, col.names = TRUE , quote=FALSE, sep = ",")
#importance(model)
#varImpPlot(model)

#Thoughts on further steps:
#Sort categorical variables in descending order
#Histograms of numerical variables to see what to normalize
#Check relative importance of variables
#Check distribution of categorical variables
#Find out if variables correlate
#Check Correlation between numerical variables and income class
#Correlation between education and years of education
#try boosted classification tree ada or plyr
