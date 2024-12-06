-- Create the database
CREATE DATABASE IF NOT EXISTS CoopPlatform;


-- Use the newly created database
USE CoopPlatform;


-- Create User table
CREATE TABLE IF NOT EXISTS User (
   userID INT AUTO_INCREMENT PRIMARY KEY,
   firstName VARCHAR(50),
   lastName VARCHAR(50),
   email VARCHAR(100) UNIQUE,
   major VARCHAR(50),
   skills TEXT,
   interests TEXT,
   isAdmin BOOLEAN DEFAULT FALSE,
   isAnalyst BOOLEAN DEFAULT FALSE
);


-- Create Companies table
CREATE TABLE IF NOT EXISTS Companies (
   companyID INT AUTO_INCREMENT PRIMARY KEY,
   name VARCHAR(100),
   description TEXT,
   createdAt DATETIME,
   updatedAT DATETIME
);


-- Create Industries table
CREATE TABLE IF NOT EXISTS Industries (
   industryID INT AUTO_INCREMENT PRIMARY KEY,
   name VARCHAR(100)
);


-- Create the relationship table for Industries and Companies
CREATE TABLE IF NOT EXISTS CompanyIndustry (
   companyID INT,
   industryID INT,
   PRIMARY KEY (companyID, industryID),
   FOREIGN KEY (companyID) REFERENCES Companies(companyID),
   FOREIGN KEY (industryID) REFERENCES Industries(industryID)
);


-- Create Location table
CREATE TABLE IF NOT EXISTS Location (
   locationID INT AUTO_INCREMENT PRIMARY KEY,
   companyID INT,
   address TEXT,
   city VARCHAR(100),
   state_province VARCHAR(100),
   country VARCHAR(100),
   FOREIGN KEY (companyID) REFERENCES Companies(companyID)
);


-- Create Role table
CREATE TABLE IF NOT EXISTS Role (
   roleID INT AUTO_INCREMENT PRIMARY KEY,
   companyID INT,
   locationID INT,
   roleName VARCHAR(100),
   description TEXT,
   skillsRequired TEXT,
   FOREIGN KEY (companyID) REFERENCES Companies(companyID),
   FOREIGN KEY (locationID) REFERENCES Location(locationID)
);


-- Create Reviews table
CREATE TABLE IF NOT EXISTS Reviews (
   reviewID INT AUTO_INCREMENT PRIMARY KEY,
   userID INT,
   roleID INT,
   createdAt DATETIME DEFAULT CURRENT_TIMESTAMP,
   updatedAt DATETIME ON UPDATE CURRENT_TIMESTAMP,
   publishedAt DATETIME,
   reviewType VARCHAR(50),
   heading VARCHAR(100),
   content TEXT,
   views INT DEFAULT 0,
   likes INT DEFAULT 0,
   isFlagged BOOLEAN DEFAULT FALSE,
   FOREIGN KEY (userID) REFERENCES User(userID),
   FOREIGN KEY (roleID) REFERENCES Role(roleID)
);


-- Create Comments table
CREATE TABLE IF NOT EXISTS Comments (
   commentID INT AUTO_INCREMENT PRIMARY KEY,
   reviewID INT,
   userID INT,
   parentCommentID INT DEFAULT NULL,
   createdAt DATETIME DEFAULT CURRENT_TIMESTAMP,
   updatedAt DATETIME ON UPDATE CURRENT_TIMESTAMP,
   content TEXT,
   likes INT DEFAULT 0,
   isFlagged BOOLEAN DEFAULT FALSE,
   FOREIGN KEY (reviewID) REFERENCES Reviews(reviewID),
   FOREIGN KEY (userID) REFERENCES User(userID),
   FOREIGN KEY (parentCommentID) REFERENCES Comments(commentID)
);


-- Create Badges table
CREATE TABLE IF NOT EXISTS Badges (
   badgeID INT AUTO_INCREMENT PRIMARY KEY,
   badgeName VARCHAR(50)
);


-- Create the relationship table for User and Badges
CREATE TABLE IF NOT EXISTS UserBadges (
   userID INT,
   badgeID INT,
   PRIMARY KEY (userID, badgeID),
   FOREIGN KEY (userID) REFERENCES User(userID),
   FOREIGN KEY (badgeID) REFERENCES Badges(badgeID)
);


-- Create Feedback table
CREATE TABLE IF NOT EXISTS Feedback (
   feedbackID INT AUTO_INCREMENT PRIMARY KEY,
   userID INT,
   timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
   header VARCHAR(100),
   content TEXT,
   status VARCHAR(100) DEFAULT 'In Progress',
   FOREIGN KEY (userID) REFERENCES User(userID)
);





