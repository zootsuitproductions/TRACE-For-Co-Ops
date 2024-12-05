-- only the examples that update or insert into tables
USE CoopPlatform;

-- 1.6 Insert a recent interview experience.
INSERT INTO InterviewReports (roleID, userID, questions, timeline, tips)
VALUES (1, 123, 'What are your strengths?', 'Applied in August, interviewed in September', 'Focus on teamwork skills and problem-solving.');


-- Persona 2: Riley Reviewer


-- 2.1 Submit detailed insights on a co-op experience.
INSERT INTO Reviews (roleID, userID, publishedAt, heading, content)
VALUES (1, 123, NOW(), 'Great Work Environment', 'Collaborative and inclusive environment with supportive management.');


-- 2.2 Break down feedback into structured categories.
-- Note: Adjusted to match the schema
INSERT INTO Reviews (roleID, userID, publishedAt, heading, content)
VALUES (2, 124, NOW(), 'Fast-Paced and Challenging', 'Innovative culture but tough work-life balance during campaigns.');


-- 2.3 Provide feedback on work-life balance.
UPDATE Reviews
SET content = CONCAT(content, ' Flexible hours but tight deadlines occasionally.')
WHERE reviewID = 5;


-- 2.4 Describe an interview experience.
INSERT INTO InterviewReports (roleID, userID, questions, timeline, tips)
VALUES (2, 124, 'Behavioral and technical questions', 'Interview took 2 weeks', 'Focus on leadership examples for behavioral questions.');


-- 2.5 Update a review after receiving a full-time offer.
UPDATE Reviews
SET heading = 'Supportive Mentorship Opportunities', content = CONCAT(content, ' Expanded to include leadership roles.')
WHERE reviewID = 5;


-- 2.6 Reward user contributions with badges.
INSERT INTO UserBadges (userID, badgeID)
VALUES (124, (SELECT badgeID FROM Badges WHERE badgeName = 'Top Reviewer'));


-- Persona 3: Alex Admin


-- 3.2 Resolve disputes over flagged content.
UPDATE Reviews
SET isFlagged = FALSE
WHERE reviewID = 10;


-- 3.3 Update company profiles.
UPDATE Companies
SET description = 'Leading tech company specializing in AI and robotics'
WHERE companyID = 3;



-- Persona 4: Annalise Analyst
