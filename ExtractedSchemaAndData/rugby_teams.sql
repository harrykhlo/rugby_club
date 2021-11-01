CREATE DATABASE  IF NOT EXISTS `rugby` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `rugby`;
-- MySQL dump 10.16  Distrib 10.1.38-MariaDB, for Win32 (AMD64)
--
-- Host: 127.0.0.1    Database: rugby
-- ------------------------------------------------------
-- Server version	10.1.38-MariaDB

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
-- Table structure for table `teams`
--

DROP TABLE IF EXISTS `teams`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `teams` (
  `TeamID` int(11) NOT NULL AUTO_INCREMENT,
  `ClubID` int(11) NOT NULL,
  `TeamName` varchar(80) NOT NULL,
  `TeamGrade` int(11) DEFAULT NULL,
  PRIMARY KEY (`TeamID`),
  KEY `TeamClub` (`TeamID`,`ClubID`),
  KEY `TeamGrade` (`TeamGrade`),
  KEY `ClubID` (`ClubID`),
  CONSTRAINT `teams_ibfk_1` FOREIGN KEY (`TeamGrade`) REFERENCES `grades` (`GradeID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `teams_ibfk_2` FOREIGN KEY (`ClubID`) REFERENCES `clubs` (`ClubID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=161 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teams`
--

LOCK TABLES `teams` WRITE;
/*!40000 ALTER TABLE `teams` DISABLE KEYS */;
INSERT INTO `teams` VALUES (101,23,'Junior Crusaders',1),(102,23,'Crushers',6),(103,23,'Southern Boot',3),(123,23,'Between the Posts',5),(125,6,'Midgets',3),(133,12,'Black Ferns',6),(143,12,'ScrumTime',5),(152,6,'All Blacks',1),(153,23,'test team name 1',1),(154,23,'asd123',6),(155,23,'Test team name 1',3),(156,23,'Test Team Name 2',5),(157,23,'Team Name Test 3',6),(158,12,'Test Opposition Team Name 1',3),(159,23,'Test Club Name 1',6),(160,6,'Test Opposition Team 1',5);
/*!40000 ALTER TABLE `teams` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-01 13:57:36
