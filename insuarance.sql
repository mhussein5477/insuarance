-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 14, 2021 at 12:52 PM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 7.3.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `insuarance`
--

-- --------------------------------------------------------

--
-- Table structure for table `predictions`
--

CREATE TABLE `predictions` (
  `id` int(11) NOT NULL,
  `name` varchar(250) NOT NULL,
  `city` varchar(250) NOT NULL,
  `phoneno` varchar(250) NOT NULL,
  `email` varchar(250) NOT NULL,
  `age` int(11) NOT NULL,
  `sex` int(11) NOT NULL,
  `salary` int(11) NOT NULL,
  `tax` int(11) NOT NULL,
  `costofliving` int(11) NOT NULL,
  `healthcondition` int(11) NOT NULL,
  `highway` int(11) NOT NULL,
  `smoker` int(11) NOT NULL,
  `crimerate` int(11) NOT NULL,
  `job` int(11) NOT NULL,
  `children` int(11) NOT NULL,
  `lifestyle` varchar(250) NOT NULL,
  `result` varchar(250) NOT NULL,
  `accuracy` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `predictions`
--

INSERT INTO `predictions` (`id`, `name`, `city`, `phoneno`, `email`, `age`, `sex`, `salary`, `tax`, `costofliving`, `healthcondition`, `highway`, `smoker`, `crimerate`, `job`, `children`, `lifestyle`, `result`, `accuracy`) VALUES
(1, 'test test test', 'test', '071245785', 'test@gmail.com', 30, 1, 70000, 2100, 19998, 1, 1, 1, 1, 0, 4, 'middleclass', '25900', '89.757'),
(2, 'test test test', 'test', '071245785', 'test@gmail.com', 30, 1, 70000, 2100, 19998, 1, 1, 1, 1, 0, 4, 'middleclass', '25900', '71.936'),
(3, 'test test test', 'test', '071245785', 'test@gmail.com', 30, 1, 70000, 2100, 19998, 1, 1, 1, 1, 0, 4, 'middleclass', '25900', '88.944'),
(4, 'test test test', 'test', '071245785', 'test@gmail.com', 52, 1, 75000, 5000, 20000, 0, 1, 1, 1, 0, 4, 'middleclass', '27750', '85.396');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(250) NOT NULL,
  `phone` varchar(250) NOT NULL,
  `city` varchar(250) NOT NULL,
  `email` varchar(250) NOT NULL,
  `category` varchar(250) NOT NULL,
  `password` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `phone`, `city`, `email`, `category`, `password`) VALUES
(3, 'Collins Odhiambo', '071245785', 'Nairobi', 'collo@gmail.com', 'admin', '$2b$12$sqoW0Bl.sGcZLBs7w48dIO/JoSpXOOKL.fzv5EEuXxsbFp61OYBrK'),
(4, 'Samue Sanya', '+2547123456789', 'Nakuru', 'sam@gmail.com', 'user', '$2b$12$YqAYv8NElOHpJz22bmC0lOfcn1jB5F5TcaOY4dlvyjFwJe3RcgBti');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `predictions`
--
ALTER TABLE `predictions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `predictions`
--
ALTER TABLE `predictions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
