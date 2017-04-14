/*
Navicat MySQL Data Transfer

Source Server         : mysql-练习机
Source Server Version : 50716
Source Host           : 192.168.75.133:3306
Source Database       : oldboy

Target Server Type    : MYSQL
Target Server Version : 50716
File Encoding         : 65001

Date: 2017-04-14 14:42:38
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for admin
-- ----------------------------
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of admin
-- ----------------------------
INSERT INTO `admin` VALUES ('1', 'zhang', 'zhang');
INSERT INTO `admin` VALUES ('2', 'pan', 'pan');
INSERT INTO `admin` VALUES ('3', 'guan', 'guan');

-- ----------------------------
-- Table structure for content
-- ----------------------------
DROP TABLE IF EXISTS `content`;
CREATE TABLE `content` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `content` varchar(255) DEFAULT NULL,
  `media_id` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of content
-- ----------------------------

-- ----------------------------
-- Table structure for media
-- ----------------------------
DROP TABLE IF EXISTS `media`;
CREATE TABLE `media` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `address` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of media
-- ----------------------------
INSERT INTO `media` VALUES ('1', 'usr/local/bin');

-- ----------------------------
-- Table structure for Userinfo
-- ----------------------------
DROP TABLE IF EXISTS `Userinfo`;
CREATE TABLE `Userinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of Userinfo
-- ----------------------------
INSERT INTO `Userinfo` VALUES ('1', 'zhang', 'ruzhou');
INSERT INTO `Userinfo` VALUES ('2', 'pan', 'xinyang');
INSERT INTO `Userinfo` VALUES ('6', 'shao', 'shangqiu');
INSERT INTO `Userinfo` VALUES ('7', 'guan', 'shangqiu');
INSERT INTO `Userinfo` VALUES ('8', 'liu', 'zhoukou');
INSERT INTO `Userinfo` VALUES ('9', 'guan', 'shangqiu');
INSERT INTO `Userinfo` VALUES ('10', 'guan', 'shangqiu');
INSERT INTO `Userinfo` VALUES ('11', 'liu', 'zhoukou');
INSERT INTO `Userinfo` VALUES ('12', 'guan', 'shangqiu');
