library(ggplot2); library(caret); library(Hmisc); 
set.seed(1337)

#import data
training <- read.csv("data/adult.data", header = FALSE, na.strings = "?")

#Data description
summary(training)
describe(training)
head(training)
sapply(training, class)
str(training)

# Split training data into train and test to do cross-validation
inTrain <- createDataPartition(training$V15, p = 0.75, list = FALSE)
train.train <- training[inTrain,]
train.test <- training[-inTrain,]

#train the model
model <- train(V15 ~., data = train.train, method = "rpart")
vari <- varImp(model)
#Make predictions
rpartpred <- predict(model, train.test[,c(1:14)])

#Summarize results
results <- confusionMatrix(rpartpred, train.test$V15)

#Thoughts on further steps:
#Sort categorical variables in descending order
#Histograms of numerical variables to see what to normalize
#Check relative importance of variables
#Check distribution of categorical variables
#Find out if variables correlate
#Check Correlation between numerical variables and income class
#Correlation between education and years of education
#try boosted classification tree ada or plyr

# Select a parameter setting
selectedIndices <- model$pred$mtry == 2
# Plot:
plot.roc(model$pred$obs[selectedIndices],
         model$pred$M[selectedIndices])