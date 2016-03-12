library(ggplot2); library(caret); library(Hmisc); library(pROC);
set.seed(1337)

#import data
training <- read.csv("data/adult.data", header = FALSE, na.strings = "?")

#Data description
# summary(training)
# describe(training)
# head(training)
sapply(training, class)
str(training)

# del row["native-country"]
# del row["fnlwgt"]
# del row["education-num"]
# del row["marital-status"]

training$V1 <- cut(training$V1, 11)
training$V13 <- cut(training$V13, 2)
training$V11 <- cut(training$V11, 50)
training$V12 <- cut(training$V12, 50)

training <- training[,-c(3, 5:6, 14)]

# Split training data into train and test to do cross-validation
training <- training[sample(nrow(training)),]
split <- floor(nrow(training)/3)
ensembleData <- training[0:split,]
blenderData <- training[(split+1):(split*2),]
testingData <- training[(split*2+1):nrow(training),]

labelName <- 'V15'
predictors <- names(ensembleData)[names(ensembleData) != labelName]
myControl <- trainControl(method='cv', number=3, returnResamp='none')

test_model <- train(blenderData[,predictors], blenderData[,labelName], method='gbm', trControl=myControl)
preds <- predict(object=test_model, testingData[,predictors])
# auc <- roc(testingData$15, preds)
#print(auc$auc) 

#Summarize results
test_results <- confusionMatrix(preds, testingData$V15)
print(test_results)

model_gbm <- train(ensembleData[,predictors], ensembleData[,labelName], method='gbm', trControl=myControl)

model_rpart <- train(ensembleData[,predictors], ensembleData[,labelName], method='rpart', trControl=myControl)

model_treebag <- train(ensembleData[,predictors], ensembleData[,labelName], method='treebag', trControl=myControl)

blenderData$gbm_PROB <- predict(object=model_gbm, blenderData[,predictors])
blenderData$rf_PROB <- predict(object=model_rpart, blenderData[,predictors])
blenderData$treebag_PROB <- predict(object=model_treebag, blenderData[,predictors])

testingData$gbm_PROB <- predict(object=model_gbm, testingData[,predictors])
testingData$rf_PROB <- predict(object=model_rpart, testingData[,predictors])
testingData$treebag_PROB <- predict(object=model_treebag, testingData[,predictors])

predictors <- names(blenderData)[names(blenderData) != labelName]
final_blender_model <- train(blenderData[,predictors], blenderData[,labelName], method='gbm', trControl=myControl)

preds <- predict(object=final_blender_model, testingData[,predictors])

#Summarize results
results <- confusionMatrix(preds, testingData$V15)
print(results)


write.table(mydata, "c:/mydata.txt", sep="\t")
