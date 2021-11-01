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
-- Table structure for table `members`
--

DROP TABLE IF EXISTS `members`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `members` (
  `MemberID` int(11) NOT NULL AUTO_INCREMENT,
  `ClubID` int(11) NOT NULL,
  `TeamID` int(11) DEFAULT NULL,
  `MemberFirstName` varchar(50) NOT NULL,
  `MemberLastName` varchar(50) NOT NULL,
  `Address1` varchar(50) DEFAULT NULL,
  `Address2` varchar(50) DEFAULT NULL,
  `City` varchar(30) NOT NULL,
  `Email` varchar(320) NOT NULL,
  `Phone` varchar(10) DEFAULT NULL,
  `Birthdate` date NOT NULL,
  `MembershipStatus` tinyint(1) NOT NULL,
  `AdminAccess` tinyint(1) NOT NULL,
  PRIMARY KEY (`MemberID`),
  KEY `TeamID` (`TeamID`,`ClubID`),
  CONSTRAINT `members_ibfk_1` FOREIGN KEY (`TeamID`, `ClubID`) REFERENCES `teams` (`TeamID`, `ClubID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5696 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `members`
--

LOCK TABLES `members` WRITE;
/*!40000 ALTER TABLE `members` DISABLE KEYS */;
INSERT INTO `members` VALUES (5623,23,123,'Beauden','Barrett','34 Main Sth Rd','Islington','Christchurch','beauden@allblack.co.nz','274658254','1999-06-07',1,0),(5643,23,156,'Aaron','Smith','47 Westminster St','St Albans','Christchurch','aaron@allblack.co.nz','222463854','1987-04-26',1,1),(5646,23,123,'Antoine','Dupont','123 Columbo St','Sydenham','Christchurch','antoine@crusadersrugby.co.nz','214567892','2001-12-08',1,0),(5689,23,102,'Grant','Fox','4567 Gingerbread Lane','Bowenvale','Christchurch','foxy@crusaders.co.nz','0214568274','1975-11-21',0,0),(5690,23,NULL,'Harry','Lo','109A Suva Street','Upper Riccarton','Christchurch','harrykhlo@gmail.com','+642102824','2000-01-01',1,0),(5691,23,NULL,'Harry','Lo','109A Suva Street','Upper Riccarton','Christchurch','harrykhlo@gmail.com','+642102824','2000-01-01',1,0),(5692,23,NULL,'Harry','Lo','109A Suva Street','Upper Riccarton','Christchurch','harrykhlo@gmail.com','+642102824','2000-01-01',1,0),(5693,23,153,'Harry','Lo','109A Suva Street','Upper Riccarton','Christchurch','harrykhlo@gmail.com','+642102824','2000-01-01',1,0),(5694,23,156,'Harry','Lo','109A Suva Street','Upper Riccarton','Christchurch','harrykhlo@gmail.com','+642102824','2000-01-01',1,0),(5695,23,156,'Harry','Lo','109A Suva Street','Upper Riccarton','Christchurch','harrykhlo@gmail.com','+642102824','2000-01-01',1,0);
/*!40000 ALTER TABLE `members` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-01 13:57:35
