library(dplyr)
library(ggplot2)

students <- data.frame(
  ID = 1:6,
  Name = c("Asha", "Ravi", "Meena", "Kiran", "Divya", "Rahul"),
  Age = c(20, 22, 21, 23, 22, 21),
  Score = c(85, 90, 78, 88, 92, 80),
  Dept = c("CS", "Math", "CS", "Physics", "Math", "CS")
)
students



# Scatterplot: Age vs Score, colored by Dept
ggplot(students, aes(x=Age, y=Score, color=Dept)) +
  geom_point(size=3) +
  geom_smooth(method="lm", se=FALSE) +
  labs(title="Student Scores by Age and Dept", x="Age", y="Score") +
  theme_minimal()
