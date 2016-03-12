library(ggplot2); library(caret); library(Hmisc); library(arules)
set.seed(1337)

#import data
training <- read.csv("data/adult.data", header = FALSE, na.strings = "?")
testing <- read.csv("data/adult.test", header = FALSE, na.strings = "?")

colnames(training) <- c("age", "Workclass", "fnlwgt", "Education", "education-num", "Martial Status",
"Occupation", "Relationship", "Race", "Sex", "capital-gain", "capital-loss", "hours-per-week", "Country", "Target")

colnames(testing) <- c("age", "Workclass", "fnlwgt", "Education", "education-num", "Martial Status",
                       "Occupation", "Relationship", "Race", "Sex", "capital-gain", "capital-loss", "hours-per-week", "Country")

#https://cran.r-project.org/web/packages/arules/arules.pdf
cleanData <- function(data){
        ## remove attributes
        data[["fnlwgt"]] <- NULL
        data[["education-num"]] <- NULL

#         ## map metric attributes
#         data[[ "age"]] <- ordered(cut(data[[ "age"]], c(15,25,45,65,100)), labels = c("Young", "Middle-aged", "Senior", "Old"))
#         data[[ "hours-per-week"]] <- ordered(cut(data[[ "hours-per-week"]], c(0,25,40,60,168)), labels = c("Part-time", "Full-time", "Over-time", "Workaholic"))
#         data[[ "capital-gain"]] <- ordered(cut(data[[ "capital-gain"]],c(-Inf,0,median(data[[ "capital-gain"]][data[[ "capital-gain"]]>0]), Inf)), labels = c("None", "Low", "High"))
#         data[[ "capital-loss"]] <- ordered(cut(data[[ "capital-loss"]], c(-Inf,0, median(data[[ "capital-loss"]][data[[ "capital-loss"]]>0]), Inf)), labels = c("None", "Low", "High"))
        return(data)
}

training <- cleanData(training)
testing <- cleanData(testing)

# GBM TEST
model <- train(Target~., data = training, method = 'gbm')
preds <- predict(model, testing)
indx <- data.frame(Id=1:length(preds), preds)
colnames(indx) <- c("Id", "Target")
trim <- function (x) gsub("^\\s+|\\s+$", "", x)
indx$Target <- trim(indx$Target)
write.table(indx, "output/test1_gbm.out", row.names=FALSE, col.names = TRUE , quote=FALSE, sep = ",")


# GBM With CV TEST 
myControl <- trainControl(method="repeatedcv", number=5, repeats=1, verboseIter=TRUE)
model <- train(Target~., data = training, method = 'gbm', trControl=myControl)
preds <- predict(model, testing)
indx <- data.frame(Id=1:length(preds), preds)
colnames(indx) <- c("Id", "Target")
trim <- function (x) gsub("^\\s+|\\s+$", "", x)
indx$Target <- trim(indx$Target)
write.table(indx, "output/test2_gbmCV.out", row.names=FALSE, col.names = TRUE , quote=FALSE, sep = ",")

# rPART With CV TEST 
# myControl <- trainControl(method="repeatedcv", number=5, repeats=1, verboseIter=TRUE)
# model <- train(Target~., data = training, method = 'rpart')
# preds <- predict(model, testing)
# indx <- data.frame(Id=1:length(preds), preds)
# colnames(indx) <- c("Id", "Target")
# trim <- function (x) gsub("^\\s+|\\s+$", "", x)
# indx$Target <- trim(indx$Target)
# write.table(indx, "output/test3_rpartCV.out", row.names=FALSE, col.names = TRUE , quote=FALSE, sep = ",")

# RF With OOB TEST 
myControl <- trainControl(method="oob")
model <- train(Target~., data = training, method = 'rf', trControl=myControl)
preds <- predict(model, testing)
indx <- data.frame(Id=1:length(preds), preds)
colnames(indx) <- c("Id", "Target")
trim <- function (x) gsub("^\\s+|\\s+$", "", x)
indx$Target <- trim(indx$Target)
write.table(indx, "output/test4_rfCV.out", row.names=FALSE, col.names = TRUE , quote=FALSE, sep = ",")


# ADABAG With CV TEST 
model <- train(Target~., data = training, method = 'AdaBag')
preds <- predict(model, testing)
indx <- data.frame(Id=1:length(preds), preds)
colnames(indx) <- c("Id", "Target")
trim <- function (x) gsub("^\\s+|\\s+$", "", x)
indx$Target <- trim(indx$Target)
write.table(indx, "output/test5_adaCV.out", row.names=FALSE, col.names = TRUE , quote=FALSE, sep = ",")


# Tree ensambles With OOB TEST 
model <- train(Target~., data = training, method = 'nodeHarvest')
preds <- predict(model, testing)
indx <- data.frame(Id=1:length(preds), preds)
colnames(indx) <- c("Id", "Target")
trim <- function (x) gsub("^\\s+|\\s+$", "", x)
indx$Target <- trim(indx$Target)
write.table(indx, "output/test6_nodeHarvest.out", row.names=FALSE, col.names = TRUE , quote=FALSE, sep = ",")



