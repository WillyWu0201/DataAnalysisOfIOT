-- --------------------------------------------------------
-- 主機:                           140.120.13.188
-- 服務器版本:                        5.6.16 - MySQL Community Server (GPL)
-- 服務器操作系統:                      Win32
-- HeidiSQL 版本:                  8.3.0.4694
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- 導出 product 的資料庫結構
CREATE DATABASE IF NOT EXISTS `product` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `product`;


-- 導出  表 product.books 結構
CREATE TABLE IF NOT EXISTS `books` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` text,
  `price` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

-- 正在導出表  product.books 的資料：~12 rows (大約)
DELETE FROM `books`;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` (`id`, `name`, `price`) VALUES
	(1, 'Android', 400),
	(2, 'PHP', 280),
	(3, 'jQuery', 360),
	(4, 'C++', 240),
	(5, 'C#', 360),
	(6, 'Matlab', 400),
	(7, 'Python', 280),
	(8, 'Java', 368),
	(9, 'Arduino', 304),
	(10, 'HTML', 384),
	(11, 'ASP', 360),
	(12, 'Hadoop', 256);
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
testtomoto