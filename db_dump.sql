CREATE DATABASE  IF NOT EXISTS `db_test1` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `db_test1`;
-- MySQL dump 10.13  Distrib 5.7.20, for Linux (x86_64)
--
-- Host: dbprojectinstance.cmdvn9umwvmv.ap-southeast-1.rds.amazonaws.com    Database: db_test1
-- ------------------------------------------------------
-- Server version	5.6.39-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Building`
--

DROP TABLE IF EXISTS `Building`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Building` (
  `name` varchar(60) NOT NULL,
  `faculty_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`name`),
  KEY `faculty_id` (`faculty_id`),
  CONSTRAINT `Building_ibfk_1` FOREIGN KEY (`faculty_id`) REFERENCES `Faculty` (`faculty_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Building`
--

LOCK TABLES `Building` WRITE;
/*!40000 ALTER TABLE `Building` DISABLE KEYS */;
INSERT INTO `Building` VALUES ('Vidya',2),('Engineering 1',21),('Engineering 3',21),('Engineering 4',21),('Borom',22),('Mahamakut',23),('Mahit',26);
/*!40000 ALTER TABLE `Building` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Building_Room`
--

DROP TABLE IF EXISTS `Building_Room`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Building_Room` (
  `room_no` int(11) NOT NULL,
  `building_name` varchar(60) NOT NULL,
  `capacity` int(11) NOT NULL,
  PRIMARY KEY (`room_no`,`building_name`),
  KEY `building_name` (`building_name`),
  CONSTRAINT `Building_Room_ibfk_1` FOREIGN KEY (`building_name`) REFERENCES `Building` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Building_Room`
--

LOCK TABLES `Building_Room` WRITE;
/*!40000 ALTER TABLE `Building_Room` DISABLE KEYS */;
INSERT INTO `Building_Room` VALUES (201,'Mahamakut',100),(204,'Engineering 3',30),(205,'Engineering 3',30),(206,'Engineering 3',30),(302,'Engineering 1',30),(409,'Engineering 3',30),(409,'Vidya',20),(510,'Borom',60),(1804,'Engineering 4',30);
/*!40000 ALTER TABLE `Building_Room` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Course`
--

DROP TABLE IF EXISTS `Course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Course` (
  `course_id` int(11) NOT NULL,
  `section` int(11) NOT NULL,
  `course_semester_no` int(11) NOT NULL,
  `course_year` int(11) NOT NULL,
  `course_name` varchar(60) NOT NULL,
  `credit` int(11) NOT NULL,
  `midterm_exam_date` date DEFAULT NULL,
  `final_exam_date` date DEFAULT NULL,
  `course_capacity` int(11) DEFAULT NULL,
  `registered_amount` int(11) DEFAULT NULL,
  `course_Type` varchar(60) NOT NULL,
  `course_gpax` float DEFAULT NULL,
  `major_id` int(11) DEFAULT NULL,
  `faculty_id` int(11) DEFAULT NULL,
  `room_no` int(11) DEFAULT NULL,
  `building_name` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`course_id`,`section`,`course_semester_no`,`course_year`),
  KEY `building_name` (`building_name`,`room_no`),
  KEY `course_semester_no` (`course_semester_no`,`course_year`),
  KEY `faculty_id` (`faculty_id`,`major_id`),
  CONSTRAINT `Course_ibfk_1` FOREIGN KEY (`building_name`, `room_no`) REFERENCES `Building_Room` (`building_name`, `room_no`),
  CONSTRAINT `Course_ibfk_2` FOREIGN KEY (`course_semester_no`, `course_year`) REFERENCES `Semester` (`semester_no`, `year`),
  CONSTRAINT `Course_ibfk_3` FOREIGN KEY (`faculty_id`, `major_id`) REFERENCES `Major` (`faculty_id`, `major_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Course`
--

LOCK TABLES `Course` WRITE;
/*!40000 ALTER TABLE `Course` DISABLE KEYS */;
INSERT INTO `Course` VALUES (2110101,1,1,2558,'Computer Programming',3,'2016-03-01','2016-05-10',30,0,'Engineering Freshmen Only',NULL,10,21,302,'Engineering 1'),(2110101,1,1,2560,'Computer Programming',3,'2018-03-01','2018-05-10',30,0,'Engineering Freshmen Only',NULL,10,21,302,'Engineering 1'),(2110422,1,1,2560,'Database Management Systems Design',3,'2018-03-02','2018-05-11',30,0,'CP Juniors Only',NULL,10,21,204,'Engineering 3'),(2110422,2,1,2560,'Database Management Systems Design',3,'2018-03-02','2018-05-11',30,0,'CP Juniors Only',NULL,10,21,205,'Engineering 3'),(2110422,3,1,2560,'Database Management Systems Design',3,'2018-03-02','2018-05-11',30,0,'CP Juniors Only',NULL,10,21,206,'Engineering 3'),(2110422,33,1,2560,'Database Management Systems Design',3,'2018-03-02','2018-05-11',30,0,'CP Juniors Only',NULL,10,21,409,'Engineering 3'),(2313213,1,1,2558,'Digital Photography',3,'2016-03-10','2016-05-21',100,0,'Gened Science',NULL,13,23,201,'Mahamakut'),(2313213,1,1,2560,'Digital Photography',3,'2018-03-10','2018-05-21',100,0,'Gened Science',NULL,13,23,201,'Mahamakut');
/*!40000 ALTER TABLE `Course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Dorm_Room`
--

DROP TABLE IF EXISTS `Dorm_Room`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Dorm_Room` (
  `dorm_name` varchar(60) NOT NULL,
  `dorm_room_no` int(11) NOT NULL,
  PRIMARY KEY (`dorm_name`,`dorm_room_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Dorm_Room`
--

LOCK TABLES `Dorm_Room` WRITE;
/*!40000 ALTER TABLE `Dorm_Room` DISABLE KEYS */;
INSERT INTO `Dorm_Room` VALUES ('A',1),('B',2),('C',3),('D',4),('E',5);
/*!40000 ALTER TABLE `Dorm_Room` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Faculty`
--

DROP TABLE IF EXISTS `Faculty`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Faculty` (
  `faculty_id` int(11) NOT NULL AUTO_INCREMENT,
  `faculty_name` varchar(60) NOT NULL,
  PRIMARY KEY (`faculty_id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Faculty`
--

LOCK TABLES `Faculty` WRITE;
/*!40000 ALTER TABLE `Faculty` DISABLE KEYS */;
INSERT INTO `Faculty` VALUES (2,'Gened'),(21,'Engineering'),(22,'Arts'),(23,'Science'),(24,'Political Science'),(25,'Architecture'),(26,'Finance');
/*!40000 ALTER TABLE `Faculty` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Major`
--

DROP TABLE IF EXISTS `Major`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Major` (
  `major_id` int(11) NOT NULL,
  `faculty_id` int(11) NOT NULL,
  `major_name` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`major_id`,`faculty_id`),
  KEY `faculty_id` (`faculty_id`),
  CONSTRAINT `Major_ibfk_1` FOREIGN KEY (`faculty_id`) REFERENCES `Faculty` (`faculty_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Major`
--

LOCK TABLES `Major` WRITE;
/*!40000 ALTER TABLE `Major` DISABLE KEYS */;
INSERT INTO `Major` VALUES (1,21,'Civil Engineering'),(1,22,'Thai'),(1,23,'Mathematics and Computer Science'),(2,21,'Electrical Engineering'),(2,22,'English'),(3,21,'Mechanical Engineering'),(4,22,'History'),(7,22,'Philosophy'),(9,21,'Metallurgical Engineering'),(10,21,'Computer Engineering'),(13,23,'Photo Science');
/*!40000 ALTER TABLE `Major` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Pay_Tuition`
--

DROP TABLE IF EXISTS `Pay_Tuition`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Pay_Tuition` (
  `sid` int(11) NOT NULL,
  `tuition_semester` int(11) NOT NULL,
  `tuition_year` int(11) NOT NULL,
  `faculty_id` int(11) NOT NULL,
  `tuition_late` tinyint(1) NOT NULL,
  `tuition_paid` tinyint(1) NOT NULL,
  PRIMARY KEY (`sid`,`tuition_semester`,`tuition_year`,`faculty_id`),
  KEY `faculty_id` (`faculty_id`,`tuition_semester`,`tuition_year`),
  CONSTRAINT `Pay_Tuition_ibfk_1` FOREIGN KEY (`faculty_id`, `tuition_semester`, `tuition_year`) REFERENCES `Tuition` (`faculty_id`, `tuition_semester`, `tuition_year`),
  CONSTRAINT `Pay_Tuition_ibfk_2` FOREIGN KEY (`sid`) REFERENCES `Student` (`sid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Pay_Tuition`
--

LOCK TABLES `Pay_Tuition` WRITE;
/*!40000 ALTER TABLE `Pay_Tuition` DISABLE KEYS */;
INSERT INTO `Pay_Tuition` VALUES (10000,2,2018,21,0,0),(10002,2,2016,25,0,1);
/*!40000 ALTER TABLE `Pay_Tuition` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Professor`
--

DROP TABLE IF EXISTS `Professor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Professor` (
  `professor_id` int(11) NOT NULL AUTO_INCREMENT,
  `major_id` int(11) DEFAULT NULL,
  `faculty_id` int(11) DEFAULT NULL,
  `name` varchar(60) NOT NULL,
  `surname` varchar(60) NOT NULL,
  PRIMARY KEY (`professor_id`),
  KEY `faculty_id` (`faculty_id`),
  KEY `major_id` (`major_id`),
  CONSTRAINT `Professor_ibfk_1` FOREIGN KEY (`faculty_id`) REFERENCES `Major` (`faculty_id`),
  CONSTRAINT `Professor_ibfk_2` FOREIGN KEY (`major_id`) REFERENCES `Major` (`major_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5107 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Professor`
--

LOCK TABLES `Professor` WRITE;
/*!40000 ALTER TABLE `Professor` DISABLE KEYS */;
INSERT INTO `Professor` VALUES (1000,1,21,'Sunny','Sobright'),(1001,1,21,'Moon','Mmmmm'),(1002,9,21,'Sommm','Oh'),(2011,1,22,'Funny','Muchjoke'),(2012,1,23,'Somewhere','Ibelong'),(2121,10,21,'Attawish','Youamarrychristmas'),(2173,10,21,'Bi','nary'),(2222,10,21,'Crass','Ennab'),(2323,10,21,'Apirat','Cisco'),(3045,13,23,'Obiwan','Kenobi'),(5106,7,22,'Iam','Urfather');
/*!40000 ALTER TABLE `Professor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Request`
--

DROP TABLE IF EXISTS `Request`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Request` (
  `sid` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `section` int(11) NOT NULL,
  `course_semester_no` int(11) NOT NULL,
  `course_year` int(11) NOT NULL,
  `result` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`sid`,`course_id`,`section`,`course_semester_no`,`course_year`),
  KEY `course_id` (`course_id`,`section`,`course_semester_no`,`course_year`),
  CONSTRAINT `Request_ibfk_1` FOREIGN KEY (`course_id`, `section`, `course_semester_no`, `course_year`) REFERENCES `Course` (`course_id`, `section`, `course_semester_no`, `course_year`),
  CONSTRAINT `Request_ibfk_2` FOREIGN KEY (`sid`) REFERENCES `Student` (`sid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Request`
--

LOCK TABLES `Request` WRITE;
/*!40000 ALTER TABLE `Request` DISABLE KEYS */;
/*!40000 ALTER TABLE `Request` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Semester`
--

DROP TABLE IF EXISTS `Semester`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Semester` (
  `semester_no` int(11) NOT NULL,
  `year` int(11) NOT NULL,
  `enroll_start_date` date DEFAULT NULL,
  `enroll_end_date` date DEFAULT NULL,
  `withdraw_start_date` date DEFAULT NULL,
  `withdraw_end_date` date DEFAULT NULL,
  PRIMARY KEY (`semester_no`,`year`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Semester`
--

LOCK TABLES `Semester` WRITE;
/*!40000 ALTER TABLE `Semester` DISABLE KEYS */;
INSERT INTO `Semester` VALUES (1,2558,'2016-01-01','2016-01-15','2016-03-01','2016-05-01'),(1,2560,'2018-01-01','2018-01-15','2018-03-01','2018-05-01'),(2,2560,'2018-08-01','2018-08-15','2018-11-01','2019-01-01');
/*!40000 ALTER TABLE `Semester` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Student`
--

DROP TABLE IF EXISTS `Student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Student` (
  `sid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(60) NOT NULL,
  `enroll_year` int(11) DEFAULT NULL,
  `graduated` tinyint(1) DEFAULT NULL,
  `degree` varchar(60) DEFAULT NULL,
  `gpax` float DEFAULT NULL,
  `dorm_score` int(11) DEFAULT NULL,
  `dorm_name` varchar(60) DEFAULT NULL,
  `dorm_room_no` int(11) DEFAULT NULL,
  `faculty_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`sid`),
  KEY `dorm_name` (`dorm_name`,`dorm_room_no`),
  KEY `faculty_id` (`faculty_id`),
  CONSTRAINT `Student_ibfk_1` FOREIGN KEY (`dorm_name`, `dorm_room_no`) REFERENCES `Dorm_Room` (`dorm_name`, `dorm_room_no`),
  CONSTRAINT `Student_ibfk_2` FOREIGN KEY (`faculty_id`) REFERENCES `Faculty` (`faculty_id`)
) ENGINE=InnoDB AUTO_INCREMENT=30005 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Student`
--

LOCK TABLES `Student` WRITE;
/*!40000 ALTER TABLE `Student` DISABLE KEYS */;
INSERT INTO `Student` VALUES (10000,'Ah',2018,0,'Bachelor',2.3,100,'A',1,21),(10001,'Than',2018,0,'Bachelor',3.9,NULL,NULL,NULL,23),(10002,'Khem',2016,0,'Master',3.58,100,'B',2,25),(20003,'Nick',2013,1,'Bachelor',2.67,NULL,NULL,NULL,22),(20005,'Gam',2015,1,'Master',2.99,100,'D',4,24),(30004,'Gam',2017,0,'Doctoral',3.5,100,'D',4,24);
/*!40000 ALTER TABLE `Student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Study`
--

DROP TABLE IF EXISTS `Study`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Study` (
  `sid` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `section` int(11) NOT NULL,
  `course_semester_no` int(11) NOT NULL,
  `course_year` int(11) NOT NULL,
  `grade` float DEFAULT NULL,
  PRIMARY KEY (`sid`,`course_id`,`section`,`course_semester_no`,`course_year`),
  KEY `course_id` (`course_id`,`section`,`course_semester_no`,`course_year`),
  CONSTRAINT `Study_ibfk_1` FOREIGN KEY (`course_id`, `section`, `course_semester_no`, `course_year`) REFERENCES `Course` (`course_id`, `section`, `course_semester_no`, `course_year`),
  CONSTRAINT `Study_ibfk_2` FOREIGN KEY (`sid`) REFERENCES `Student` (`sid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Study`
--

LOCK TABLES `Study` WRITE;
/*!40000 ALTER TABLE `Study` DISABLE KEYS */;
INSERT INTO `Study` VALUES (10000,2110101,1,1,2558,4),(10000,2110422,3,1,2560,NULL),(10000,2313213,1,1,2558,2),(10001,2110422,33,1,2560,NULL),(10002,2110422,33,1,2560,NULL);
/*!40000 ALTER TABLE `Study` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Teaches`
--

DROP TABLE IF EXISTS `Teaches`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Teaches` (
  `professor_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `section` int(11) NOT NULL,
  `course_semester_no` int(11) NOT NULL,
  `course_year` int(11) NOT NULL,
  PRIMARY KEY (`professor_id`,`course_id`,`section`,`course_semester_no`,`course_year`),
  KEY `course_id` (`course_id`,`section`,`course_semester_no`,`course_year`),
  CONSTRAINT `Teaches_ibfk_1` FOREIGN KEY (`professor_id`) REFERENCES `Professor` (`professor_id`),
  CONSTRAINT `Teaches_ibfk_2` FOREIGN KEY (`course_id`, `section`, `course_semester_no`, `course_year`) REFERENCES `Course` (`course_id`, `section`, `course_semester_no`, `course_year`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Teaches`
--

LOCK TABLES `Teaches` WRITE;
/*!40000 ALTER TABLE `Teaches` DISABLE KEYS */;
INSERT INTO `Teaches` VALUES (2173,2110101,1,1,2558),(2121,2110101,1,1,2560),(2173,2110422,1,1,2560),(2323,2110422,2,1,2560),(2222,2110422,3,1,2560),(2121,2110422,33,1,2560),(3045,2313213,1,1,2558),(3045,2313213,1,1,2560);
/*!40000 ALTER TABLE `Teaches` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Tuition`
--

DROP TABLE IF EXISTS `Tuition`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Tuition` (
  `tuition_semester` int(11) NOT NULL,
  `tuition_year` int(11) NOT NULL,
  `faculty_id` int(11) NOT NULL,
  `tuition_degree` varchar(60) DEFAULT NULL,
  `tuition_amount` int(11) DEFAULT NULL,
  `tuition_start_date` date DEFAULT NULL,
  `tuition_end_date` date DEFAULT NULL,
  PRIMARY KEY (`tuition_semester`,`tuition_year`,`faculty_id`),
  KEY `faculty_id` (`faculty_id`),
  CONSTRAINT `Tuition_ibfk_1` FOREIGN KEY (`faculty_id`) REFERENCES `Faculty` (`faculty_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Tuition`
--

LOCK TABLES `Tuition` WRITE;
/*!40000 ALTER TABLE `Tuition` DISABLE KEYS */;
INSERT INTO `Tuition` VALUES (1,2014,21,'Bachelor',21000,'2014-07-21','2014-07-29'),(1,2015,23,'Master',23000,'2015-07-21','2015-07-29'),(1,2016,21,'Bachelor',21000,'2016-07-21','2016-07-29'),(1,2017,21,'Doctoral',21000,'2017-07-21','2017-07-29'),(2,2016,24,'Bachelor',21000,'2016-12-21','2016-12-29'),(2,2016,25,'Bachelor',21000,'2016-12-21','2016-12-29'),(2,2018,21,'Bachelor',21000,'2018-12-21','2018-12-29');
/*!40000 ALTER TABLE `Tuition` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('f26feff4c26f');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(64) DEFAULT NULL,
  `password` varchar(64) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_user_username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'10001','password'),(2,'5831058721','password'),(3,'10000','lonely'),(4,'10002','eiei');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-04-25 23:09:36
