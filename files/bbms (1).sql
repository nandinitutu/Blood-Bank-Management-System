-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 07, 2021 at 08:39 AM
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
-- Database: `bbms`
--

-- --------------------------------------------------------

--
-- Table structure for table `bldstck`
--

CREATE TABLE `bldstck` (
  `bid` int(11) NOT NULL,
  `hid` int(11) NOT NULL,
  `ap` int(11) NOT NULL,
  `an` int(11) NOT NULL,
  `bp` int(11) NOT NULL,
  `bn` int(11) NOT NULL,
  `abp` int(11) NOT NULL,
  `abn` int(11) NOT NULL,
  `opg` int(11) NOT NULL,
  `ong` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bldstck`
--

INSERT INTO `bldstck` (`bid`, `hid`, `ap`, `an`, `bp`, `bn`, `abp`, `abn`, `opg`, `ong`) VALUES
(1, 1, 4, 2, 2, 2, 2, 2, 2, 2);

-- --------------------------------------------------------

--
-- Table structure for table `donorbld`
--

CREATE TABLE `donorbld` (
  `did` int(11) NOT NULL,
  `bld` varchar(10) NOT NULL,
  `pid` int(11) NOT NULL,
  `path` varchar(255) NOT NULL,
  `status` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `donorbld`
--

INSERT INTO `donorbld` (`did`, `bld`, `pid`, `path`, `status`) VALUES
(3, 'A+', 1, 'uploaded_files/0.76872702582215353.png', 0);

-- --------------------------------------------------------

--
-- Table structure for table `fdbk`
--

CREATE TABLE `fdbk` (
  `fid` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `sug` varchar(100) NOT NULL,
  `imp` varchar(100) NOT NULL,
  `frnd` varchar(100) NOT NULL,
  `ftr` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `fdbk`
--

INSERT INTO `fdbk` (`fid`, `name`, `email`, `sug`, `imp`, `frnd`, `ftr`) VALUES
(7, 'NANDINI MAITY', 'we@gmail.com', 'Work Hard Never Give Up !', 'Add more new features.........', 'good', 'Pretty Good.');

-- --------------------------------------------------------

--
-- Table structure for table `msg`
--

CREATE TABLE `msg` (
  `mid` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `cnct` varchar(10) NOT NULL,
  `addr` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `msg`
--

INSERT INTO `msg` (`mid`, `name`, `email`, `cnct`, `addr`) VALUES
(13, 'NANDINI MAITY', 'nssaa@gmail.com', '7980170029', 'Nandini Maity'),
(14, 'NANDINI MAITY', 'we@gmail.com', '7980000009', 'nnnnnnn mmmmm');

-- --------------------------------------------------------

--
-- Table structure for table `post`
--

CREATE TABLE `post` (
  `sid` int(11) NOT NULL,
  `post` varchar(255) NOT NULL,
  `font` varchar(50) NOT NULL,
  `back` varchar(50) NOT NULL,
  `text` varchar(50) NOT NULL,
  `status` int(6) NOT NULL,
  `pid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `post`
--

INSERT INTO `post` (`sid`, `post`, `font`, `back`, `text`, `status`, `pid`) VALUES
(3, 'I need O+ Blood !! Please kindly contact me.......', 'impact', '#FFCE54', '#000000', 1, 1),
(5, '45 Years old patient need A+ Blood. Urgent Need From Kolkata.', 'Monaco', '#DA4453', '#ffff00', 1, 4),
(6, 'Urgent Need of Blood B-\r\nFor 12 years Kid', 'Verdana', '#434A54', '#ffff00', 0, 5),
(8, 'A thalassemia patient Need A+ Blood In Between 7 day.', 'Georgia', '#48CFAD', '#000080', 0, 7);

-- --------------------------------------------------------

--
-- Table structure for table `registration`
--

CREATE TABLE `registration` (
  `pid` int(11) NOT NULL,
  `name` varchar(150) NOT NULL,
  `fname` varchar(150) NOT NULL,
  `mname` varchar(150) NOT NULL,
  `email` varchar(155) NOT NULL,
  `dob` date NOT NULL,
  `mob` varchar(20) NOT NULL,
  `age` int(20) NOT NULL,
  `gen` varchar(6) NOT NULL,
  `blood` varchar(6) NOT NULL,
  `city` varchar(20) NOT NULL,
  `addr` varchar(255) NOT NULL,
  `wgh` varchar(50) NOT NULL,
  `hgh` varchar(50) NOT NULL,
  `psw` varchar(155) NOT NULL,
  `squs` varchar(155) NOT NULL,
  `sans` varchar(155) NOT NULL,
  `status` int(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `registration`
--

INSERT INTO `registration` (`pid`, `name`, `fname`, `mname`, `email`, `dob`, `mob`, `age`, `gen`, `blood`, `city`, `addr`, `wgh`, `hgh`, `psw`, `squs`, `sans`, `status`) VALUES
(1, 'Nandini Maity', 'Sanjay Maity', 'Bandana Maity ', 'nandinitutu82@gmail.com', '2000-08-16', '798017002', 20, 'Female', 'A+', 'Kolkata', 'Baranagar', '60', '5.3', 'Nandini8', 'what was your first pets name?', 'betu', 0),
(4, 'Subhajit Ghosh', 'Kajal Ghosh', 'Sadhana Ghosh', 'subhajitghosh1260@gmail.com', '1999-06-22', '8013530481', 22, 'Male', 'B+', 'Kolkata', '1260 S.H.K.BOSE SAEANI JAWPUR', '40', '5.8', 'Subho1260', 'In what city or town did your mother and father meet?', 'Kolkata', 0),
(5, 'Srijita Majumder', 'Sanjib Majumder', 'Soma Majumder', 'srijitamajumder6@gmail.com', '1999-08-25', '98366 05055', 21, 'Female', 'B+', 'Kolkata', 'New Barrackpore', '55', '5.1', 'Srijita8', 'what was your first pets name?', 'neon', 0),
(7, 'Ritu Das', 'Ananda Das', 'Gita Das', 'adidevbose@gmail.com', '2019-06-05', '98446 33055', 2, 'Female', 'O-', 'Medinipur', 'A C Bose Sarani', '10', '2', 'RituRitu1', 'What was your childhood nickname?', 'Ritu', 0),
(12, 'Raju Roy', 'Sudip Roy', 'Priyanka Roy', 'abcd@gmail.com', '1989-06-21', '9036686420', 32, 'Male', 'AB+', 'Kharagpur', '208, K G Road', '60', '5.8', 'Rajudas1', 'What is your favourite actor?', 'dev', 0),
(13, 'Dipti Sen', 'Gagan Sen', 'Tumpa Sen', 'abc@gmail.com', '2008-06-04', '6249053792', 13, 'Female', 'B+', 'Asansol', 'A K Road', '40', '3.3', 'DiDIDIDI1', 'what was your first pets name?', 'jani', 0);

-- --------------------------------------------------------

--
-- Table structure for table `request`
--

CREATE TABLE `request` (
  `hid` int(11) NOT NULL,
  `hname` varchar(100) NOT NULL,
  `haddr` varchar(255) NOT NULL,
  `hemail` varchar(155) NOT NULL,
  `hpass` varchar(50) NOT NULL,
  `cont` varchar(10) NOT NULL,
  `pin` int(6) NOT NULL,
  `hcity` varchar(50) NOT NULL,
  `web` varchar(255) NOT NULL,
  `sques` varchar(100) NOT NULL,
  `sans` varchar(100) NOT NULL,
  `status` int(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `request`
--

INSERT INTO `request` (`hid`, `hname`, `haddr`, `hemail`, `hpass`, `cont`, `pin`, `hcity`, `web`, `sques`, `sans`, `status`) VALUES
(1, 'Baine Hospital', '123, 1, Gopal Lal Tagore Rd, Bonhooghly Government Colony, Baranagar, Kolkata, West Bengal 700035', 'bainehospital@gmail.com', 'bainehospital1234', '2147483647', 700036, 'Kolkata', 'https://www.justdial.com/Kolkata/Baine-Hospital-Near-Dunlop-Alambazar/033PXX33-XX33-180831220034-D7Z1_BZDET', 'What is your work address?', 'Baranagar', 1),
(2, 'Zenith Super Specialist Hospital', '9/3, Feeder Rd, Rathtala, Belghoria, Kolkata, West Bengal 700056', 'info@zenithhospital.in', 'zenithhospital1234', '2147483647', 700056, 'Kolkata', 'http://zenithhospital.in/', 'What was your first car?', 'Alto', 0),
(3, 'Galaxy Multispeciality Hospital', 'Kalyani Expy, Rabindrapally, Jaffarpur Panchanantala, Kolkata, West Bengal 700121', 'galaxyhospital@hospital.in', 'galaxyhospital1234', '2147483647', 700121, 'Kolkata', 'https://www.justdial.com/Kolkata/Galaxy-Hospital-Hanuman-Mandir-Basti-Garden-Reach/033PXX33-XX33-181108065954-R4C2_BZDET', 'what was your first pets name?', 'siro', 0);

-- --------------------------------------------------------

--
-- Table structure for table `srcbld`
--

CREATE TABLE `srcbld` (
  `sid` int(11) NOT NULL,
  `bld` varchar(10) NOT NULL,
  `pid` int(11) NOT NULL,
  `path` varchar(255) NOT NULL,
  `status` int(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `srcbld`
--

INSERT INTO `srcbld` (`sid`, `bld`, `pid`, `path`, `status`) VALUES
(7, 'B+', 5, 'uploaded_files/0.038628543222242851.png', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bldstck`
--
ALTER TABLE `bldstck`
  ADD PRIMARY KEY (`bid`);

--
-- Indexes for table `donorbld`
--
ALTER TABLE `donorbld`
  ADD PRIMARY KEY (`did`);

--
-- Indexes for table `fdbk`
--
ALTER TABLE `fdbk`
  ADD PRIMARY KEY (`fid`);

--
-- Indexes for table `msg`
--
ALTER TABLE `msg`
  ADD PRIMARY KEY (`mid`);

--
-- Indexes for table `post`
--
ALTER TABLE `post`
  ADD PRIMARY KEY (`sid`);

--
-- Indexes for table `registration`
--
ALTER TABLE `registration`
  ADD PRIMARY KEY (`pid`);

--
-- Indexes for table `request`
--
ALTER TABLE `request`
  ADD PRIMARY KEY (`hid`);

--
-- Indexes for table `srcbld`
--
ALTER TABLE `srcbld`
  ADD PRIMARY KEY (`sid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bldstck`
--
ALTER TABLE `bldstck`
  MODIFY `bid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `donorbld`
--
ALTER TABLE `donorbld`
  MODIFY `did` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `fdbk`
--
ALTER TABLE `fdbk`
  MODIFY `fid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `msg`
--
ALTER TABLE `msg`
  MODIFY `mid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `post`
--
ALTER TABLE `post`
  MODIFY `sid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `registration`
--
ALTER TABLE `registration`
  MODIFY `pid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `request`
--
ALTER TABLE `request`
  MODIFY `hid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `srcbld`
--
ALTER TABLE `srcbld`
  MODIFY `sid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
