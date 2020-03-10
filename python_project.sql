-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 02, 2019 at 12:53 PM
-- Server version: 10.1.36-MariaDB
-- PHP Version: 7.2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `python_project`
--

-- --------------------------------------------------------

--
-- Table structure for table `bank_details`
--

CREATE TABLE `bank_details` (
  `SrNo` int(11) NOT NULL,
  `Bank_Name` text,
  `ATM_Card_No` text,
  `CVV` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bank_details`
--

INSERT INTO `bank_details` (`SrNo`, `Bank_Name`, `ATM_Card_No`, `CVV`) VALUES
(1, 'SBI BANK', '111111111111', '111'),
(2, 'HDFC BANK', '222222222222', '222'),
(3, 'ICICI BANK', '333333333333', '333'),
(4, 'PMC BANK', '444444444444', '444'),
(5, 'BANK OF BARODA', '555555555555', '555');

-- --------------------------------------------------------

--
-- Table structure for table `booking_history`
--

CREATE TABLE `booking_history` (
  `SrNo` int(11) NOT NULL,
  `Name` text,
  `Consumer_No` text,
  `Reference_No` text,
  `Booking_Date` text,
  `Payment_Method` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `booking_history`
--

INSERT INTO `booking_history` (`SrNo`, `Name`, `Consumer_No`, `Reference_No`, `Booking_Date`, `Payment_Method`) VALUES
(1, 'a', '999999999999', '47325431', '04-04-2019', 'Cash On Delivery'),
(2, 'a', '999999999999', '68595137', '04-04-2019', 'Cash On Delivery'),
(3, 'Pratik', '111111111111', '31106173', '04-04-2019', 'Cash On Delivery'),
(4, 'Suraj', '111111111115', '16430733', '05-04-2019', 'Cash On Delivery'),
(5, 'Hardik', '333333333333', '43133649', '05-04-2019', 'Paid Online'),
(6, 'a', '888888888888', '85426432', '05-04-2019', 'Paid Online'),
(7, 'suraj', '192384942923', '96420983', '05-04-2019', 'Cash On Delivery'),
(8, 'sqq', 'qfef4esrh6ty', '46818428', '05-04-2019', 'Paid Online'),
(9, 'shivam', '836926879222', '54560149', '05-04-2019', 'Cash On Delivery'),
(10, 'hardik', '666666666666', '64367944', '05-04-2019', 'Paid Online'),
(11, 'abcd', '121212121212', '52667002', '05-04-2019', 'Paid Online'),
(12, 'umang', '454545454545', '21543424', '05-04-2019', 'Paid Online'),
(13, 'suraj', '123443211234', '28288830', '07-04-2019', 'Paid Online'),
(14, 'Pratik', '123456781358', '44158370', '07-04-2019', 'Paid Online'),
(15, 'pratik', '678678678678', '57217861', '12-04-2019', 'Paid Online'),
(16, 'kartik', '456789012345', '50196020', '12-04-2019', 'Paid Online'),
(17, 'abc', '759841248876', '19577727', '13-04-2019', 'Paid Online'),
(18, 'Rutuja', '123456789456', '80861463', '24-05-2019', 'Paid Online'),
(19, 'Nayan', '798234672347', '26124375', '31-05-2019', 'Paid Online');

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `SrNo` int(11) NOT NULL,
  `Feedback` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `feedback`
--

INSERT INTO `feedback` (`SrNo`, `Feedback`) VALUES
(1, 'Fine'),
(2, 'Excellent'),
(3, 'good'),
(4, 'Good\nEasy To Use System'),
(5, 'excellent service');

-- --------------------------------------------------------

--
-- Table structure for table `registration_details`
--

CREATE TABLE `registration_details` (
  `SrNo` int(11) NOT NULL,
  `Name` char(20) DEFAULT NULL,
  `Cons_No` text,
  `Mobile_No` text,
  `Username` char(20) DEFAULT NULL,
  `Password` char(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `registration_details`
--

INSERT INTO `registration_details` (`SrNo`, `Name`, `Cons_No`, `Mobile_No`, `Username`, `Password`) VALUES
(1, 'a', '999999999999', '9999999999', 'a', '99999999'),
(2, 'Pratik', '111111111111', '1111111111', 'Pratik123', '12345678'),
(3, 'a', '999999999991', '9999999999', 'b', '11122230'),
(4, 'b', '123456789012', '9999999999', '12', '98765432'),
(5, 'Suraj', '111111111115', '1111111110', 'q', 'bbbbb111'),
(6, 'Hardik', '333333333333', '3333333333', 'c', 'aaaaaaaa'),
(7, 'a', '888888888888', '8888888888', '8', '88888888'),
(8, 'suraj', '192384942923', '9987545755', 'abc', 'abc@1234'),
(9, 'sqq', 'qfef4esrh6ty', 'abcdefghio', 'scd', 'abc@12345'),
(10, 'shivam', '836926879222', '4465678678', 'shivam', '12341234'),
(11, 'hardik', '666666666666', '6666666666', 'hardik123', '77777777'),
(12, 'knjn', '676767676767', '8080022219', 'cd', '11111111'),
(13, 'abcd', '121212121212', '1212121212', 'ab', '12121212'),
(14, 'umang', '454545454545', '4545454545', 'umang123', 'umang123'),
(15, 'f', '123123123123', '1231231234', 'pppppppp', 'pppppppp'),
(16, 't', '123123123456', '1231231231', 't', 'tttttttt'),
(17, 'suraj', '123443211234', '1234554321', 'suraj123', 'suraj123'),
(18, 'Pratik', '123456781358', '9987554120', 'Pratik1234', 'Pratik1234'),
(19, 'pratik', '678678678678', '9987554122', 'pratik456', 'hhhhhhhh'),
(20, 'kartik', '456789012345', '8945280589', 'kartik123', 'kartik123'),
(21, 'abc', '759841248876', '8845776325', 'abcd@123', 'abcd@123'),
(22, 'Rutuja', '123456789456', '7889563412', 'Rutuja', 'Rutuja123'),
(23, 'Nayan', '798234672347', '9702797180', 'Nayan123', 'Nayan123');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bank_details`
--
ALTER TABLE `bank_details`
  ADD PRIMARY KEY (`SrNo`);

--
-- Indexes for table `booking_history`
--
ALTER TABLE `booking_history`
  ADD PRIMARY KEY (`SrNo`);

--
-- Indexes for table `feedback`
--
ALTER TABLE `feedback`
  ADD PRIMARY KEY (`SrNo`);

--
-- Indexes for table `registration_details`
--
ALTER TABLE `registration_details`
  ADD PRIMARY KEY (`SrNo`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bank_details`
--
ALTER TABLE `bank_details`
  MODIFY `SrNo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `booking_history`
--
ALTER TABLE `booking_history`
  MODIFY `SrNo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `feedback`
--
ALTER TABLE `feedback`
  MODIFY `SrNo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `registration_details`
--
ALTER TABLE `registration_details`
  MODIFY `SrNo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
