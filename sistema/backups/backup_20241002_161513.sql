-- MariaDB dump 10.19  Distrib 10.4.32-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: prueba00
-- ------------------------------------------------------
-- Server version	8.0.30

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
-- Table structure for table `administrador`
--

DROP TABLE IF EXISTS `administrador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `administrador` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `tipo_documento` varchar(3) NOT NULL,
  `numero_documento` int unsigned NOT NULL,
  `telefono` int unsigned NOT NULL,
  `contrasena` varchar(128) NOT NULL,
  `conf_contrasena` varchar(128) NOT NULL,
  `user_id` int NOT NULL,
  `activado` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `numero_documento` (`numero_documento`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `administrador_user_id_fc435e22_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `administrador_chk_1` CHECK ((`numero_documento` >= 0)),
  CONSTRAINT `administrador_chk_2` CHECK ((`telefono` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administrador`
--

LOCK TABLES `administrador` WRITE;
/*!40000 ALTER TABLE `administrador` DISABLE KEYS */;
INSERT INTO `administrador` VALUES (3,'CC',1055226143,3138089907,'','',4,1);
/*!40000 ALTER TABLE `administrador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add categoria',7,'add_categoria'),(26,'Can change categoria',7,'change_categoria'),(27,'Can delete categoria',7,'delete_categoria'),(28,'Can view categoria',7,'view_categoria'),(29,'Can add marca',8,'add_marca'),(30,'Can change marca',8,'change_marca'),(31,'Can delete marca',8,'delete_marca'),(32,'Can view marca',8,'view_marca'),(33,'Can add unidad medida',9,'add_unidadmedida'),(34,'Can change unidad medida',9,'change_unidadmedida'),(35,'Can delete unidad medida',9,'delete_unidadmedida'),(36,'Can view unidad medida',9,'view_unidadmedida'),(37,'Can add presentacion',10,'add_presentacion'),(38,'Can change presentacion',10,'change_presentacion'),(39,'Can delete presentacion',10,'delete_presentacion'),(40,'Can view presentacion',10,'view_presentacion'),(41,'Can add producto',11,'add_producto'),(42,'Can change producto',11,'change_producto'),(43,'Can delete producto',11,'delete_producto'),(44,'Can view producto',11,'view_producto'),(45,'Can add compra',12,'add_compra'),(46,'Can change compra',12,'change_compra'),(47,'Can delete compra',12,'delete_compra'),(48,'Can view compra',12,'view_compra'),(49,'Can add venta',13,'add_venta'),(50,'Can change venta',13,'change_venta'),(51,'Can delete venta',13,'delete_venta'),(52,'Can view venta',13,'view_venta'),(53,'Can add proveedor',14,'add_proveedor'),(54,'Can change proveedor',14,'change_proveedor'),(55,'Can delete proveedor',14,'delete_proveedor'),(56,'Can view proveedor',14,'view_proveedor'),(57,'Can add respaldo',15,'add_respaldo'),(58,'Can change respaldo',15,'change_respaldo'),(59,'Can delete respaldo',15,'delete_respaldo'),(60,'Can view respaldo',15,'view_respaldo'),(61,'Can add Administrador',16,'add_administrador'),(62,'Can change Administrador',16,'change_administrador'),(63,'Can delete Administrador',16,'delete_administrador'),(64,'Can view Administrador',16,'view_administrador'),(65,'Can add Empleado',17,'add_empleado'),(66,'Can change Empleado',17,'change_empleado'),(67,'Can delete Empleado',17,'delete_empleado'),(68,'Can view Empleado',17,'view_empleado');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$720000$LxljU9qhw6k0TQqiHSzkFK$AKzlTDBoR0QeEQY3SgsWpw6h3oecTrbkT4AgGlfcUu4=','2024-10-02 19:17:17.069427',1,'admin','','','admin@gmail.com',1,1,'2024-09-30 22:20:58.658124'),(4,'pbkdf2_sha256$720000$PLAPXxbqd2wCi1Of4ygX3U$GeqItxz6OnEo9MXd8vj2C4bLYO2elRXyiSMF3nDhr10=','2024-10-02 21:12:05.294903',1,'Jhon Deivy Alba','','','siganadeivyalba@gmail.com',1,1,'2024-10-02 21:10:11.189753'),(5,'pbkdf2_sha256$720000$S79FaSWgdwxFtkTFQQOeRw$4XYnPiqmphacWEYbMFESyQRdwj+x41p7tEJhwFVo+fc=','2024-10-02 21:11:31.702836',0,'Ximena Barrera','','','xime@gmail.com',0,1,'2024-10-02 21:10:56.101220');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(16,'app','administrador'),(17,'app','empleado'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'libreria','categoria'),(12,'libreria','compra'),(8,'libreria','marca'),(10,'libreria','presentacion'),(11,'libreria','producto'),(14,'libreria','proveedor'),(15,'libreria','respaldo'),(9,'libreria','unidadmedida'),(13,'libreria','venta'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-09-30 22:20:03.733727'),(2,'auth','0001_initial','2024-09-30 22:20:04.065619'),(3,'admin','0001_initial','2024-09-30 22:20:04.161812'),(4,'admin','0002_logentry_remove_auto_add','2024-09-30 22:20:04.167812'),(5,'admin','0003_logentry_add_action_flag_choices','2024-09-30 22:20:04.175705'),(6,'app','0001_initial','2024-09-30 22:20:04.311421'),(7,'app','0002_alter_empleado_telefono','2024-09-30 22:20:04.386961'),(8,'app','0003_remove_administrador_nombre','2024-09-30 22:20:04.402960'),(9,'contenttypes','0002_remove_content_type_name','2024-09-30 22:20:04.494114'),(10,'auth','0002_alter_permission_name_max_length','2024-09-30 22:20:04.541113'),(11,'auth','0003_alter_user_email_max_length','2024-09-30 22:20:04.568119'),(12,'auth','0004_alter_user_username_opts','2024-09-30 22:20:04.576631'),(13,'auth','0005_alter_user_last_login_null','2024-09-30 22:20:04.636632'),(14,'auth','0006_require_contenttypes_0002','2024-09-30 22:20:04.639634'),(15,'auth','0007_alter_validators_add_error_messages','2024-09-30 22:20:04.648633'),(16,'auth','0008_alter_user_username_max_length','2024-09-30 22:20:04.709735'),(17,'auth','0009_alter_user_last_name_max_length','2024-09-30 22:20:04.779254'),(18,'auth','0010_alter_group_name_max_length','2024-09-30 22:20:04.797252'),(19,'auth','0011_update_proxy_permissions','2024-09-30 22:20:04.806252'),(20,'auth','0012_alter_user_first_name_max_length','2024-09-30 22:20:04.861260'),(21,'libreria','0001_initial','2024-09-30 22:20:04.875770'),(22,'libreria','0002_categoria_libro_categoria','2024-09-30 22:20:04.935771'),(23,'libreria','0003_producto','2024-09-30 22:20:04.947771'),(24,'libreria','0004_marca_remove_producto_unidad_de_medida_and_more','2024-09-30 22:20:04.983207'),(25,'libreria','0005_delete_producto_alter_marca_nombre','2024-09-30 22:20:04.996466'),(26,'libreria','0006_unidadmedida_alter_marca_id','2024-09-30 22:20:05.032468'),(27,'libreria','0007_presentacion','2024-09-30 22:20:05.041492'),(28,'libreria','0008_producto','2024-09-30 22:20:05.246908'),(29,'libreria','0009_remove_producto_unidad_medida_producto_unida_medida_and_more','2024-09-30 22:20:05.630140'),(30,'libreria','0010_rename_unida_medida_producto_unidad_medida','2024-09-30 22:20:05.698327'),(31,'libreria','0011_remove_producto_unidad_medida','2024-09-30 22:20:05.746328'),(32,'libreria','0012_producto_unidad_medida','2024-09-30 22:20:05.792898'),(33,'libreria','0013_estado_alter_producto_categoria_alter_producto_marca_and_more','2024-09-30 22:20:06.028802'),(34,'libreria','0014_alter_estado_nombre','2024-09-30 22:20:06.065847'),(35,'libreria','0015_alter_categoria_id_alter_estado_id','2024-09-30 22:20:06.842817'),(36,'libreria','0016_alter_categoria_estado','2024-09-30 22:20:06.848814'),(37,'libreria','0017_alter_categoria_estado','2024-09-30 22:20:06.854814'),(38,'libreria','0018_remove_marca_estado_remove_presentacion_estado_and_more','2024-09-30 22:20:07.059912'),(39,'libreria','0019_marca_estado_presentacion_estado_producto_estado_and_more','2024-09-30 22:20:07.214883'),(40,'libreria','0020_remove_presentacion_estado_remove_marca_estado_and_more','2024-09-30 22:20:07.447279'),(41,'libreria','0021_producto_activo','2024-09-30 22:20:07.468213'),(42,'libreria','0022_categoria_activado','2024-09-30 22:20:07.493757'),(43,'libreria','0023_delete_libro','2024-09-30 22:20:07.500837'),(44,'libreria','0024_marca_activado','2024-09-30 22:20:07.521826'),(45,'libreria','0025_presentacion_activado','2024-09-30 22:20:07.545831'),(46,'libreria','0026_rename_activo_producto_activado_and_more','2024-09-30 22:20:07.584441'),(47,'libreria','0027_compra_persona_venta','2024-09-30 22:20:07.617417'),(48,'libreria','0028_compra_activado_persona_activado_venta_activado','2024-09-30 22:20:07.666289'),(49,'libreria','0029_remove_compra_estado','2024-09-30 22:20:07.674802'),(50,'libreria','0030_remove_persona_estado_remove_venta_estado','2024-09-30 22:20:07.700760'),(51,'libreria','0031_proveedor_respaldo_delete_persona','2024-09-30 22:20:07.777333'),(52,'libreria','0032_producto_proveedor','2024-09-30 22:20:07.841160'),(53,'sessions','0001_initial','2024-09-30 22:20:07.872154'),(54,'app','0004_administrador_activado_and_more','2024-10-02 18:55:16.030152'),(55,'app','0005_empleado_activado_alter_empleado_numero_documento_and_more','2024-10-02 19:17:04.466614');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('bz4zqu9ecishw4vqkbuqnbgevt1ayi89','.eJxVjEEOwiAQRe_C2hBomQ64dO8ZyDAMtmpoUtqV8e7apAvd_vfef6lI2zrGrckSp6zOyqnT75aIH1J3kO9Ub7Pmua7LlPSu6IM2fZ2zPC-H-3cwUhu_NWCwoRfT8SAAxkDCAV3omNEUbxwWTuAJ-j5xsVgGAm_FkjgxaAOp9we9WTdK:1sw6dh:FS4NsoDaWGS7_VD_kpEdu9qhhu7fHe-aPpaAI_KZKOk','2024-10-16 21:12:05.294903'),('z4kcmkgm32mi9e2dchgpovqys9o4mano','.eJxVjEEOwiAQRe_C2pBhQAGX7nsGMjAgVUOT0q6Md7dNutDtf-_9twi0LjWsPc9hZHEVSpx-t0jpmdsO-EHtPsk0tWUeo9wVedAuh4nz63a4fweVet1qk8j7Ui6Ilix6U9gBkNXOagBrHXJSXCAXAK2cSoxkztHErdKIrojPF82TNz8:1sw4YL:x0FEVPGNcBaH2qIPJyN8PhV-TJkO0z72KTmxVTL-A_A','2024-10-16 18:58:25.180866');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `empleado`
--

DROP TABLE IF EXISTS `empleado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `empleado` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `tipo_documento` varchar(3) NOT NULL,
  `numero_documento` bigint unsigned NOT NULL,
  `telefono` varchar(10) NOT NULL,
  `contrasena` varchar(128) NOT NULL,
  `conf_contrasena` varchar(128) NOT NULL,
  `user_id` int NOT NULL,
  `activado` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `numero_documento` (`numero_documento`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `Empleado_user_id_6f1e7e22_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `empleado_chk_1` CHECK ((`numero_documento` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empleado`
--

LOCK TABLES `empleado` WRITE;
/*!40000 ALTER TABLE `empleado` DISABLE KEYS */;
INSERT INTO `empleado` VALUES (1,'','CC',1055228144,'3215635126','Jhon123$','Jhon123$',5,1);
/*!40000 ALTER TABLE `empleado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `libreria_categoria`
--

DROP TABLE IF EXISTS `libreria_categoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `libreria_categoria` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `activado` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `libreria_categoria`
--

LOCK TABLES `libreria_categoria` WRITE;
/*!40000 ALTER TABLE `libreria_categoria` DISABLE KEYS */;
INSERT INTO `libreria_categoria` VALUES (1,'Bebidas',1),(2,'Alimentos',1),(3,'Cuidado personal',1),(4,'Limpieza del hogar',1),(5,'Cosmeticos',1);
/*!40000 ALTER TABLE `libreria_categoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `libreria_compra`
--

DROP TABLE IF EXISTS `libreria_compra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `libreria_compra` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombreproducto` varchar(100) NOT NULL,
  `fechaingreso` date NOT NULL,
  `cantidad` int NOT NULL,
  `valorunitario` decimal(10,2) NOT NULL,
  `valortotal` decimal(10,2) NOT NULL,
  `activado` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `libreria_compra`
--

LOCK TABLES `libreria_compra` WRITE;
/*!40000 ALTER TABLE `libreria_compra` DISABLE KEYS */;
INSERT INTO `libreria_compra` VALUES (1,'Postobon','2024-09-30',4,2500.00,14400.00,1),(2,'Postobon','2024-09-30',2,2500.00,16000.00,1),(3,'Coca Cola','2024-09-30',5,2200.00,11000.00,1),(4,'Postobon','2024-10-08',3,2500.00,7500.00,1),(5,'Jabon Rey','2024-10-02',10,10000.00,40000.00,1);
/*!40000 ALTER TABLE `libreria_compra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `libreria_marca`
--

DROP TABLE IF EXISTS `libreria_marca`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `libreria_marca` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `activado` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `libreria_marca`
--

LOCK TABLES `libreria_marca` WRITE;
/*!40000 ALTER TABLE `libreria_marca` DISABLE KEYS */;
INSERT INTO `libreria_marca` VALUES (1,'Coca Cola',1),(2,'Postobon',1),(3,'Colgate',1),(4,'Nestle',1),(5,'Arroz Diana',1),(6,'Saltin Noel',1),(7,'Doria',1),(8,'Zenú',1),(9,'Roa',1),(10,'Dersa',1);
/*!40000 ALTER TABLE `libreria_marca` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `libreria_presentacion`
--

DROP TABLE IF EXISTS `libreria_presentacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `libreria_presentacion` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `activado` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `libreria_presentacion`
--

LOCK TABLES `libreria_presentacion` WRITE;
/*!40000 ALTER TABLE `libreria_presentacion` DISABLE KEYS */;
INSERT INTO `libreria_presentacion` VALUES (1,'Botella Plastica',1),(2,'Polvo',1),(3,'Barra',1),(4,'Paquete',1),(5,'Lata',1),(6,'Botella Vidrio',1);
/*!40000 ALTER TABLE `libreria_presentacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `libreria_producto`
--

DROP TABLE IF EXISTS `libreria_producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `libreria_producto` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  `categoria_id` int DEFAULT NULL,
  `marca_id` int DEFAULT NULL,
  `presentacion_id` int DEFAULT NULL,
  `unidad_medida_id` int DEFAULT NULL,
  `activado` tinyint(1) NOT NULL,
  `proveedor_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `libreria_producto_marca_id_ba46b2d2_fk_libreria_marca_id` (`marca_id`),
  KEY `libreria_producto_presentacion_id_0c26f4f6_fk_libreria_` (`presentacion_id`),
  KEY `libreria_producto_unidad_medida_id_a77895a9_fk_libreria_` (`unidad_medida_id`),
  KEY `libreria_producto_categoria_id_2d9a6ae2_fk` (`categoria_id`),
  KEY `libreria_producto_proveedor_id_41442a1c_fk_libreria_proveedor_id` (`proveedor_id`),
  CONSTRAINT `libreria_producto_categoria_id_2d9a6ae2_fk` FOREIGN KEY (`categoria_id`) REFERENCES `libreria_categoria` (`id`),
  CONSTRAINT `libreria_producto_marca_id_ba46b2d2_fk_libreria_marca_id` FOREIGN KEY (`marca_id`) REFERENCES `libreria_marca` (`id`),
  CONSTRAINT `libreria_producto_presentacion_id_0c26f4f6_fk_libreria_` FOREIGN KEY (`presentacion_id`) REFERENCES `libreria_presentacion` (`id`),
  CONSTRAINT `libreria_producto_proveedor_id_41442a1c_fk_libreria_proveedor_id` FOREIGN KEY (`proveedor_id`) REFERENCES `libreria_proveedor` (`id`),
  CONSTRAINT `libreria_producto_unidad_medida_id_a77895a9_fk_libreria_` FOREIGN KEY (`unidad_medida_id`) REFERENCES `libreria_unidadmedida` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `libreria_producto`
--

LOCK TABLES `libreria_producto` WRITE;
/*!40000 ALTER TABLE `libreria_producto` DISABLE KEYS */;
INSERT INTO `libreria_producto` VALUES (5,'Coca Cola',2500.00,1,1,1,1,1,1),(6,'Jabon Rey',3000.00,4,10,2,2,1,3),(7,'Cuatro',5000.00,1,1,1,1,1,1);
/*!40000 ALTER TABLE `libreria_producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `libreria_proveedor`
--

DROP TABLE IF EXISTS `libreria_proveedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `libreria_proveedor` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `numero_celular` bigint NOT NULL,
  `correo_electronico` varchar(100) NOT NULL,
  `activado` tinyint(1) NOT NULL,
  `marca_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `libreria_proveedor_marca_id_69b7614e_fk_libreria_marca_id` (`marca_id`),
  CONSTRAINT `libreria_proveedor_marca_id_69b7614e_fk_libreria_marca_id` FOREIGN KEY (`marca_id`) REFERENCES `libreria_marca` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `libreria_proveedor`
--

LOCK TABLES `libreria_proveedor` WRITE;
/*!40000 ALTER TABLE `libreria_proveedor` DISABLE KEYS */;
INSERT INTO `libreria_proveedor` VALUES (1,'Jhon Deivy Alba',3138089907,'asdf@gmail.com',1,1),(3,'Yessica Ximena Barrera',311052884,'xime@gmail.com',1,10);
/*!40000 ALTER TABLE `libreria_proveedor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `libreria_respaldo`
--

DROP TABLE IF EXISTS `libreria_respaldo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `libreria_respaldo` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre_archivo` varchar(255) NOT NULL,
  `fecha_creacion` datetime(6) NOT NULL,
  `tamano` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `libreria_respaldo`
--

LOCK TABLES `libreria_respaldo` WRITE;
/*!40000 ALTER TABLE `libreria_respaldo` DISABLE KEYS */;
/*!40000 ALTER TABLE `libreria_respaldo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `libreria_unidadmedida`
--

DROP TABLE IF EXISTS `libreria_unidadmedida`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `libreria_unidadmedida` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `activado` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `libreria_unidadmedida`
--

LOCK TABLES `libreria_unidadmedida` WRITE;
/*!40000 ALTER TABLE `libreria_unidadmedida` DISABLE KEYS */;
INSERT INTO `libreria_unidadmedida` VALUES (1,'L',1),(2,'Kg',1),(3,'g',1),(4,'ml',1);
/*!40000 ALTER TABLE `libreria_unidadmedida` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `libreria_venta`
--

DROP TABLE IF EXISTS `libreria_venta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `libreria_venta` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombreproducto` varchar(100) NOT NULL,
  `fechaventa` date NOT NULL,
  `cantidad` int NOT NULL,
  `valorunitario` decimal(10,2) NOT NULL,
  `valortotal` decimal(10,2) NOT NULL,
  `activado` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `libreria_venta`
--

LOCK TABLES `libreria_venta` WRITE;
/*!40000 ALTER TABLE `libreria_venta` DISABLE KEYS */;
INSERT INTO `libreria_venta` VALUES (1,'Coca Cola','2024-09-30',5,2200.00,11000.00,0);
/*!40000 ALTER TABLE `libreria_venta` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-02 16:15:13
