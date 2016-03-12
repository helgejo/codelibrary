library(ggplot2); library(caret); library(Hmisc); library(pROC);
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

training$V1 <- cut(training$V1, 11)
training$V13 <- cut(training$V13, 2)
training$V11 <- cut(training$V11, seq(0,100000, by = 100))
training$V12 <- cut(training$V12, seq(0,4400, by = 50))

training <- training[,-c(3, 5:6, 14)]

testing$V1 <- cut(testing$V1, 11)
testing$V13 <- cut(testing$V13, 2)
testing$V11 <- cut(testing$V11, seq(0,100000, by = 100))
testing$V12 <- cut(testing$V12, seq(0,4400, by = 50))

testing <- testing[,-c(3, 5:6, 14)]

# Split training data into train and test to do cross-validation
training <- training[sample(nrow(training)),]
split <- floor(nrow(training)/2)
ensembleData <- training[0:split,]
blenderData <- training[(split+1):nrow(training),]
#testingData <- training[(split*2+1):nrow(training),]

labelName <- 'V15'
predictors <- names(ensembleData)[names(ensembleData) != labelName]
myControl <- trainControl(method='cv', number=3, returnResamp='none')

#test_model <- train(blenderData[,predictors], blenderData[,labelName], method='gbm', trControl=myControl)
#preds <- predict(object=test_model, testingData[,predictors])
# auc <- roc(testingData$15, preds)
#print(auc$auc) 

#Summarize results
#test_results <- confusionMatrix(preds, testingData$V15)
#print(test_results)

model_gbm <- train(ensembleData[,predictors], ensembleData[,labelName], method='gbm', trControl=myControl)
model_rpart <- train(ensembleData[,predictors], ensembleData[,labelName], method='rpart', trControl=myControl)
model_treebag <- train(ensembleData[,predictors], ensembleData[,labelName], method='treebag', trControl=myControl)

blenderData$gbm_PROB <- predict(object=model_gbm, blenderData[,predictors])
blenderData$rf_PROB <- predict(object=model_rpart, blenderData[,predictors])
blenderData$treebag_PROB <- predict(object=model_treebag, blenderData[,predictors])

testing$gbm_PROB <- predict(object=model_gbm, testing[,predictors])
testing$rf_PROB <- predict(object=model_rpart, testing[,predictors])
testing$treebag_PROB <- predict(object=model_treebag, testing[,predictors])

predictors <- names(blenderData)[names(blenderData) != labelName]
final_blender_model <- train(blenderData[,predictors], blenderData[,labelName], method='gbm', trControl=myControl)

#preds <- predict(object=final_blender_model, testingData[,predictors])

#Summarize results
#results <- confusionMatrix(preds, testingData$V15)
#print(results)


#predictors <- predictors[1:10]
preds <- predict(final_blender_model, testing[,predictors])

write.table(preds, "output/task3.out", row.names=FALSE, col.names=FALSE, quote=FALSE)
