-- MariaDB dump 10.18  Distrib 10.5.8-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: e_vent
-- ------------------------------------------------------
-- Server version	10.5.8-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `e_vent`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `e_vent` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `e_vent`;

--
-- Table structure for table `event`
--

DROP TABLE IF EXISTS `event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `event` (
  `event_id` int(11) NOT NULL AUTO_INCREMENT,
  `namaEvent` varchar(255) NOT NULL,
  `deskripsi` varchar(255) NOT NULL,
  `tanggal` date NOT NULL,
  `biaya` int(11) NOT NULL,
  `penyelenggara_id` int(11) NOT NULL DEFAULT 1,
  PRIMARY KEY (`event_id`),
  KEY `fk_penyelenggara_id` (`penyelenggara_id`),
  CONSTRAINT `fk_penyelenggara_id` FOREIGN KEY (`penyelenggara_id`) REFERENCES `penyelenggara` (`penyelenggara_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `event`
--

LOCK TABLES `event` WRITE;
/*!40000 ALTER TABLE `event` DISABLE KEYS */;
INSERT INTO `event` (`event_id`, `namaEvent`, `deskripsi`, `tanggal`, `biaya`, `penyelenggara_id`) VALUES (1,'a','test event','2021-07-15',0,1),(2,'astaga','astaga','2021-06-01',0,1),(3,'Test1','Test1','2021-03-19',50000,1),(4,'Test1','Test1','2021-03-19',50000,1);
/*!40000 ALTER TABLE `event` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `member`
--

DROP TABLE IF EXISTS `member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `member` (
  `member_id` int(11) NOT NULL AUTO_INCREMENT,
  `nama` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `tgl_lahir` date NOT NULL,
  `password` varchar(16) NOT NULL,
  PRIMARY KEY (`member_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
INSERT INTO `member` (`member_id`, `nama`, `email`, `tgl_lahir`, `password`) VALUES (1,'A','a@mail.com','2000-07-12','a'),(2,'test','test','1970-07-23','test');
INSERT INTO `member` (`member_id`, `nama`, `email`, `tgl_lahir`, `password`) VALUES (NULL,'Rizky A','13519132@std.stei.itb.ac.id','1998-02-02','admin'),(NULL,'Rehagana S.','13519117@std.stei.itb.ac.id','1999-03-03','admin2'),(NULL,'Test dari App','test@test.com','2001-11-21','test'),(NULL,'Jonathan','jonathan@yahoo.co.id','2000-07-10','jonathan'),(NULL,'Joni','joni@joni.id','1970-07-14','joni'),(NULL,'Test5','test5@test.com','2001-11-29','test5'),(NULL,'Rizky','rizky@rizky.com','2001-11-29','rizky');
/*!40000 ALTER TABLE `member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `member_event`
--

DROP TABLE IF EXISTS `member_event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `member_event` (
  `member_id` int(11) NOT NULL,
  `event_id` int(11) NOT NULL,
  PRIMARY KEY (`member_id`,`event_id`),
  KEY `event_id` (`event_id`),
  CONSTRAINT `member_event_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `member` (`member_id`),
  CONSTRAINT `member_event_ibfk_2` FOREIGN KEY (`event_id`) REFERENCES `event` (`event_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member_event`
--

LOCK TABLES `member_event` WRITE;
/*!40000 ALTER TABLE `member_event` DISABLE KEYS */;
INSERT INTO `member_event` (`member_id`, `event_id`) VALUES (2,1),(2,3);
/*!40000 ALTER TABLE `member_event` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `penyelenggara`
--

DROP TABLE IF EXISTS `penyelenggara`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `penyelenggara` (
  `penyelenggara_id` int(11) NOT NULL AUTO_INCREMENT,
  `nama` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `no_telp` varchar(20) NOT NULL,
  `password` varchar(16) NOT NULL,
  `deskripsi` varchar(255) NOT NULL,
  PRIMARY KEY (`penyelenggara_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `penyelenggara`
--

LOCK TABLES `penyelenggara` WRITE;
/*!40000 ALTER TABLE `penyelenggara` DISABLE KEYS */;
INSERT INTO `penyelenggara` (`penyelenggara_id`, `nama`, `email`, `no_telp`, `password`, `deskripsi`) VALUES (1,'test','test','0000','test','test');
INSERT INTO `penyelenggara` (`penyelenggara_id`, `nama`, `email`, `no_telp`, `password`, `deskripsi`) VALUES (4,'Test1','test1@yahoo.com','082233445566','test1','Ini Deskripsi Penyelenggara'),(5,'joni','joni@joni.id','082211223344','joni','joni'),(6,'test5','test5@test.com','080882823232','test5','test5');
/*!40000 ALTER TABLE `penyelenggara` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-04-20 20:49:13
