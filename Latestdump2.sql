-- MySQL dump 10.13  Distrib 5.7.20, for macos10.12 (x86_64)
--
-- Host: itsdb.c4idvpseeifj.ap-south-1.rds.amazonaws.com    Database: OnlineClassroom
-- ------------------------------------------------------
-- Server version	5.7.22-log

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
-- Current Database: `OnlineClassroom`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `OnlineClassroom` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `OnlineClassroom`;

--
-- Table structure for table `Announcement_announcement`
--

DROP TABLE IF EXISTS `Announcement_announcement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Announcement_announcement` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` longtext,
  `created_on` datetime(6) NOT NULL,
  `announcer_id` int(11) NOT NULL,
  `classroom_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Announcement_announc_classroom_id_98d6d028_fk_Classroom` (`classroom_id`),
  KEY `Announcement_announc_announcer_id_90f3252f_fk_AuthUser_` (`announcer_id`),
  CONSTRAINT `Announcement_announc_announcer_id_90f3252f_fk_AuthUser_` FOREIGN KEY (`announcer_id`) REFERENCES `AuthUser_user` (`id`),
  CONSTRAINT `Announcement_announc_classroom_id_98d6d028_fk_Classroom` FOREIGN KEY (`classroom_id`) REFERENCES `Classroom_classroom` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Announcement_announcement`
--


/*!40000 ALTER TABLE `Announcement_announcement` DISABLE KEYS */;
INSERT INTO `Announcement_announcement` VALUES (1,'NO DBMS class this week.','2018-10-16 06:43:53.055345',13,3),(9,'Quiz coming this week.','2018-10-25 20:44:34.816082',13,3);
/*!40000 ALTER TABLE `Announcement_announcement` ENABLE KEYS */;
 

--
-- Table structure for table `Announcement_announcement_comment`
--

DROP TABLE IF EXISTS `Announcement_announcement_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Announcement_announcement_comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `announcement_id` int(11) NOT NULL,
  `comment_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Announcement_announcemen_announcement_id_comment__8eca7910_uniq` (`announcement_id`,`comment_id`),
  KEY `Announcement_announc_comment_id_3efeeffd_fk_Comment_c` (`comment_id`),
  CONSTRAINT `Announcement_announc_announcement_id_1cba5d2f_fk_Announcem` FOREIGN KEY (`announcement_id`) REFERENCES `Announcement_announcement` (`id`),
  CONSTRAINT `Announcement_announc_comment_id_3efeeffd_fk_Comment_c` FOREIGN KEY (`comment_id`) REFERENCES `Comment_comment` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Announcement_announcement_comment`
--


/*!40000 ALTER TABLE `Announcement_announcement_comment` DISABLE KEYS */;
INSERT INTO `Announcement_announcement_comment` VALUES (1,1,1),(2,1,2),(3,1,3),(4,1,4),(5,1,5),(6,1,6),(21,1,11),(22,1,12),(29,9,1),(30,9,3),(31,9,4),(32,9,6),(33,9,7),(34,9,9),(35,9,11);
/*!40000 ALTER TABLE `Announcement_announcement_comment` ENABLE KEYS */;
 

--
-- Table structure for table `Assignment_assignment`
--

DROP TABLE IF EXISTS `Assignment_assignment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Assignment_assignment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) DEFAULT NULL,
  `attachment` varchar(100) NOT NULL,
  `deadline` datetime(6) DEFAULT NULL,
  `created_on` datetime(6) NOT NULL,
  `uploader_id` int(11) DEFAULT NULL,
  `classroom_id` int(11) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `max_score` int(11),
  PRIMARY KEY (`id`),
  KEY `Assignment_assignment_uploader_id_b971473d_fk_AuthUser_user_id` (`uploader_id`),
  KEY `Assignment_assignmen_classroom_id_9b519da5_fk_Classroom` (`classroom_id`),
  CONSTRAINT `Assignment_assignmen_classroom_id_9b519da5_fk_Classroom` FOREIGN KEY (`classroom_id`) REFERENCES `Classroom_classroom` (`id`),
  CONSTRAINT `Assignment_assignment_uploader_id_b971473d_fk_AuthUser_user_id` FOREIGN KEY (`uploader_id`) REFERENCES `AuthUser_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Assignment_assignment`
--


/*!40000 ALTER TABLE `Assignment_assignment` DISABLE KEYS */;
INSERT INTO `Assignment_assignment` VALUES (1,'Bonus Task 5','Assignments/UMA_umgL4HU','2018-10-25 22:00:00.000000','2018-10-25 13:17:12.085043',13,3,NULL,100),(2,'Bonus Task 2','Assignments/UMA_nADMroZ','2018-10-25 16:30:00.000000','2018-10-25 13:24:44.937682',13,3,NULL,50),(3,'Bonus Task 3','Assignments/UMA_dYiYcPq','2018-10-25 16:30:00.000000','2018-10-25 16:39:30.107452',13,3,NULL,30),(4,'Bonus Task 4','Assignments/UMA_6GppBW4','2018-10-25 16:41:00.000000','2018-10-25 16:40:42.534106',13,3,NULL,30),(5,'Bonus Task 1','Assignments/UMA_wWEaZ4n','2018-10-25 17:00:00.000000','2018-10-25 16:41:15.156278',13,3,NULL,30),(6,'Bonus task 6','Assignments/UMA_0bnC9GC','2018-10-29 19:31:00.000000','2018-10-25 20:39:45.441249',13,3,NULL,100);
/*!40000 ALTER TABLE `Assignment_assignment` ENABLE KEYS */;
 

--
-- Table structure for table `Assignment_assignment_comments`
--

DROP TABLE IF EXISTS `Assignment_assignment_comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Assignment_assignment_comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `assignment_id` int(11) NOT NULL,
  `comment_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Assignment_assignment_co_assignment_id_comment_id_ca1ac1b5_uniq` (`assignment_id`,`comment_id`),
  KEY `Assignment_assignmen_comment_id_f71c8702_fk_Comment_c` (`comment_id`),
  CONSTRAINT `Assignment_assignmen_assignment_id_11e46527_fk_Assignmen` FOREIGN KEY (`assignment_id`) REFERENCES `Assignment_assignment` (`id`),
  CONSTRAINT `Assignment_assignmen_comment_id_f71c8702_fk_Comment_c` FOREIGN KEY (`comment_id`) REFERENCES `Comment_comment` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Assignment_assignment_comments`
--


/*!40000 ALTER TABLE `Assignment_assignment_comments` DISABLE KEYS */;
INSERT INTO `Assignment_assignment_comments` VALUES (1,5,1);
/*!40000 ALTER TABLE `Assignment_assignment_comments` ENABLE KEYS */;
 

--
-- Table structure for table `Assignment_submission`
--

DROP TABLE IF EXISTS `Assignment_submission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Assignment_submission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `attachment` varchar(100) NOT NULL,
  `score` int(11) DEFAULT NULL,
  `submitted_on` datetime(6) NOT NULL,
  `assignment_id` int(11) DEFAULT NULL,
  `submitter_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `Assignment_submissio_assignment_id_0446d884_fk_Assignmen` (`assignment_id`),
  KEY `Assignment_submission_submitter_id_8ac6763c_fk_AuthUser_user_id` (`submitter_id`),
  CONSTRAINT `Assignment_submissio_assignment_id_0446d884_fk_Assignmen` FOREIGN KEY (`assignment_id`) REFERENCES `Assignment_assignment` (`id`),
  CONSTRAINT `Assignment_submission_submitter_id_8ac6763c_fk_AuthUser_user_id` FOREIGN KEY (`submitter_id`) REFERENCES `AuthUser_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Assignment_submission`
--


/*!40000 ALTER TABLE `Assignment_submission` DISABLE KEYS */;
INSERT INTO `Assignment_submission` VALUES (1,'Submission/1_Bonus_Task_5',70,'2018-10-25 16:51:21.064443',1,8),(2,'Submission/6_Bonus_task_6_VJYpyDW',-1,'2018-10-25 20:48:41.882178',6,16),(3,'Submission/1_Bonus_Task_5_Gy4DUJr',100,'2018-10-25 20:54:00.438754',1,16),(4,'Submission/6_Bonus_task_6_Ci3FXxt',-1,'2018-10-25 20:55:10.149996',6,15),(5,'Submission/1_Bonus_Task_5_GV8QadX',40,'2018-10-25 20:59:40.752125',1,15),(7,'Submission/1_Bonus_Task_5_4o4QPKO',60,'2018-10-25 21:05:27.109606',1,11),(8,'Submission/1_Bonus_Task_5_Az7nHWU',40,'2018-10-25 21:17:24.252786',1,17);
/*!40000 ALTER TABLE `Assignment_submission` ENABLE KEYS */;
 

--
-- Table structure for table `AuthUser_user`
--

DROP TABLE IF EXISTS `AuthUser_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `AuthUser_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `mobile_no` varchar(100) NOT NULL,
  `is_faculty` tinyint(1) NOT NULL,
  `avatar` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AuthUser_user`
--


/*!40000 ALTER TABLE `AuthUser_user` DISABLE KEYS */;
INSERT INTO `AuthUser_user` VALUES (1,'pbkdf2_sha256$120000$7aOtKk4UCBpf$Wb6HjNOUygc+LctOs7SL4i34/S3uDIgNT2ZjbUmCAY4=','2018-10-25 11:30:12.635587',1,'itsadmin','','','its@iiits.in',1,1,'2018-10-16 04:55:06.541427','',0,'default_avatar.png'),(8,'pbkdf2_sha256$120000$aejzDdYjZ6Ej$ClwVopMK8INVm9aKm2WfNaRpuZFIn9axY2p34eN/ikw=',NULL,0,'anubhav','anubhav','ujjawal','anubhav.u16@iiits.in',0,1,'2018-10-16 05:55:09.637767','7014156060',0,'default_avatar.png'),(9,'pbkdf2_sha256$120000$AvFCqPltSdlz$gWpYw2Fdun6vITJSRZ6Lz8XRX1tiUdo3lIq0yf8mYpg=',NULL,0,'sanyem','anurag','gupta','anurag.g16@iiits.in',0,1,'2018-10-16 05:58:42.871489','7014156060',0,'default_avatar.png'),(10,'pbkdf2_sha256$120000$k0UxRGz1nk3X$9+3kp3Whxo3edP8BMRaSk/+hwefZCSLSe/858q1xwfU=',NULL,0,'bhavi','anurag','gupta','anurag.g16@iiits.in',0,1,'2018-10-16 05:58:53.274486','7014156060',0,'default_avatar.png'),(11,'pbkdf2_sha256$120000$Rma4hpji8e6F$MgY6vfISr8gpYHZ1039O2PWD/yXHK6Z0F1TBZ1bQLLg=',NULL,0,'uday','anurag','gupta','anurag.g16@iiits.in',0,1,'2018-10-16 05:58:59.453122','7014156060',0,'default_avatar.png'),(12,'pbkdf2_sha256$120000$CXKB1IWt8ikU$nIaxx13GDRsoJrE+KvSXobVdTeZ60i5zBeS+RhvZphU=',NULL,0,'Vishvanath','bhavi','gupta','bhavi.g16@iiits.in',0,1,'2018-10-16 06:17:32.943015','7014156060',1,'default_avatar.png'),(13,'pbkdf2_sha256$120000$s5dimQXVa3rN$dZvjMITxCSMG6MXVTfQfAGMeI+BryS2Rm1Ks07bj/T0=',NULL,0,'UMA','bhavi','gupta','bhavi.g16@iiits.in',0,1,'2018-10-16 06:17:38.170732','7014156060',1,'default_avatar.png'),(15,'pbkdf2_sha256$120000$Vl6HZ3kiQN2s$8sLg73Szi/seUG1gL4MnHzyOVVdHj/kDtiWId7oQzv0=',NULL,0,'anurag','bhavi','gupta','bhavi.g16@iiits.in',0,1,'2018-10-16 06:19:01.000000','7014156060',0,'default_avatar.png'),(16,'pbkdf2_sha256$120000$q7AYAdAzn0je$KQG8iSHqHXFOZXu8WiW3BI19Oj5IwncPYBCWErOdp/M=',NULL,0,'garvit','bhavi','gupta','bhavi.g16@iiits.in',0,1,'2018-10-16 06:19:10.878436','7014156060',0,'default_avatar.png'),(17,'pbkdf2_sha256$120000$Bfa0hLDzfvvm$tJZJQXA9kc46rSMM+uXJVOs3JKzd8kZT/EROXrNFqks=',NULL,0,'sahaj','bhavi','gupta','bhavi.g16@iiits.in',0,1,'2018-10-16 06:19:15.490862','7014156060',0,'default_avatar.png');
/*!40000 ALTER TABLE `AuthUser_user` ENABLE KEYS */;
 

--
-- Table structure for table `AuthUser_user_groups`
--

DROP TABLE IF EXISTS `AuthUser_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `AuthUser_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `AuthUser_user_groups_user_id_group_id_004e50a2_uniq` (`user_id`,`group_id`),
  KEY `AuthUser_user_groups_group_id_ba031ad9_fk_auth_group_id` (`group_id`),
  CONSTRAINT `AuthUser_user_groups_group_id_ba031ad9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `AuthUser_user_groups_user_id_19b324d4_fk_AuthUser_user_id` FOREIGN KEY (`user_id`) REFERENCES `AuthUser_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AuthUser_user_groups`
--


/*!40000 ALTER TABLE `AuthUser_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `AuthUser_user_groups` ENABLE KEYS */;
 

--
-- Table structure for table `AuthUser_user_user_permissions`
--

DROP TABLE IF EXISTS `AuthUser_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `AuthUser_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `AuthUser_user_user_permi_user_id_permission_id_6cc36f83_uniq` (`user_id`,`permission_id`),
  KEY `AuthUser_user_user_p_permission_id_17fc7953_fk_auth_perm` (`permission_id`),
  CONSTRAINT `AuthUser_user_user_p_permission_id_17fc7953_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `AuthUser_user_user_p_user_id_c6126833_fk_AuthUser_` FOREIGN KEY (`user_id`) REFERENCES `AuthUser_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AuthUser_user_user_permissions`
--


/*!40000 ALTER TABLE `AuthUser_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `AuthUser_user_user_permissions` ENABLE KEYS */;
 

--
-- Table structure for table `Classroom_classroom`
--

DROP TABLE IF EXISTS `Classroom_classroom`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Classroom_classroom` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `code` varchar(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `creator_id` int(11) NOT NULL,
  `image` varchar(100) NOT NULL,
  `description` varchar(120) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `Classroom_classroom_creator_id_2a6d4ec9_fk_AuthUser_user_id` (`creator_id`),
  CONSTRAINT `Classroom_classroom_creator_id_2a6d4ec9_fk_AuthUser_user_id` FOREIGN KEY (`creator_id`) REFERENCES `AuthUser_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Classroom_classroom`
--

/*!40000 ALTER TABLE `Classroom_classroom` DISABLE KEYS */;
INSERT INTO `Classroom_classroom` VALUES (3,'DBMS','1ee9853','2018-10-16 06:20:01.468898',1,13,'default_classroom_image.png','It is a great course to learn DBMS concepts.'),(4,'AI','0f3c2f4','2018-10-16 06:20:29.471488',1,12,'default_classroom_image.png','It is a great course to learn AI concepts.'),(5,'ASE-II','ASE-IIa043c','2018-10-21 15:18:35.599581',1,13,'default_classroom_image.png',''),(6,'ASE-I','ASE-I0b5be','2018-10-21 15:21:52.417240',1,13,'default_classroom_image.png','ASE classroom for monsoon 2018.');
/*!40000 ALTER TABLE `Classroom_classroom` ENABLE KEYS */;
 

--
-- Table structure for table `Classroom_classroom_moderators`
--

DROP TABLE IF EXISTS `Classroom_classroom_moderators`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Classroom_classroom_moderators` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `classroom_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Classroom_classroom_mode_classroom_id_user_id_0f735bff_uniq` (`classroom_id`,`user_id`),
  KEY `Classroom_classroom__user_id_73c47636_fk_AuthUser_` (`user_id`),
  CONSTRAINT `Classroom_classroom__classroom_id_9e420406_fk_Classroom` FOREIGN KEY (`classroom_id`) REFERENCES `Classroom_classroom` (`id`),
  CONSTRAINT `Classroom_classroom__user_id_73c47636_fk_AuthUser_` FOREIGN KEY (`user_id`) REFERENCES `AuthUser_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Classroom_classroom_moderators`
--


/*!40000 ALTER TABLE `Classroom_classroom_moderators` DISABLE KEYS */;
INSERT INTO `Classroom_classroom_moderators` VALUES (12,3,8),(9,3,9),(5,3,10),(11,3,13),(6,4,8),(7,4,15);
/*!40000 ALTER TABLE `Classroom_classroom_moderators` ENABLE KEYS */;
 

--
-- Table structure for table `Classroom_classroom_students`
--

DROP TABLE IF EXISTS `Classroom_classroom_students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Classroom_classroom_students` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `classroom_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Classroom_classroom_students_classroom_id_user_id_9b2340e4_uniq` (`classroom_id`,`user_id`),
  KEY `Classroom_classroom__user_id_be7f0e7d_fk_AuthUser_` (`user_id`),
  CONSTRAINT `Classroom_classroom__classroom_id_b05ed3e1_fk_Classroom` FOREIGN KEY (`classroom_id`) REFERENCES `Classroom_classroom` (`id`),
  CONSTRAINT `Classroom_classroom__user_id_be7f0e7d_fk_AuthUser_` FOREIGN KEY (`user_id`) REFERENCES `AuthUser_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Classroom_classroom_students`
--


/*!40000 ALTER TABLE `Classroom_classroom_students` DISABLE KEYS */;
INSERT INTO `Classroom_classroom_students` VALUES (6,3,8),(7,3,11),(16,3,13),(8,3,15),(9,3,16),(10,3,17),(11,4,9),(12,4,10),(13,4,11),(14,4,16),(15,4,17),(17,6,15);
/*!40000 ALTER TABLE `Classroom_classroom_students` ENABLE KEYS */;
 

--
-- Table structure for table `Comment_comment`
--

DROP TABLE IF EXISTS `Comment_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Comment_comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `parent_id` int(11) DEFAULT NULL,
  `comment_text` longtext NOT NULL,
  `commenter_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Comment_comment_commenter_id_98ac5e4e_fk_AuthUser_user_id` (`commenter_id`),
  KEY `Comment_comment_parent_id_dbda7c7f_fk_Comment_comment_id` (`parent_id`),
  CONSTRAINT `Comment_comment_commenter_id_98ac5e4e_fk_AuthUser_user_id` FOREIGN KEY (`commenter_id`) REFERENCES `AuthUser_user` (`id`),
  CONSTRAINT `Comment_comment_parent_id_dbda7c7f_fk_Comment_comment_id` FOREIGN KEY (`parent_id`) REFERENCES `Comment_comment` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Comment_comment`
--


/*!40000 ALTER TABLE `Comment_comment` DISABLE KEYS */;
INSERT INTO `Comment_comment` VALUES (1,'2018-10-16 06:42:11.459634',NULL,'Thank You Ma\'am',8),(2,'2018-10-16 06:42:40.436969',1,'OK',9),(3,'2018-10-16 06:43:44.593242',NULL,'testing',10),(4,'2018-10-21 17:49:44.258562',NULL,'hello',9),(5,'2018-10-21 17:50:34.939059',NULL,'hello hi',9),(6,'2018-10-23 16:45:44.602452',NULL,'test text :-)',15),(7,'2018-10-24 20:24:08.455670',NULL,'test comment',15),(8,'2018-10-24 20:26:35.995122',NULL,'hey hey :-(',15),(9,'2018-10-24 20:28:44.717460',NULL,'text comment',15),(10,'2018-10-24 20:31:28.856071',NULL,'null comment',15),(11,'2018-10-24 20:35:18.547440',NULL,'hello kitty',15),(12,'2018-10-24 20:36:50.758052',NULL,'thanks :-)',15),(13,'2018-10-24 20:50:54.231127',NULL,'',15),(14,'2018-10-24 20:52:31.025705',NULL,'Bhai Bhai Bhai..',15),(15,'2018-10-24 20:53:20.120613',NULL,'hello anurag',15),(16,'2018-10-24 20:54:54.362696',NULL,'hi I am here',15),(17,'2018-10-24 20:55:54.485995',NULL,'last test',15),(18,'2018-10-25 18:17:59.636984',NULL,'Garvit hello',15);
/*!40000 ALTER TABLE `Comment_comment` ENABLE KEYS */;
 

--
-- Table structure for table `Comment_comment_downvoters`
--

DROP TABLE IF EXISTS `Comment_comment_downvoters`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Comment_comment_downvoters` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `comment_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Comment_comment_downvoters_comment_id_user_id_9eb943d2_uniq` (`comment_id`,`user_id`),
  KEY `Comment_comment_downvoters_user_id_829229e8_fk_AuthUser_user_id` (`user_id`),
  CONSTRAINT `Comment_comment_down_comment_id_4a22ea83_fk_Comment_c` FOREIGN KEY (`comment_id`) REFERENCES `Comment_comment` (`id`),
  CONSTRAINT `Comment_comment_downvoters_user_id_829229e8_fk_AuthUser_user_id` FOREIGN KEY (`user_id`) REFERENCES `AuthUser_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Comment_comment_downvoters`
--


/*!40000 ALTER TABLE `Comment_comment_downvoters` DISABLE KEYS */;
INSERT INTO `Comment_comment_downvoters` VALUES (1,1,16),(2,1,17),(3,2,16),(4,2,17),(5,3,9),(15,3,15),(31,4,13),(16,4,15),(25,5,13),(13,6,13),(29,8,15),(18,9,15),(23,11,13),(30,17,15);
/*!40000 ALTER TABLE `Comment_comment_downvoters` ENABLE KEYS */;
 

--
-- Table structure for table `Comment_comment_upvoters`
--

DROP TABLE IF EXISTS `Comment_comment_upvoters`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Comment_comment_upvoters` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `comment_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Comment_comment_upvoters_comment_id_user_id_45e7e97f_uniq` (`comment_id`,`user_id`),
  KEY `Comment_comment_upvoters_user_id_5cba8cbf_fk_AuthUser_user_id` (`user_id`),
  CONSTRAINT `Comment_comment_upvo_comment_id_907ed9d2_fk_Comment_c` FOREIGN KEY (`comment_id`) REFERENCES `Comment_comment` (`id`),
  CONSTRAINT `Comment_comment_upvoters_user_id_5cba8cbf_fk_AuthUser_user_id` FOREIGN KEY (`user_id`) REFERENCES `AuthUser_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Comment_comment_upvoters`
--


/*!40000 ALTER TABLE `Comment_comment_upvoters` DISABLE KEYS */;
INSERT INTO `Comment_comment_upvoters` VALUES (1,1,9),(2,1,10),(39,1,13),(21,1,15),(3,2,10),(4,2,11),(37,2,13),(23,2,15),(5,3,8),(38,3,13),(22,5,15),(18,6,15),(25,7,15),(26,10,15),(27,11,15),(28,12,15),(34,15,15);
/*!40000 ALTER TABLE `Comment_comment_upvoters` ENABLE KEYS */;
 

--
-- Table structure for table `Notifications_notification`
--

DROP TABLE IF EXISTS `Notifications_notification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Notifications_notification` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `text` varchar(250) DEFAULT NULL,
  `notification_type` varchar(5) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `actor_id` int(11) NOT NULL,
  `receiver_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Notifications_notification_actor_id_8a420ccc_fk_AuthUser_user_id` (`actor_id`),
  KEY `Notifications_notifi_receiver_id_e7b8d54c_fk_AuthUser_` (`receiver_id`),
  CONSTRAINT `Notifications_notifi_receiver_id_e7b8d54c_fk_AuthUser_` FOREIGN KEY (`receiver_id`) REFERENCES `AuthUser_user` (`id`),
  CONSTRAINT `Notifications_notification_actor_id_8a420ccc_fk_AuthUser_user_id` FOREIGN KEY (`actor_id`) REFERENCES `AuthUser_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Notifications_notification`
--


/*!40000 ALTER TABLE `Notifications_notification` DISABLE KEYS */;
/*!40000 ALTER TABLE `Notifications_notification` ENABLE KEYS */;
 

--
-- Table structure for table `PollResponse_pollresponse`
--

DROP TABLE IF EXISTS `PollResponse_pollresponse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PollResponse_pollresponse` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `poll_id` int(11) NOT NULL,
  `poll_option_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `PollResponse_pollresponse_poll_id_dee5b70f_fk_Polls_poll_id` (`poll_id`),
  KEY `PollResponse_pollres_poll_option_id_36d6d685_fk_Polls_pol` (`poll_option_id`),
  KEY `PollResponse_pollresponse_user_id_1b3319a1_fk_AuthUser_user_id` (`user_id`),
  CONSTRAINT `PollResponse_pollres_poll_option_id_36d6d685_fk_Polls_pol` FOREIGN KEY (`poll_option_id`) REFERENCES `Polls_polloption` (`id`),
  CONSTRAINT `PollResponse_pollresponse_poll_id_dee5b70f_fk_Polls_poll_id` FOREIGN KEY (`poll_id`) REFERENCES `Polls_poll` (`id`),
  CONSTRAINT `PollResponse_pollresponse_user_id_1b3319a1_fk_AuthUser_user_id` FOREIGN KEY (`user_id`) REFERENCES `AuthUser_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PollResponse_pollresponse`
--


/*!40000 ALTER TABLE `PollResponse_pollresponse` DISABLE KEYS */;
INSERT INTO `PollResponse_pollresponse` VALUES (7,'2018-10-21 18:44:32.452134',9,9,13),(10,'2018-10-25 20:14:04.053623',10,10,8),(11,'2018-10-25 20:14:21.722309',10,11,16),(12,'2018-10-25 20:14:43.183335',10,10,9),(13,'2018-10-25 20:14:58.827864',10,13,17),(14,'2018-10-25 20:16:24.060918',9,9,17),(15,'2018-10-25 20:17:12.090659',9,8,8);
/*!40000 ALTER TABLE `PollResponse_pollresponse` ENABLE KEYS */;
 

--
-- Table structure for table `Polls_poll`
--

DROP TABLE IF EXISTS `Polls_poll`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Polls_poll` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `poll_text` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `classroom_id` int(11) DEFAULT NULL,
  `creater_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Polls_poll_classroom_id_290f8457_fk_Classroom_classroom_id` (`classroom_id`),
  KEY `Polls_poll_creater_id_b58e1435_fk_AuthUser_user_id` (`creater_id`),
  CONSTRAINT `Polls_poll_classroom_id_290f8457_fk_Classroom_classroom_id` FOREIGN KEY (`classroom_id`) REFERENCES `Classroom_classroom` (`id`),
  CONSTRAINT `Polls_poll_creater_id_b58e1435_fk_AuthUser_user_id` FOREIGN KEY (`creater_id`) REFERENCES `AuthUser_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Polls_poll`
--


/*!40000 ALTER TABLE `Polls_poll` DISABLE KEYS */;
INSERT INTO `Polls_poll` VALUES (9,'Should Anurag be failed in mid-term?','2018-10-21 17:25:52.583763',3,13),(10,'Which is the best car?','2018-10-25 20:12:46.724536',3,13);
/*!40000 ALTER TABLE `Polls_poll` ENABLE KEYS */;
 

--
-- Table structure for table `Polls_polloption`
--

DROP TABLE IF EXISTS `Polls_polloption`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Polls_polloption` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `option_text` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `parrent_poll_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Polls_polloption_parrent_poll_id_498ce52f_fk_Polls_poll_id` (`parrent_poll_id`),
  CONSTRAINT `Polls_polloption_parrent_poll_id_498ce52f_fk_Polls_poll_id` FOREIGN KEY (`parrent_poll_id`) REFERENCES `Polls_poll` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Polls_polloption`
--

/*!40000 ALTER TABLE `Polls_polloption` DISABLE KEYS */;
INSERT INTO `Polls_polloption` VALUES (8,'YES','2018-10-21 17:25:52.847410',9),(9,'NO','2018-10-21 17:25:53.088615',9),(10,'Swift','2018-10-25 20:12:46.944964',10),(11,'Verna','2018-10-25 20:12:47.309568',10),(12,'Safari','2018-10-25 20:12:47.849569',10),(13,'XUV 500','2018-10-25 20:12:47.986871',10);
/*!40000 ALTER TABLE `Polls_polloption` ENABLE KEYS */;
 

--
-- Table structure for table `Resources_resource`
--

DROP TABLE IF EXISTS `Resources_resource`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Resources_resource` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `attachment` varchar(100) DEFAULT NULL,
  `description` varchar(300) DEFAULT NULL,
  `uploaded_on` datetime(6) NOT NULL,
  `is_lecture` tinyint(1) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `classroom_id` int(11) NOT NULL,
  `uploader_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Resources_resource_classroom_id_9f1c088f_fk_Classroom` (`classroom_id`),
  KEY `Resources_resource_uploader_id_fd66e751_fk_AuthUser_user_id` (`uploader_id`),
  CONSTRAINT `Resources_resource_classroom_id_9f1c088f_fk_Classroom` FOREIGN KEY (`classroom_id`) REFERENCES `Classroom_classroom` (`id`),
  CONSTRAINT `Resources_resource_uploader_id_fd66e751_fk_AuthUser_user_id` FOREIGN KEY (`uploader_id`) REFERENCES `AuthUser_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Resources_resource`
--


/*!40000 ALTER TABLE `Resources_resource` DISABLE KEYS */;
INSERT INTO `Resources_resource` VALUES (1,'Resources/3_DBMS/UMA','Test description','2018-10-21 17:31:05.561170',1,0,3,13),(2,'Resources/3_DBMS/sanyem','Moderator','2018-10-21 17:34:04.408699',0,0,3,9),(3,'Resources/3_DBMS/UMA_NNTrWV5','Hello','2018-10-22 10:51:11.019179',1,0,3,13),(4,'','Yada yada','2018-10-22 11:38:14.023210',1,0,3,13),(5,'Resources/3_DBMS/UMA_24wzvX5','ffhjfhbjfhbhjfbf','2018-10-22 11:41:23.986367',1,0,3,13),(6,'Resources/3_DBMS/UMA_GGodRU6','','2018-10-22 11:45:21.812508',1,0,3,13),(7,'Resources/3_DBMS/UMA_ZvS5UVF','Lor','2018-10-22 11:49:04.111611',1,0,3,13),(8,'Resources/3_DBMS/UMA_vUIMVM0','Loremmmmmmm .  hjhjbjhbjhbjh','2018-10-22 11:50:24.898242',1,0,3,13),(9,'Resources/3_DBMS/UMA_vwzsoLm','Just a test to see if it is working. If working then great.','2018-10-22 13:16:21.113816',0,0,3,13),(10,'Resources/3_DBMS/uday','Thesis based on DBMS for music indexing','2018-10-22 13:18:58.238897',0,0,3,11),(11,'Resources/3_DBMS/UMA_R8rrBma','','2018-10-22 20:43:55.269333',1,0,3,13),(12,'Resources/3_DBMS/UMA_YpZECGw','','2018-10-22 20:44:27.352152',1,0,3,13),(13,'Resources/3_DBMS/UMA_ENcTzt4','2018-10-24T22:00','2018-10-22 20:44:42.650693',1,0,3,13);
/*!40000 ALTER TABLE `Resources_resource` ENABLE KEYS */;
 

--
-- Table structure for table `Resources_resource_comments`
--

DROP TABLE IF EXISTS `Resources_resource_comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Resources_resource_comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `resource_id` int(11) NOT NULL,
  `comment_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Resources_resource_comments_resource_id_comment_id_1fceea58_uniq` (`resource_id`,`comment_id`),
  KEY `Resources_resource_c_comment_id_adeab51a_fk_Comment_c` (`comment_id`),
  CONSTRAINT `Resources_resource_c_comment_id_adeab51a_fk_Comment_c` FOREIGN KEY (`comment_id`) REFERENCES `Comment_comment` (`id`),
  CONSTRAINT `Resources_resource_c_resource_id_dba050a9_fk_Resources` FOREIGN KEY (`resource_id`) REFERENCES `Resources_resource` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Resources_resource_comments`
--


/*!40000 ALTER TABLE `Resources_resource_comments` DISABLE KEYS */;
/*!40000 ALTER TABLE `Resources_resource_comments` ENABLE KEYS */;
 

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--


/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
 

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--


/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
 

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--


/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add user',6,'add_user'),(22,'Can change user',6,'change_user'),(23,'Can delete user',6,'delete_user'),(24,'Can view user',6,'view_user'),(25,'Can add classroom',7,'add_classroom'),(26,'Can change classroom',7,'change_classroom'),(27,'Can delete classroom',7,'delete_classroom'),(28,'Can view classroom',7,'view_classroom'),(29,'Can add comment',8,'add_comment'),(30,'Can change comment',8,'change_comment'),(31,'Can delete comment',8,'delete_comment'),(32,'Can view comment',8,'view_comment'),(33,'Can add announcement',9,'add_announcement'),(34,'Can change announcement',9,'change_announcement'),(35,'Can delete announcement',9,'delete_announcement'),(36,'Can view announcement',9,'view_announcement'),(37,'Can add assignment',10,'add_assignment'),(38,'Can change assignment',10,'change_assignment'),(39,'Can delete assignment',10,'delete_assignment'),(40,'Can view assignment',10,'view_assignment'),(41,'Can add submission',11,'add_submission'),(42,'Can change submission',11,'change_submission'),(43,'Can delete submission',11,'delete_submission'),(44,'Can view submission',11,'view_submission'),(45,'Can add poll',12,'add_poll'),(46,'Can change poll',12,'change_poll'),(47,'Can delete poll',12,'delete_poll'),(48,'Can view poll',12,'view_poll'),(49,'Can add poll option',13,'add_polloption'),(50,'Can change poll option',13,'change_polloption'),(51,'Can delete poll option',13,'delete_polloption'),(52,'Can view poll option',13,'view_polloption'),(53,'Can add resource',14,'add_resource'),(54,'Can change resource',14,'change_resource'),(55,'Can delete resource',14,'delete_resource'),(56,'Can view resource',14,'view_resource'),(57,'Can add poll response',15,'add_pollresponse'),(58,'Can change poll response',15,'change_pollresponse'),(59,'Can delete poll response',15,'delete_pollresponse'),(60,'Can view poll response',15,'view_pollresponse'),(61,'Can add notification',16,'add_notification'),(62,'Can change notification',16,'change_notification'),(63,'Can delete notification',16,'delete_notification'),(64,'Can view notification',16,'view_notification');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
 

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_AuthUser_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_AuthUser_user_id` FOREIGN KEY (`user_id`) REFERENCES `AuthUser_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2018-10-16 04:56:20.419429','2','garvit',1,'[{\"added\": {}}]',6,1),(2,'2018-10-16 05:02:17.937555','2','garvit',2,'[{\"changed\": {\"fields\": [\"is_faculty\"]}}]',6,1),(3,'2018-10-16 05:31:07.651324','3','anurag',1,'[{\"added\": {}}]',6,1),(4,'2018-10-16 05:31:46.272610','4','sahaj',1,'[{\"added\": {}}]',6,1),(5,'2018-10-16 05:32:19.639940','5','chandu',1,'[{\"added\": {}}]',6,1),(6,'2018-10-16 05:32:53.568559','6','vishvanath',1,'[{\"added\": {}}]',6,1),(7,'2018-10-16 05:33:00.334385','6','vishvanath',2,'[{\"changed\": {\"fields\": [\"is_faculty\"]}}]',6,1),(8,'2018-10-16 05:33:24.382673','7','UMA',1,'[{\"added\": {}}]',6,1),(9,'2018-10-16 05:33:33.488939','7','UMA',2,'[{\"changed\": {\"fields\": [\"is_faculty\"]}}]',6,1),(10,'2018-10-16 05:34:25.412929','1','DBMS -- UMA -- 2018-10-16 05:34:25.394021+00:00 -- True',1,'[{\"added\": {}}]',7,1),(11,'2018-10-16 05:35:09.810460','2','AI -- vishvanath -- 2018-10-16 05:35:09.793831+00:00 -- True',1,'[{\"added\": {}}]',7,1),(12,'2018-10-16 05:35:29.941015','2','AI -- vishvanath -- 2018-10-16 05:35:09.793831+00:00 -- True',2,'[{\"changed\": {\"fields\": [\"moderators\"]}}]',7,1),(13,'2018-10-16 06:16:46.713011','4','sahaj',3,'',6,1),(14,'2018-10-16 06:17:20.068575','7','UMA',3,'',6,1),(15,'2018-10-16 06:17:20.076160','6','vishvanath',3,'',6,1),(16,'2018-10-16 06:17:20.085050','5','chandu',3,'',6,1),(17,'2018-10-16 06:17:20.094353','3','anurag',3,'',6,1),(18,'2018-10-16 06:17:20.105450','2','garvit',3,'',6,1),(19,'2018-10-16 06:18:26.117406','14','test',1,'[{\"added\": {}}]',6,1),(20,'2018-10-16 06:18:41.439845','14','test',3,'',6,1),(21,'2018-10-16 06:20:01.487372','3','DBMS -- UMA -- 2018-10-16 06:20:01.468898+00:00 -- True',1,'[{\"added\": {}}]',7,1),(22,'2018-10-16 06:20:29.489618','4','AI -- Vishvanath -- 2018-10-16 06:20:29.471488+00:00 -- True',1,'[{\"added\": {}}]',7,1),(23,'2018-10-16 06:42:11.471840','1','anubhav -- 2018-10-16 06:42:11.459634+00:00',1,'[{\"added\": {}}]',8,1),(24,'2018-10-16 06:42:40.455127','2','sanyem -- 2018-10-16 06:42:40.436969+00:00',1,'[{\"added\": {}}]',8,1),(25,'2018-10-16 06:43:44.605502','3','bhavi -- 2018-10-16 06:43:44.593242+00:00',1,'[{\"added\": {}}]',8,1),(26,'2018-10-16 06:43:53.063812','1','UMA -- 2018-10-16 06:43:53.055345+00:00',1,'[{\"added\": {}}]',9,1),(27,'2018-10-16 06:46:48.955522','3','DBMS -- UMA -- 2018-10-16 06:20:01.468898+00:00 -- True',2,'[{\"changed\": {\"fields\": [\"students\"]}}]',7,1),(28,'2018-10-16 14:55:29.265240','3','DBMS -- UMA -- 2018-10-16 06:20:01.468898+00:00 -- True',2,'[{\"changed\": {\"fields\": [\"description\"]}}]',7,1),(29,'2018-10-16 14:55:40.774529','4','AI -- Vishvanath -- 2018-10-16 06:20:29.471488+00:00 -- True',2,'[{\"changed\": {\"fields\": [\"description\"]}}]',7,1),(30,'2018-10-21 08:26:18.008150','1','UMA -- 2018-10-21 08:26:18.006895+00:00',1,'[{\"added\": {}}]',12,1),(31,'2018-10-21 08:44:00.617082','1','Verna -- 2018-10-21 08:44:00.616241+00:00',1,'[{\"added\": {}}]',13,1),(32,'2018-10-21 08:44:12.707257','2','Safari -- 2018-10-21 08:44:12.706309+00:00',1,'[{\"added\": {}}]',13,1),(33,'2018-10-21 08:44:23.859006','3','XUV -- 2018-10-21 08:44:23.858184+00:00',1,'[{\"added\": {}}]',13,1),(34,'2018-10-21 15:46:40.325212','2','Kinfolk waistcoat occupy cred. Tacos bicycle rights jean shorts craft beer letterpress, banjo post-ironic activated charcoal lomo wolf. Hell of kombucha biodiesel, direct trade listicle hexagon mixtap',3,'',14,1),(35,'2018-10-23 17:33:31.321061','6','anurag -- 2018-10-23 16:45:44.602452+00:00',2,'[{\"changed\": {\"fields\": [\"comment_text\", \"upvoters\", \"downvoters\"]}}]',8,1),(36,'2018-10-24 18:18:41.511708','4','UMA -- 2018-10-24 18:18:40.877153+00:00',1,'[{\"added\": {}}]',9,1),(37,'2018-10-24 18:24:09.763686','5','5---UMA -- 2018-10-24 18:24:09.441212+00:00',1,'[{\"added\": {}}]',9,1),(38,'2018-10-24 18:26:06.355650','6','6---UMA -- 2018-10-24 18:26:05.961156+00:00',1,'[{\"added\": {}}]',9,1),(39,'2018-10-24 18:27:05.209610','7','7---UMA -- 2018-10-24 18:27:04.894957+00:00',1,'[{\"added\": {}}]',9,1),(40,'2018-10-24 18:28:20.261243','8','8---UMA -- 2018-10-24 18:28:19.929748+00:00',1,'[{\"added\": {}}]',9,1),(41,'2018-10-25 20:14:04.054535','10','Which is the best car? -- Swift -- 2018-10-25 20:14:04.053623+00:00',1,'[{\"added\": {}}]',15,1),(42,'2018-10-25 20:14:21.723333','11','Which is the best car? -- Verna -- 2018-10-25 20:14:21.722309+00:00',1,'[{\"added\": {}}]',15,1),(43,'2018-10-25 20:14:43.184216','12','Which is the best car? -- Swift -- 2018-10-25 20:14:43.183335+00:00',1,'[{\"added\": {}}]',15,1),(44,'2018-10-25 20:14:58.829018','13','Which is the best car? -- XUV 500 -- 2018-10-25 20:14:58.827864+00:00',1,'[{\"added\": {}}]',15,1),(45,'2018-10-25 20:16:24.061969','14','Should Anurag be failed in mid-term? -- NO -- 2018-10-25 20:16:24.060918+00:00',1,'[{\"added\": {}}]',15,1),(46,'2018-10-25 20:17:12.091560','15','Should Anurag be failed in mid-term? -- YES -- 2018-10-25 20:17:12.090659+00:00',1,'[{\"added\": {}}]',15,1),(47,'2018-10-25 20:21:02.323648','5','UMA -- Bonus Task 1',2,'[{\"changed\": {\"fields\": [\"title\", \"comments\"]}}]',10,1),(48,'2018-10-25 20:43:49.086366','3','3---UMA -- 2018-10-21 09:45:34.379649+00:00',3,'',9,1),(49,'2018-10-25 20:43:49.092915','2','2---UMA -- 2018-10-16 06:48:56.802261+00:00',3,'',9,1),(50,'2018-10-25 20:44:34.821634','9','9---UMA -- 2018-10-25 20:44:34.816082+00:00',1,'[{\"added\": {}}]',9,1),(51,'2018-10-25 20:55:10.152083','4','anurag -- Bonus task 6',1,'[{\"added\": {}}]',11,1),(52,'2018-10-25 20:58:54.784230','15','anurag',2,'[{\"changed\": {\"fields\": [\"is_faculty\"]}}]',6,1),(53,'2018-10-25 21:03:59.699596','3','DBMS -- UMA -- 2018-10-16 06:20:01.468898+00:00 -- True',2,'[{\"changed\": {\"fields\": [\"moderators\"]}}]',7,1),(54,'2018-10-25 21:17:17.109659','6','sahaj -- Bonus Task 5',3,'',11,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
 

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--


/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(9,'Announcement','announcement'),(10,'Assignment','assignment'),(11,'Assignment','submission'),(3,'auth','group'),(2,'auth','permission'),(6,'AuthUser','user'),(7,'Classroom','classroom'),(8,'Comment','comment'),(4,'contenttypes','contenttype'),(16,'Notifications','notification'),(15,'PollResponse','pollresponse'),(12,'Polls','poll'),(13,'Polls','polloption'),(14,'Resources','resource'),(5,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
 

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--


/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-10-25 11:24:12.641981'),(2,'contenttypes','0002_remove_content_type_name','2018-10-25 11:24:12.708414'),(3,'auth','0001_initial','2018-10-25 11:24:12.905543'),(4,'auth','0002_alter_permission_name_max_length','2018-10-25 11:24:12.924413'),(5,'auth','0003_alter_user_email_max_length','2018-10-25 11:24:12.935747'),(6,'auth','0004_alter_user_username_opts','2018-10-25 11:24:12.947302'),(7,'auth','0005_alter_user_last_login_null','2018-10-25 11:24:12.958296'),(8,'auth','0006_require_contenttypes_0002','2018-10-25 11:24:12.963879'),(9,'auth','0007_alter_validators_add_error_messages','2018-10-25 11:24:12.975166'),(10,'auth','0008_alter_user_username_max_length','2018-10-25 11:24:12.986041'),(11,'auth','0009_alter_user_last_name_max_length','2018-10-25 11:24:12.996992'),(12,'AuthUser','0001_initial','2018-10-25 11:24:13.249509'),(13,'Comment','0001_initial','2018-10-25 11:24:13.795264'),(14,'Comment','0002_auto_20181010_1254','2018-10-25 11:24:13.850241'),(15,'Comment','0003_auto_20181010_1255','2018-10-25 11:24:13.905352'),(16,'Comment','0004_remove_comment_commenter','2018-10-25 11:24:13.953590'),(17,'Comment','0005_comment_commenter','2018-10-25 11:24:14.032568'),(18,'Comment','0006_auto_20181010_1348','2018-10-25 11:24:14.057883'),(19,'Comment','0007_auto_20181010_1410','2018-10-25 11:24:14.148468'),(20,'Comment','0008_comment_comment_text','2018-10-25 11:24:14.191331'),(21,'Comment','0009_remove_comment_commenter','2018-10-25 11:24:14.240648'),(22,'Comment','0010_comment_commenter','2018-10-25 11:24:14.315205'),(23,'Comment','0011_auto_20181010_1513','2018-10-25 11:24:14.395113'),(24,'Comment','0012_auto_20181010_1539','2018-10-25 11:24:14.482690'),(25,'Comment','0013_auto_20181011_1025','2018-10-25 11:24:14.540635'),(26,'Classroom','0001_initial','2018-10-25 11:24:14.605945'),(27,'Classroom','0002_classroom_moderators','2018-10-25 11:24:14.714285'),(28,'Classroom','0003_auto_20181010_1127','2018-10-25 11:24:14.921102'),(29,'Announcement','0001_initial','2018-10-25 11:24:15.050393'),(30,'Announcement','0002_remove_announcement_comment','2018-10-25 11:24:15.102488'),(31,'Announcement','0003_announcement_comment','2018-10-25 11:24:15.178711'),(32,'Announcement','0004_announcement_classroom','2018-10-25 11:24:15.265937'),(33,'Announcement','0005_auto_20181011_1230','2018-10-25 11:24:15.426326'),(34,'Announcement','0006_auto_20181017_2140','2018-10-25 11:24:15.486013'),(35,'Comment','0014_auto_20181017_2140','2018-10-25 11:24:15.681820'),(36,'Classroom','0004_auto_20181017_2140','2018-10-25 11:24:16.020322'),(37,'Assignment','0001_initial','2018-10-25 11:24:16.112741'),(38,'Assignment','0002_auto_20181017_2140','2018-10-25 11:24:16.485131'),(39,'Assignment','0003_auto_20181025_1117','2018-10-25 11:24:16.557331'),(40,'AuthUser','0002_user_is_faculty','2018-10-25 11:24:16.609719'),(41,'AuthUser','0003_user_avatar','2018-10-25 11:24:16.664590'),(42,'admin','0001_initial','2018-10-25 11:24:16.765538'),(43,'admin','0002_logentry_remove_auto_add','2018-10-25 11:24:16.789715'),(44,'admin','0003_logentry_add_action_flag_choices','2018-10-25 11:24:16.814528'),(45,'sessions','0001_initial','2018-10-25 11:24:16.852377'),(46,'Notifications','0001_initial','2018-10-25 11:31:37.161255'),(47,'Polls','0001_initial','2018-10-25 11:35:18.346658'),(48,'PollResponse','0001_initial','2018-10-25 11:35:18.378174'),(49,'PollResponse','0002_auto_20181025_1133','2018-10-25 11:35:18.605475'),(50,'Resources','0001_initial','2018-10-25 11:37:39.388116');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
 

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('cnhstrar2aoljqcq2nkxtjaziw8nia7v','NWI3YTVhZTk3YjZlYTc0OWY1YmQwMWVlZGU5NDAxMDE5YTRhYTFiMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzMDhjN2Q2MDg1MDYyN2RhYWUxMGU5Y2IyYmI5MjNlZTQzOTIwZTZmIn0=','2018-11-04 19:42:38.608307'),('d1lctyb31kj2k2t0k0ykt53xyonoo7u3','NWI3YTVhZTk3YjZlYTc0OWY1YmQwMWVlZGU5NDAxMDE5YTRhYTFiMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzMDhjN2Q2MDg1MDYyN2RhYWUxMGU5Y2IyYmI5MjNlZTQzOTIwZTZmIn0=','2018-10-30 04:55:17.263101'),('m1eqvunn2mmpozeagmlkrgo161jk8k41','NWI3YTVhZTk3YjZlYTc0OWY1YmQwMWVlZGU5NDAxMDE5YTRhYTFiMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzMDhjN2Q2MDg1MDYyN2RhYWUxMGU5Y2IyYmI5MjNlZTQzOTIwZTZmIn0=','2018-11-04 15:54:56.863915'),('pzonkazozsg2y5t5axwgoc3ln9wx','NWI3YTVhZTk3YjZlYTc0OWY1YmQwMWVlZGU5NDAxMDE5YTRhYTFiMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzMDhjN2Q2MDg1MDYyN2RhYWUxMGU5Y2IyYmI5MjNlZTQzOTIwZTZmIn0=','2018-11-04 15:33:26.218392'),('t2tig7bsv8hj1htnyg7glk6yz3cyiqn7','NWI3YTVhZTk3YjZlYTc0OWY1YmQwMWVlZGU5NDAxMDE5YTRhYTFiMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzMDhjN2Q2MDg1MDYyN2RhYWUxMGU5Y2IyYmI5MjNlZTQzOTIwZTZmIn0=','2018-11-08 11:30:12.641860'),('umystq50g25i59kjvx8vhtf2no5y92p0','NWI3YTVhZTk3YjZlYTc0OWY1YmQwMWVlZGU5NDAxMDE5YTRhYTFiMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzMDhjN2Q2MDg1MDYyN2RhYWUxMGU5Y2IyYmI5MjNlZTQzOTIwZTZmIn0=','2018-11-06 17:32:52.978618'),('uofcrna339uwzv38uvunldwh1bud75d4','NWI3YTVhZTk3YjZlYTc0OWY1YmQwMWVlZGU5NDAxMDE5YTRhYTFiMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzMDhjN2Q2MDg1MDYyN2RhYWUxMGU5Y2IyYmI5MjNlZTQzOTIwZTZmIn0=','2018-11-07 03:33:29.412465'),('ydy6mpg9rrf7g798y6lymi08ipmh2ley','NWI3YTVhZTk3YjZlYTc0OWY1YmQwMWVlZGU5NDAxMDE5YTRhYTFiMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzMDhjN2Q2MDg1MDYyN2RhYWUxMGU5Y2IyYmI5MjNlZTQzOTIwZTZmIn0=','2018-11-04 16:15:47.333490');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
 
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-10-26 12:40:11
