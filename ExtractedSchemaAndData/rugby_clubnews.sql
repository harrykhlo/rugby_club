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
-- Table structure for table `clubnews`
--

DROP TABLE IF EXISTS `clubnews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `clubnews` (
  `NewsID` int(11) NOT NULL AUTO_INCREMENT,
  `ClubID` int(11) NOT NULL,
  `NewsHeader` varchar(100) DEFAULT NULL,
  `NewsByline` varchar(50) DEFAULT NULL,
  `NewsDate` date DEFAULT NULL,
  `News` text,
  PRIMARY KEY (`NewsID`),
  KEY `ClubID` (`ClubID`),
  CONSTRAINT `clubnews_ibfk_1` FOREIGN KEY (`ClubID`) REFERENCES `clubs` (`ClubID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clubnews`
--

LOCK TABLES `clubnews` WRITE;
/*!40000 ALTER TABLE `clubnews` DISABLE KEYS */;
INSERT INTO `clubnews` VALUES (3,23,'Aaron Smith to miss rest of Fortinet rugby championship','By Superman','2021-06-28','All Blacks halfback Aaron Smith won\'t be joining the All Blacks in Australia for the remainder of the Fortinet Rugby Championship. 32-year-old Smith stayed in New Zealand to be with his family awaiting the birth of his second child. He will join his Manawat? Turbos team this week to train and play in the Bunnings Warehouse NPC this season. Smith says he\'s excited about playing for the Turbos and can\'t wait to get back on the field.'),(4,23,'All Blacks find areas to improve ahead of Pumas rematch','By Joe Bloggs','2021-09-15','A different approach can be expected from Argentina on Saturday when taking on the All Blacks at Suncorp Stadium in Brisbane in the Fortinet Rugby Championship. That\'s the feeling lock Scott Barrett, 45 Tests, has ahead of the game. The South Americans, who have endured more obstacles than any of their Championship opponents in arriving at the tournament, have not scored a point against the All Blacks in the two outings since last year\'s triumph when winning their first Test against them.\nThat would add to the desperation they brought to the Test. They\'ll look at their tape and present different pictures. They\'ll probably turn up with a little more of an edge he said. But while the Pumas would be looking to get better, so would the All Blacks.'),(5,23,'testNewsHeader 1','By Tester 1','2021-03-28','Test News Contents 1'),(6,23,'testNewsHeader 2','By Tester 2','2021-07-28','Test News Contents 2'),(13,23,'News Header 123','by tester 123','2023-01-01','Future news'),(14,23,'News Header 999','By tester 999','2024-01-01','New News 999'),(15,23,'Admin Added News Header','By admin','2025-01-01','Admin News'),(16,23,'New Header test 2021.10.23','By tester 2021.10.23','2023-01-01','Test news'),(17,23,'News Header test 999','By tester 999','2222-12-30','This is a testing news 999'),(18,23,'','','0000-00-00','');
/*!40000 ALTER TABLE `clubnews` ENABLE KEYS */;
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
