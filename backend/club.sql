CREATE DATABASE  IF NOT EXISTS `demo` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `demo`;
-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: demo
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `club`
--

DROP TABLE IF EXISTS `club`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `club` (
  `id` int NOT NULL,
  `number` varchar(13) NOT NULL,
  `name` varchar(100) NOT NULL,
  `seat` int NOT NULL,
  `song` varchar(100) NOT NULL,
  `time` datetime NOT NULL,
  `status` int NOT NULL,
  `ques1` int NOT NULL,
  `ques2` int NOT NULL,
  `alldone` int NOT NULL,
  PRIMARY KEY (`club_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `club`
--

LOCK TABLES `club` WRITE;
/*!40000 ALTER TABLE `club` DISABLE KEYS */;
INSERT INTO `club` VALUES (1,'0313','ibtehaj',4,'jazba junoon by ali azmat','2022-10-02 10:02:07',0,0,1,0),(3,'0313','bilal',5,'waka waka','2022-10-02 10:07:22',0,0,1,1),(17,'923237655474','Ibtehaj',7,'Waka waka by shakira','2022-10-02 16:20:36',0,1,1,1),(18,'923101062596','Ibtehaj Khan',7,'eminem loose yourself','2022-10-02 16:38:31',0,1,1,1),(19,'923237655474','Ibtehaj',5,'Gangasta paradise by big e','2022-10-02 16:39:28',0,1,1,1),(20,'923237655474','Ibtehaj',4,'Mujhe tum nazar se gira to rahe ho by mehdi hasan','2022-10-02 19:57:02',0,1,1,1),(21,'923237655474','Ibtehaj',8,'Love me like you do remix','2022-10-02 22:32:26',0,1,1,1),(23,'923237655474','Ibtehaj',5,'Afreen afreen by rfak','2022-10-02 23:04:21',0,1,1,1),(25,'923213277510','Dua Jan M',5,'Aaj ki Raat','2022-10-02 23:10:37',0,1,1,1),(27,'923101062596','Ibtehaj Khan',8,'waka waka by shakira','2022-10-03 11:33:43',0,1,1,1),(28,'923101062596','Ibtehaj Khan',22,'pasoori','2022-10-03 11:51:24',0,1,1,1),(31,'923213277510','Dua Jan M',0,'','2022-10-03 22:14:44',0,1,0,0),(32,'923101062590','Ibtehaj Khan',22,'pasoori','2022-10-03 11:51:24',0,1,1,1),(33,'03324472937','nofel',22,'karachi mera','2022-10-15 06:26:53',0,1,1,1);
/*!40000 ALTER TABLE `club` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-10-16 22:09:56
