-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8081
-- Generation Time: Dec 18, 2020 at 02:02 PM
-- Server version: 5.7.24
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `breizhibus`
--

-- --------------------------------------------------------

--
-- Table structure for table `arrets`
--

CREATE TABLE `arrets` (
  `id_arret` int(11) NOT NULL,
  `nom` varchar(20) NOT NULL,
  `adresse` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `arrets`
--

INSERT INTO `arrets` (`id_arret`, `nom`, `adresse`) VALUES
(1, 'Korrigan', '1 impasse du Korrigan'),
(2, 'Morgana', '2 place Morgana'),
(3, 'L\'Ankou', '3 place de l\'Ankou'),
(4, 'Ys', '4 rue de l\'Ys'),
(5, 'Viviane', '5 avenue de Viviane'),
(6, 'Guénolé', '6 rue Saint Guénolé');

-- --------------------------------------------------------

--
-- Table structure for table `arrets_lignes`
--

CREATE TABLE `arrets_lignes` (
  `id_ligne` int(11) NOT NULL,
  `id_arret` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `arrets_lignes`
--

INSERT INTO `arrets_lignes` (`id_ligne`, `id_arret`) VALUES
(1, 1),
(1, 2),
(1, 3),
(2, 2),
(2, 4),
(2, 6),
(3, 4),
(3, 5),
(3, 6),
(3, 1),
(4, 1),
(4, 3),
(4, 5);

-- --------------------------------------------------------

--
-- Table structure for table `bus`
--

CREATE TABLE `bus` (
  `id_bus` int(11) NOT NULL,
  `numero` varchar(4) NOT NULL,
  `immatriculation` varchar(7) NOT NULL,
  `nombre_places` int(11) NOT NULL DEFAULT '25',
  `id_ligne` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `bus`
--

INSERT INTO `bus` (`id_bus`, `numero`, `immatriculation`, `nombre_places`, `id_ligne`) VALUES
(1, 'BB01', 'CA123DO', 20, 1),
(2, 'BB02', 'NO123EL', 30, 2),
(3, 'BB03', 'JE123UX', 20, 3),
(4, 'BB04', 'RE123PA', 30, 1),
(7, 'BB05', 'PU123LL', 25, NULL),
(8, 'BB06', 'FE123TE', 25, NULL),
(10, 'BB07', 'AA123ZZ', 12, 2),
(11, 'BB08', 'AA123ZZ', 12, 4),
(12, 'BB58', 'ZA345AA', 34, 4);

-- --------------------------------------------------------

--
-- Table structure for table `ligne`
--

CREATE TABLE `ligne` (
  `id_ligne` int(11) NOT NULL,
  `nom` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `ligne`
--

INSERT INTO `ligne` (`id_ligne`, `nom`) VALUES
(1, 'Rouge'),
(2, 'Vert'),
(3, 'Bleu'),
(4, 'Noir');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `arrets`
--
ALTER TABLE `arrets`
  ADD PRIMARY KEY (`id_arret`);

--
-- Indexes for table `arrets_lignes`
--
ALTER TABLE `arrets_lignes`
  ADD KEY `arret` (`id_arret`),
  ADD KEY `lignes` (`id_ligne`);

--
-- Indexes for table `bus`
--
ALTER TABLE `bus`
  ADD PRIMARY KEY (`id_bus`),
  ADD KEY `ligne_bus` (`id_ligne`);

--
-- Indexes for table `ligne`
--
ALTER TABLE `ligne`
  ADD PRIMARY KEY (`id_ligne`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `arrets`
--
ALTER TABLE `arrets`
  MODIFY `id_arret` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `bus`
--
ALTER TABLE `bus`
  MODIFY `id_bus` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `ligne`
--
ALTER TABLE `ligne`
  MODIFY `id_ligne` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `arrets_lignes`
--
ALTER TABLE `arrets_lignes`
  ADD CONSTRAINT `arret` FOREIGN KEY (`id_arret`) REFERENCES `arrets` (`id_arret`) ON DELETE NO ACTION,
  ADD CONSTRAINT `lignes` FOREIGN KEY (`id_ligne`) REFERENCES `ligne` (`id_ligne`) ON DELETE NO ACTION;

--
-- Constraints for table `bus`
--
ALTER TABLE `bus`
  ADD CONSTRAINT `ligne_bus` FOREIGN KEY (`id_ligne`) REFERENCES `ligne` (`id_ligne`) ON DELETE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
