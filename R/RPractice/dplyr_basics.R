library(dplyr)

students <- data.frame(
  ID = 1:6,
  Name = c("Asha", "Ravi", "Meena", "Kiran", "Divya", "Rahul"),
  Age = c(20, 22, 21, 23, 22, 21),
  Score = c(85, 90, 78, 88, 92, 80),
  Dept = c("CS", "Math", "CS", "Physics", "Math", "CS")
)
students


filter(students, Age > 21)

group_by(filter(students, Age > 21),Dept)

summarise(group_by(filter(students, Age > 21),Dept),Average_Score = mean(Score))


arrange(summarise(group_by(filter(students, Age > 21),Dept),Average_Score = mean(Score)),desc(Average_Score))


students %>%
  filter(Age > 21) %>%
  group_by(Dept) %>%
  summarise(Average_Score = mean(Score)) %>%
  arrange(desc(Average_Score))


