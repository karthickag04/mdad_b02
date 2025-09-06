#Step 1: Load Packages & Dataset

# Install if needed
# install.packages(c("caret", "ggplot2", "dplyr"))

library(caret)
library(ggplot2)
library(dplyr)

# Built-in dataset
data(iris)
head(iris)



# Step 2: Data Exploration with dplyr

# Check structure
glimpse(iris)

# Basic stats by species
iris %>%
  group_by(Species) %>%
  summarise(
    Avg_Sepal_Length = mean(Sepal.Length),
    Avg_Sepal_Width  = mean(Sepal.Width),
    Avg_Petal_Length = mean(Petal.Length),
    Avg_Petal_Width  = mean(Petal.Width)
  )



# Step 3: Visualization with ggplot2

# Scatterplot Petal.Length vs Petal.Width
ggplot(iris, aes(x=Petal.Length, y=Petal.Width, color=Species)) +
  geom_point(size=3) +
  labs(title="Iris Petal Dimensions", x="Petal Length", y="Petal Width") +
  theme_minimal()

# Boxplot Sepal.Length by Species
ggplot(iris, aes(x=Species, y=Sepal.Length, fill=Species)) +
  geom_boxplot() +
  labs(title="Sepal Length Distribution by Species") +
  theme_minimal()


# Step 4: Data Splitting with caret

set.seed(123)  # reproducibility
trainIndex <- createDataPartition(iris$Species, p=0.7, list=FALSE)

# 70% → training when you use "p=0.7"
# 30% → testing

trainData <- iris[trainIndex, ]
testData  <- iris[-trainIndex, ]


# Step 5: Preprocessing

preProc <- preProcess(trainData[, -5], method=c("center", "scale"))

# method = c("center", "scale")	--  StandardScaler()	Standardization (Z-score)
# method = "range"	-  MinMaxScaler()	Min-max normalization

trainTransformed <- predict(preProc, trainData[, -5])
testTransformed  <- predict(preProc, testData[, -5])


# Step 6: Train Model with caret

ctrl <- trainControl(method="cv", number=5)  # 5-fold CV

model_knn <- train(
  Species ~ ., data=trainData,
  method="knn",
  trControl=ctrl,
  preProcess=c("center", "scale"),
  tuneLength=10
)

print(model_knn)
plot(model_knn)



# Step 7: Model Evaluation

pred_knn <- predict(model_knn, testData)
confusionMatrix(pred_knn, testData$Species)


# Step 8: Variable Importance

importance <- varImp(model_knn)
print(importance)
plot(importance)




