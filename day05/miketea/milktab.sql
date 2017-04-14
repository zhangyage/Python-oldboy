/*
Navicat MySQL Data Transfer

Source Server         : mysql-练习机
Source Server Version : 50716
Source Host           : 192.168.75.133:3306
Source Database       : milktab

Target Server Type    : MYSQL
Target Server Version : 50716
File Encoding         : 65001

Date: 2017-04-14 16:39:26
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for chatrecord
-- ----------------------------
DROP TABLE IF EXISTS `chatrecord`;
CREATE TABLE `chatrecord` (
  `Nid` int(11) NOT NULL AUTO_INCREMENT,
  `Message` varchar(255) DEFAULT NULL,
  `Date` datetime DEFAULT NULL,
  `UserId` int(11) DEFAULT NULL,
  PRIMARY KEY (`Nid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of chatrecord
-- ----------------------------

-- ----------------------------
-- Table structure for userinfo
-- ----------------------------
DROP TABLE IF EXISTS `userinfo`;
CREATE TABLE `userinfo` (
  `Nid` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(255) DEFAULT NULL,
  `Password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Nid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of userinfo
-- ----------------------------
