-- phpMyAdmin SQL Dump
-- version 3.5.2.2
-- http://www.phpmyadmin.net
--
-- Client: 127.0.0.1
-- Généré le: Mar 14 Mars 2023 à 04:20
-- Version du serveur: 5.5.27-log
-- Version de PHP: 5.4.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données: `ruche`
--

-- --------------------------------------------------------

--
-- Structure de la table `gps`
--

CREATE TABLE IF NOT EXISTS `gps` (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `coordonnees` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `date` date NOT NULL,
  `heure` time NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Contenu de la table `gps`
--

INSERT INTO `gps` (`coordonnees`, `date`, `heure`) VALUES
('43.114294, 5.855473', '2051-04-07', '14:58:02'),
('43.115030, 5.852912', '2045-12-26', '15:25:45');

-- --------------------------------------------------------

--
-- Structure de la table `capteur_poids`
--

CREATE TABLE IF NOT EXISTS `capteur_poids` (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `poids` float UNSIGNED NOT NULL,
  `date` date NOT NULL,
  `heure` time NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Contenu de la table `capteur_poids`
--

INSERT INTO `capteur_poids` (`poids`, `date`, `heure`) VALUES
(30.45, '2051-04-07', '14:58:02'),
(47.54, '2045-12-26', '15:25:45');

-- --------------------------------------------------------

--
-- Structure de la table `capteur_meteorologique`
--

CREATE TABLE IF NOT EXISTS `capteur_meteorologique` (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `thermometrie` float UNSIGNED NOT NULL,
  `hygrometrie` float UNSIGNED NOT NULL,
  `barometrie` float UNSIGNED NOT NULL,
  `date` date NOT NULL,
  `heure` time NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Contenu de la table `capteur_meteorologique`
--

INSERT INTO `capteur_meteorologique` (`thermometrie`, `hygrometrie`, `barometrie`, `date`, `heure`) VALUES
(24.45, 17.458, 1.5487, '2051-04-07', '14:58:02'),
(19.65, 12.124, 1.0547, '2045-12-26', '15:25:45');

-- --------------------------------------------------------

--
-- Structure de la table `contacts`
--

CREATE TABLE IF NOT EXISTS `contacts` (
  `numero_telephone` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `nom` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `prenom` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `fonction` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`numero_telephone`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Contenu de la table `contacts`
--

INSERT INTO `contacts` (`numero_telephone`, `nom`, `prenom`, `fonction`) VALUES
('0123456789', 'DUPONT', 'Jean', 'Elève');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
