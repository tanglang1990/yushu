CREATE DATABASE  IF NOT EXISTS `demo01`  DEFAULT CHARACTER SET utf8mb4 ;

USE `demo01`;

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `username` VARCHAR(64)  DEFAULT NULL COMMENT '姓名',
  `age` INT(11) DEFAULT NULL COMMENT '年龄',
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `id` (`id`)
);

/*Data for the table `user` */

INSERT  INTO `user`(`id`,`username`,`age`) VALUES (1,'ten',18),(2,'gavin',17),(3,'本老师',16);
