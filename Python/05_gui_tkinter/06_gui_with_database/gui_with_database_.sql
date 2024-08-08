create database a;
use a;
show tables;

CREATE TABLE record (
  id int NOT NULL AUTO_INCREMENT,
  value1 int DEFAULT NULL,
  value2 int DEFAULT NULL,
  PRIMARY KEY (id)
) ;


select * from record;
