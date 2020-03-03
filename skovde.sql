-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Värd: 127.0.0.1:3306
-- Tid vid skapande: 03 mars 2020 kl 21:18
-- Serverversion: 5.7.24
-- PHP-version: 7.2.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Databas: `skovde`
--

-- --------------------------------------------------------

--
-- Tabellstruktur `print`
--

DROP TABLE IF EXISTS `print`;
CREATE TABLE IF NOT EXISTS `print` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` int(1) NOT NULL,
  `created` varchar(20) NOT NULL,
  `backup` int(1) NOT NULL,
  `data` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Dumpning av Data i tabell `print`
--

INSERT INTO `print` (`id`, `type`, `created`, `backup`, `data`) VALUES
(1, 1, '2020-02-26 18:30:20', 0, '{\"adress\": \"Drottning Kristinas Väg 39\",\"lghnr\": \"1021\",\"name\": \"Ludwig Eriksson\",\"phonenumber\": \"0761177269\",\"on_date\": \"2020-02-26\",\"perm_enter\": 1,\"comments\": \"Hela huset håller på att rasa vetetusan vad som händer\"}'),
(2, 2, '2020-02-28 18:30:20', 0, '{\"adress\": \"Slingvägen 16\",\"lghnr\": \"1001\",\"name\": \"Jenny Gustafsson\",\"phonenumber\": \"0763081393\",\"on_date\": \"2020-02-28\",\"perm_enter\": 1,\"comments\": \"Dörren går inte att stänga....\"}'),
(3, 1, '2020-02-28 18:30:20', 0, '{\"adress\": \"Slingvägen 18\",\"lghnr\": \"1021\",\"name\": \"Anders Andersson\",\"phonenumber\": \"07635481393\",\"on_date\": \"2020-02-29\",\"perm_enter\": 1,\"comments\": \"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris congue felis sed libero tempor vehicula. Curabitur ornare est nec ex sodales congue. Mauris dignissim maximus dapibus. Nulla congue finibus eros porta congue. Duis suscipit purus nibh, et accumsan purus vestibulum sed. In lorem risus, malesuada eu sagittis nec, fermentum non mi. Donec ultricies tortor molestie dolor convallis, eget fringilla velit luctus. Suspendisse suscipit odio vel erat fermentum consectetur. Aliquam et tempor felis. Suspendisse imperdiet varius magna vel eleifend. Sed felis ante, accumsan sed dolor sit amet, hendrerit pretium purus. Sed suscipit libero eros, a vestibulum nisl molestie nec.\"}');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
