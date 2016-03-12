library(ggplot2); library(caret); library(Hmisc); library(arules); library(corrplot); library(AppliedPredictiveModeling);  library(rattle)
set.seed(1337)

#import data
training <- read.csv("data/adult.data", header = FALSE, na.strings = "?")

colnames(training) <- c("age", "Workclass", "fnlwgt", "Education", "educationNum", "MartialStatus",
                        "Occupation", "Relationship", "Race", "Sex", "capitalGain", "capitalLoss", "hoursPERweek", "Country", "Target")


#Data description
summary(training)
#describe(training)
#head(training)
#sapply(training, class)
#str(training)

nzv <- nearZeroVar(training, saveMetrics= TRUE)
nzv

descrCor <- cor(training[,c("age", "fnlwgt", "educationNum", "capitalGain", "capitalLoss", "hoursPERweek")])
highlyCorDescr <- findCorrelation(descrCor, cutoff = .75)
highlyCorDescr

corrplot(descrCor, method = "circle")


model <- train(Target~., data = training, method = 'rpart')
vari <- varImp(model)
plot(vari, top = 10)
fancyRpartPlot(model$finalModel)

training.sub <- training
training.sub <- subset(training.sub, select = -c(Country, fnlwgt, educationNum, MartialStatus))
model <- train(Target ~., data = training.sub, method = 'rpart')
vari <- varImp(model)
fancyRpartPlot(model$finalModel)
plot(vari, top = 10)

transparentTheme(trans = .4)
featurePlot(x = training[, 4:5],
            y = training$Target,
            plot = "pairs",
            ## Add a key at the top
            auto.key = list(columns = 3))

hist(training$`education-num`)
education = factor(training$Education)
dummies = model.matrix(~education)
head(dummies)
#is.factor(training$educationNum)
educationNum = factor(training$educationNum)
#Target = factor(training$Target)
newEDU <- cbind(educationNum, dummies)
#newEDU <- cbind(newEDU, Target)

model <- train(educationNum~., data = newEDU, method = 'lm')
summary(model)

plot(training$MartialStatus)
