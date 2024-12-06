-- Use the newly created database
USE CoopPlatform;


INSERT INTO User (firstName, lastName, email, major, skills, interests, isAdmin, isAnalyst) VALUES
('Alice', 'Smith', 'alice.smith@example.com', 'Computer Science', 'Java, Python', 'AI, Robotics', FALSE, TRUE),
('Bob', 'Johnson', 'bob.johnson@example.com', 'Mathematics', 'R, MATLAB', 'Statistics, Data Science', FALSE, TRUE),
('Charlie', 'Brown', 'charlie.brown@example.com', 'Physics', 'C++, Fortran', 'Quantum Mechanics, Astrophysics', FALSE, FALSE),
('Diana', 'Prince', 'diana.prince@example.com', 'Electrical Engineering', 'C, Embedded Systems', 'Renewable Energy, IoT', FALSE, FALSE),
('Ethan', 'Hunt', 'ethan.hunt@example.com', 'Cybersecurity', 'Networking, Ethical Hacking', 'Digital Security, Cryptography', FALSE, TRUE),
('Fiona', 'Gallagher', 'fiona.gallagher@example.com', 'Psychology', 'SPSS, Data Analysis', 'Behavioral Studies, Neuropsychology', FALSE, FALSE),
('George', 'Michaels', 'george.michaels@example.com', 'Business', 'Excel, SQL', 'Entrepreneurship, Management', FALSE, FALSE),
('Hannah', 'Montana', 'hannah.montana@example.com', 'Music', 'Composition, Audio Editing', 'Songwriting, Producing', FALSE, FALSE),
('Ian', 'Malcolm', 'ian.malcolm@example.com', 'Biology', 'Genetics, Bioinformatics', 'Evolution, Conservation', FALSE, TRUE),
('Julia', 'Roberts', 'julia.roberts@example.com', 'Drama', 'Acting, Directing', 'Theater, Film Studies', FALSE, FALSE),
('Kevin', 'Hart', 'kevin.hart@example.com', 'Performing Arts', 'Comedy, Storytelling', 'Improv, Stand-up', FALSE, FALSE),
('Laura', 'Croft', 'laura.croft@example.com', 'Archaeology', 'Field Research, Mapping', 'Ancient Civilizations, Exploration', FALSE, TRUE),
('Michael', 'Scott', 'michael.scott@example.com', 'Business Administration', 'Leadership, Communication', 'Sales, Marketing', TRUE, FALSE),
('Nancy', 'Drew', 'nancy.drew@example.com', 'Criminology', 'Investigation, Profiling', 'Mysteries, Forensics', FALSE, FALSE),
('Oliver', 'Queen', 'oliver.queen@example.com', 'Political Science', 'Policy Analysis, Strategy', 'Social Justice, Governance', FALSE, FALSE),
('Penelope', 'Garcia', 'penelope.garcia@example.com', 'Information Systems', 'Database Management, Programming', 'Technology, Cybersecurity', FALSE, TRUE),
('Quincy', 'Jones', 'quincy.jones@example.com', 'Music', 'Arranging, Producing', 'Jazz, Classical', FALSE, FALSE),
('Rachel', 'Green', 'rachel.green@example.com', 'Fashion Design', 'Sketching, Sewing', 'Trends, Styling', FALSE, FALSE),
('Steve', 'Jobs', 'steve.jobs@example.com', 'Product Design', 'Innovation, Prototyping', 'Technology, Design Thinking', FALSE, TRUE),
('Tracy', 'Morgan', 'tracy.morgan@example.com', 'Comedy Writing', 'Humor, Screenwriting', 'Sitcoms, Stand-up', FALSE, FALSE),
('Uma', 'Thurman', 'uma.thurman@example.com', 'Film Studies', 'Directing, Editing', 'Cinema, Storytelling', FALSE, FALSE),
('Victor', 'Frankenstein', 'victor.frankenstein@example.com', 'Biotechnology', 'CRISPR, Synthetic Biology', 'Genetic Engineering, Bioethics', FALSE, TRUE),
('Will', 'Smith', 'will.smith@example.com', 'Acting', 'Acting, Producing', 'Film, Music', FALSE, FALSE),
('Xander', 'Harris', 'xander.harris@example.com', 'History', 'Archival Research, Writing', 'Medieval History, Literature', FALSE, FALSE),
('Yara', 'Greyjoy', 'yara.greyjoy@example.com', 'Marine Biology', 'Oceanography, Diving', 'Marine Conservation, Ecology', FALSE, TRUE),
('Zara', 'Larsson', 'zara.larsson@example.com', 'Music Production', 'Singing, Mixing', 'Pop Music, Performance', FALSE, FALSE),
('Adam', 'West', 'adam.west@example.com', 'Theater', 'Acting, Public Speaking', 'Drama, Performance', FALSE, FALSE),
('Bella', 'Swan', 'bella.swan@example.com', 'Literature', 'Creative Writing, Editing', 'Romance, Fiction', FALSE, FALSE),
('Chris', 'Evans', 'chris.evans@example.com', 'Film Production', 'Editing, Cinematography', 'Action, Direction', FALSE, TRUE),
('Derek', 'Shepherd', 'derek.shepherd@example.com', 'Medicine', 'Surgery, Research', 'Neurosurgery, Health Care', FALSE, FALSE),
('Evelyn', 'Salt', 'evelyn.salt@example.com', 'International Relations', 'Negotiation, Strategy', 'Conflict Resolution, Diplomacy', FALSE, FALSE),
('Finn', 'Hudson', 'finn.hudson@example.com', 'Music Education', 'Choir, Performance', 'Teaching, Vocal Training', FALSE, FALSE),
('Grace', 'Hopper', 'grace.hopper@example.com', 'Computer Science', 'Programming, Algorithms', 'Innovation, Women in Tech', TRUE, TRUE),
('Harvey', 'Specter', 'harvey.specter@example.com', 'Law', 'Litigation, Negotiation', 'Corporate Law, Strategy', FALSE, FALSE);

INSERT INTO Companies (name, description, createdAt, updatedAt) VALUES
('TechNova Inc.', 'A leading company in AI and machine learning solutions.', '2020-05-14 12:34:56', '2022-11-01 15:45:30'),
('GreenFields Ltd.', 'Specializing in sustainable agriculture and organic farming techniques.', '2021-02-20 09:22:10', '2023-05-14 10:40:20'),
('SkyHigh Aerospace', 'An innovator in aerospace engineering and satellite technology.', '2020-09-10 14:18:20', '2023-01-27 19:34:50'),
('EcoEnergy Co.', NULL, '2020-06-01 11:45:10', '2021-12-19 16:22:10'),
#('EcoEnergy Co.', 'Focused on renewable energy solutions, including solar and wind power.', '2020-06-01 11:45:10', '2021-12-19 16:22:10'),
('BrightFuture Education', 'Providing online and in-person educational programs worldwide.', '2021-07-15 08:30:00', '2024-04-12 18:11:45'),
('HealthCore Pharmaceuticals', 'Researching and developing cutting-edge medications.', '2020-11-05 10:20:30', '2022-08-21 09:50:40'),
('UrbanBuilders LLC', 'An urban construction and architecture firm creating smart cities.', '2022-03-18 15:12:00', '2023-10-25 20:05:50'),
('AquaLife Systems', 'Revolutionizing water purification and desalination technologies.', '2021-09-12 13:25:30', '2024-01-10 14:40:30'),
('GlobalTech Solutions', 'Delivering IT consulting and software development services.', '2021-05-25 10:50:50', '2023-07-15 17:05:20'),
('Stellar Entertainment', 'Producing films, music, and streaming content for a global audience.', '2020-12-19 14:15:45', '2022-06-30 18:25:40'),
('NextGen Robotics', 'Designing robots for industrial, medical, and household applications.', '2020-04-10 11:10:10', '2024-03-05 10:55:00'),
('FinPro Banking', 'A financial services firm offering innovative banking solutions.', '2021-08-23 16:45:25', '2022-11-18 12:35:50'),
('AutoFuture Ltd.', 'Developing electric and autonomous vehicles.', '2020-01-05 09:30:15', '2023-09-29 15:45:25'),
('BioGenomics Inc.', 'Advancing genetic research and biotechnology applications.', '2022-02-11 18:00:00', '2023-06-12 11:22:33'),
('BlueOcean Logistics', 'A global logistics provider specializing in ocean freight.', '2021-03-17 14:50:35', '2024-02-01 12:00:45'),
('CyberShield Security', 'Protecting businesses with advanced cybersecurity solutions.', '2020-08-21 10:05:45', '2023-03-30 14:45:50'),
('Peak Performance Sports', 'Manufacturing high-quality sports equipment and apparel.', '2020-10-13 09:15:00', '2022-10-05 16:50:40'),
('EcoHomes Construction', 'Building eco-friendly and energy-efficient homes.', '2021-06-30 14:45:20', '2023-12-02 20:10:10'),
('VirtuMed Technologies', 'Developing virtual reality solutions for medical training.', '2020-03-25 13:40:10', '2022-09-21 15:45:45'),
('Gourmet World Foods', 'An international distributor of gourmet and specialty foods.', '2020-07-14 11:30:00', '2024-01-22 10:20:50'),
('Visionary Designs', 'Offering innovative and stylish interior design services.', '2021-01-10 12:15:25', '2023-05-01 09:40:30'),
('PetCare Innovations', 'Creating cutting-edge products for pet health and wellness.', '2021-04-07 14:22:30', '2023-10-15 13:45:50'),
('TravelSphere Ltd.', 'Providing unique travel experiences and adventure tours.', '2020-02-19 08:45:15', '2023-07-11 17:30:20'),
('FusionTech Manufacturing', 'Specializing in advanced manufacturing and automation.', '2020-11-11 12:50:45', '2024-05-20 19:50:40'),
('DataPulse Analytics', 'Helping businesses harness big data for decision-making.', '2022-01-18 10:25:00', '2023-08-30 14:55:30'),
('GreenTech Farms', 'Implementing innovative vertical farming solutions.', '2021-11-21 15:35:20', '2024-04-14 09:45:00'),
('CloudNet Systems', 'Offering cloud computing and data storage services.', '2021-10-09 17:15:45', '2023-09-03 11:05:10'),
('ArtisanCrafts Co.', 'Supporting local artisans through handcrafted product sales.', '2020-06-08 09:45:10', '2022-05-25 18:55:40'),
('BrightPath Logistics', 'Providing last-mile delivery solutions for e-commerce.', '2021-07-05 13:50:50', '2024-03-19 15:20:30'),
('QuantumLeap Solutions', 'Researching quantum computing and its applications.', '2020-09-15 14:10:45', '2023-06-25 12:45:50');




INSERT INTO Industries (name) VALUES
('Information Technology'),
('Healthcare'),
('Education'),
('Finance'),
('Automotive'),
('Biotechnology'),
('Aerospace'),
('Renewable Energy'),
('Construction'),
('Entertainment'),
('Robotics'),
('Logistics'),
('Cybersecurity'),
('Sports and Recreation'),
('Real Estate'),
('Food and Beverage'),
('Interior Design'),
('Pet Care'),
('Travel and Tourism'),
('Manufacturing'),
('Data Analytics'),
('Agriculture'),
('Cloud Computing'),
('Arts and Crafts'),
('E-commerce'),
('Quantum Computing'),
('Fashion and Apparel'),
('Gaming'),
('Pharmaceuticals'),
('Marine and Aquatic Technologies');


INSERT INTO CompanyIndustry (companyID, industryID) VALUES
(1, 1), -- TechNova Inc. -> Information Technology
(1, 13), -- TechNova Inc. -> Cybersecurity
(2, 22), -- GreenFields Ltd. -> Agriculture
(2, 8), -- GreenFields Ltd. -> Renewable Energy
(3, 7), -- SkyHigh Aerospace -> Aerospace
(4, 8), -- EcoEnergy Co. -> Renewable Energy
(4, 21), -- EcoEnergy Co. -> Manufacturing
(5, 3), -- BrightFuture Education -> Education
(6, 2), -- HealthCore Pharmaceuticals -> Healthcare
(6, 30), -- HealthCore Pharmaceuticals -> Pharmaceuticals
(7, 9), -- UrbanBuilders LLC -> Construction
(8, 30), -- AquaLife Systems -> Marine and Aquatic Technologies
(9, 1), -- GlobalTech Solutions -> Information Technology
(10, 10), -- Stellar Entertainment -> Entertainment
(11, 12), -- NextGen Robotics -> Robotics
(11, 21), -- NextGen Robotics -> Manufacturing
(12, 4), -- FinPro Banking -> Finance
(13, 5), -- AutoFuture Ltd. -> Automotive
(13, 21), -- AutoFuture Ltd. -> Manufacturing
(14, 6), -- BioGenomics Inc. -> Biotechnology
(14, 30), -- BioGenomics Inc. -> Pharmaceuticals
(15, 12), -- BlueOcean Logistics -> Logistics
(16, 13), -- CyberShield Security -> Cybersecurity
(17, 14), -- Peak Performance Sports -> Sports and Recreation
(18, 9), -- EcoHomes Construction -> Construction
(18, 8), -- EcoHomes Construction -> Renewable Energy
(19, 1), -- VirtuMed Technologies -> Information Technology
(19, 3), -- VirtuMed Technologies -> Education
(20, 17), -- Gourmet World Foods -> Food and Beverage
(21, 10), -- Visionary Designs -> Interior Design
(22, 18), -- PetCare Innovations -> Pet Care
(23, 19), -- TravelSphere Ltd. -> Travel and Tourism
(24, 21), -- FusionTech Manufacturing -> Manufacturing
(25, 20), -- DataPulse Analytics -> Data Analytics
(26, 22), -- GreenTech Farms -> Agriculture
(27, 23), -- CloudNet Systems -> Cloud Computing
(28, 24), -- ArtisanCrafts Co. -> Arts and Crafts
(29, 25), -- BrightPath Logistics -> E-commerce
(30, 26); -- QuantumLeap Solutions -> Quantum Computing

INSERT INTO Location (companyID, address, city, state_province, country) VALUES
(1, '123 Innovation Blvd', 'San Francisco', 'California', 'USA'),
(2, '456 Greenway Rd', 'Seattle', 'Washington', 'USA'),
(3, '789 SkyHigh Dr', 'Huntsville', 'Alabama', 'USA'),
(4, '321 Solar St', 'Austin', 'Texas', 'USA'),
(5, '654 Bright Ln', 'Boston', 'Massachusetts', 'USA'),
(6, '987 Pharma Ave', 'Cambridge', 'Massachusetts', 'USA'),
(7, '111 Builder Way', 'New York', 'New York', 'USA'),
(8, '222 Water Works', 'Miami', 'Florida', 'USA'),
(9, '333 Tech Plaza', 'San Jose', 'California', 'USA'),
(10, '444 Entertainment Row', 'Los Angeles', 'California', 'USA'),
(11, '555 Robotics St', 'Pittsburgh', 'Pennsylvania', 'USA'),
(12, '666 Finance Blvd', 'Chicago', 'Illinois', 'USA'),
(13, '777 Auto Ln', 'Detroit', 'Michigan', 'USA'),
(14, '888 BioTech Rd', 'San Diego', 'California', 'USA'),
(15, '999 Ocean Dr', 'Savannah', 'Georgia', 'USA'),
(16, '121 Cyber Ave', 'Austin', 'Texas', 'USA'),
(17, '131 Sports Way', 'Portland', 'Oregon', 'USA'),
(18, '141 Eco Homes Blvd', 'Denver', 'Colorado', 'USA'),
(19, '151 MedTech Dr', 'Houston', 'Texas', 'USA'),
(20, '161 Gourmet St', 'Paris', 'Île-de-France', 'France'),
(21, '171 Design Ln', 'Milan', 'Lombardy', 'Italy'),
(22, '181 PetCare Way', 'Sydney', 'New South Wales', 'Australia'),
(23, '191 Travel Blvd', 'London', 'England', 'United Kingdom'),
(24, '201 FusionTech Rd', 'Munich', 'Bavaria', 'Germany'),
(25, '211 DataPulse Ave', 'Toronto', 'Ontario', 'Canada'),
(26, '221 Green Farms Rd', 'Amsterdam', 'North Holland', 'Netherlands'),
(27, '231 CloudNet Dr', 'Dublin', 'Leinster', 'Ireland'),
(28, '241 Artisan Row', 'Kyoto', 'Kyoto Prefecture', 'Japan'),
(29, '251 BrightPath Blvd', 'Shanghai', 'Shanghai', 'China'),
(30, '261 Quantum Leap Way', 'Zurich', 'Zurich', 'Switzerland'),
(1, '271 Silicon Way', 'Palo Alto', 'California', 'USA'),
(12, '282 Green Circle', 'Vancouver', 'British Columbia', 'Canada'),
(23, '293 Spaceport Dr', 'Cape Canaveral', 'Florida', 'USA'),
(24, '304 Renewable St', 'Berlin', 'Berlin', 'Germany'),
(5, '315 BrightStar Rd', 'Oslo', 'Oslo', 'Norway'),
(6, '326 Pharma Labs', 'Hyderabad', 'Telangana', 'India'),
(27, '337 Builder Ln', 'Tokyo', 'Tokyo Prefecture', 'Japan'),
(18, '348 Aqua Center', 'Cape Town', 'Western Cape', 'South Africa'),
(19, '359 TechHub Blvd', 'Bangalore', 'Karnataka', 'India'),
(10, '370 Creative Row', 'Stockholm', 'Stockholm County', 'Sweden'),
(21, '381 Robotics Ave', 'Seoul', 'Seoul', 'South Korea'),
(30, '392 Financial Way', 'Zurich', 'Zurich', 'Switzerland'),
(23, '403 Auto Plaza', 'Stuttgart', 'Baden-Württemberg', 'Germany'),
(14, '414 Biotech Blvd', 'Tel Aviv', 'Tel Aviv District', 'Israel'),
(5, '425 Logistics Lane', 'Dubai', 'Dubai', 'United Arab Emirates');

INSERT INTO Role (companyID, locationID, roleName, description, skillsRequired) VALUES
(1, 1, 'Machine Learning Engineer', 'Design and implement machine learning models for real-world applications.', 'Python, TensorFlow, Data Analysis'),
(2, 2, 'Sustainability Analyst', 'Analyze and optimize sustainable farming practices.', 'Data Analysis, Agricultural Science'),
(3, 3, 'Aerospace Engineer', 'Develop advanced spacecraft and satellite systems.', 'C++, Aerodynamics, CAD'),
(4, 4, 'Renewable Energy Consultant', 'Consult on renewable energy projects and strategies.', 'Project Management, Solar Technology'),
(5, 5, 'Educational Content Developer', 'Create engaging educational materials for online learning.', 'Curriculum Design, Content Writing'),
(6, 6, 'Clinical Research Scientist', 'Conduct research on pharmaceutical treatments and solutions.', 'Pharmacology, Research Methods'),
(7, 7, 'Architectural Designer', 'Design urban structures and smart city layouts.', 'AutoCAD, Urban Planning'),
(8, 8, 'Water Systems Engineer', 'Develop innovative water purification and desalination systems.', 'Hydraulics, System Design'),
(9, 9, 'Software Developer', 'Build scalable software solutions for clients.', 'Java, SQL, Cloud Platforms'),
(10, 10, 'Video Producer', 'Produce and manage video content for global distribution.', 'Adobe Premiere, Cinematography'),
(11, 11, 'Robotics Engineer', 'Develop robotics solutions for industrial applications.', 'Python, Robotics Frameworks'),
(12, 12, 'Financial Analyst', 'Analyze financial data to provide strategic advice.', 'Excel, Financial Modeling'),
(13, 13, 'Automotive Engineer', 'Design and test autonomous vehicle systems.', 'Matlab, Simulink, AI'),
(14, 14, 'Biotechnology Researcher', 'Conduct research in genetic engineering and biotechnology.', 'CRISPR, Lab Techniques'),
(15, 15, 'Logistics Manager', 'Oversee and optimize supply chain operations.', 'Supply Chain Management, SAP'),
(16, 16, 'Cybersecurity Specialist', 'Protect systems from cyber threats and vulnerabilities.', 'Penetration Testing, Network Security'),
(17, 17, 'Sports Equipment Designer', 'Design high-performance sports equipment.', 'Material Science, CAD'),
(18, 18, 'Eco-Friendly Construction Manager', 'Lead eco-friendly building projects.', 'Project Management, Green Building Standards'),
(19, 19, 'Virtual Reality Developer', 'Develop VR applications for medical training.', 'Unity, C#, 3D Modeling'),
(20, 20, 'Food Product Manager', 'Manage and oversee the development of gourmet food products.', 'Food Science, Marketing'),
(21, 21, 'Interior Designer', 'Create innovative and stylish interior designs.', 'Sketching, 3D Rendering'),
(22, 22, 'Veterinary Product Specialist', 'Develop and promote veterinary products.', 'Animal Science, Product Development'),
(23, 23, 'Tour Guide Manager', 'Coordinate and manage unique travel experiences.', 'Hospitality Management, Customer Service'),
(24, 24, 'Manufacturing Process Engineer', 'Optimize manufacturing processes and workflows.', 'Process Design, Lean Manufacturing'),
(25, 25, 'Data Scientist', 'Analyze big data for actionable insights.', 'Python, Machine Learning, Data Visualization'),
(26, 26, 'Agricultural Engineer', 'Implement innovative agricultural technologies.', 'Mechanical Engineering, Agricultural Systems'),
(27, 27, 'Cloud Infrastructure Engineer', 'Manage and deploy cloud-based solutions.', 'AWS, Kubernetes, Networking'),
(28, 28, 'Artisan Product Designer', 'Design and promote handcrafted artisan products.', 'Creativity, Marketing'),
(29, 29, 'E-commerce Operations Manager', 'Manage e-commerce logistics and operations.', 'Inventory Management, Analytics'),
(30, 30, 'Quantum Computing Researcher', 'Research and develop quantum computing applications.', 'Quantum Mechanics, Algorithms');

INSERT INTO Reviews (userID, roleID, publishedAt, reviewType, heading, content, views, likes, isFlagged) VALUES
(1, 1, '2024-01-01 10:00:00', 'Experience', 'Great Experience as an ML Engineer', 'I had a fantastic experience working as a Machine Learning Engineer at TechNova Inc. Learned a lot about AI.', 150, 35, FALSE),
(2, 2, '2024-01-05 15:30:00', 'Feedback', 'Improved Sustainability Practices', 'The company is making significant strides in sustainability, but communication needs improvement.', 100, 20, FALSE),
(3, 3, '2024-01-10 09:45:00', 'Review', 'Exciting Role in Aerospace', 'Working on cutting-edge technology was inspiring. Would recommend it to any aspiring engineer.', 200, 50, FALSE),
(4, 4, '2024-01-15 14:20:00', 'Insight', 'Great Opportunity in Renewable Energy', 'A rewarding experience with excellent leadership and vision.', 120, 25, FALSE),
(5, 5, '2024-01-20 11:10:00', 'Experience', 'Rewarding Work Environment', 'Collaborative culture and strong focus on education made my role enjoyable.', 90, 15, FALSE),
(6, 6, '2024-01-25 17:00:00', 'Feedback', 'Cutting-Edge Research', 'Involved in exciting research but workload was quite heavy.', 140, 30, FALSE),
(7, 7, '2024-02-01 08:00:00', 'Review', 'Urban Development at Its Best', 'Loved working on innovative projects for smart cities.', 85, 10, FALSE),
(8, 8, '2024-02-05 10:30:00', 'Insight', 'Advancing Water Purification', 'Meaningful work but limited opportunities for growth.', 70, 12, FALSE),
(9, 9, '2024-02-10 13:15:00', 'Experience', 'Dynamic Work Environment', 'Fast-paced and challenging, great place for software enthusiasts.', 180, 40, FALSE),
(10, 10, '2024-02-15 16:45:00', 'Feedback', 'Creative and Supportive', 'Perfect workplace for creative professionals.', 75, 18, FALSE),
(11, 11, '2024-02-20 19:20:00', 'Review', 'Robotics Projects Worth Pursuing', 'Exciting projects but management needs improvement.', 95, 20, FALSE),
(12, 12, '2024-02-25 07:30:00', 'Insight', 'Great Start for Financial Analysts', 'Supportive team and ample learning opportunities.', 105, 22, FALSE),
(13, 13, '2024-03-01 11:50:00', 'Experience', 'Innovative Role in Automotive', 'Hands-on experience with cutting-edge technologies.', 130, 35, FALSE),
(14, 14, '2024-03-05 09:40:00', 'Feedback', 'Inspiring Research Environment', 'Focus on innovation, but better work-life balance needed.', 165, 28, FALSE),
(15, 15, '2024-03-10 12:25:00', 'Review', 'Streamlined Logistics Management', 'Efficient processes and a dynamic team.', 80, 14, FALSE),
(16, 16, '2024-03-15 14:00:00', 'Insight', 'Top-notch Cybersecurity Expertise', 'Fantastic workplace for security professionals.', 200, 50, FALSE),
(17, 17, '2024-03-20 15:30:00', 'Experience', 'Challenging Sports Equipment Design', 'Opportunity to innovate, but tight deadlines.', 60, 10, FALSE),
(18, 18, '2024-03-25 16:45:00', 'Feedback', 'Sustainable and Collaborative', 'Loved the eco-friendly approach and teamwork.', 95, 25, FALSE),
(19, 19, '2024-03-30 10:10:00', 'Review', 'Immersive VR Development', 'Great exposure to VR development, but lacked mentorship.', 120, 18, FALSE),
(20, 20, '2024-04-01 13:00:00', 'Insight', 'Delicious Career Growth', 'Enjoyed working on gourmet food projects.', 80, 16, FALSE),
(21, 21, '2024-04-05 14:30:00', 'Experience', 'Creative Interior Design Projects', 'Amazing projects but needs better client communication.', 110, 20, FALSE),
(22, 22, '2024-04-10 09:15:00', 'Feedback', 'Innovative Pet Products', 'Great workplace with a fun and collaborative culture.', 90, 22, FALSE),
(23, 23, '2024-04-15 10:45:00', 'Review', 'Rewarding Travel Role', 'TravelSphere provides ample learning opportunities.', 115, 18, FALSE),
(24, 24, '2024-04-20 11:30:00', 'Insight', 'Streamlined Manufacturing Process', 'High-tech projects but long hours.', 130, 24, FALSE),
(25, 25, '2024-04-25 16:00:00', 'Experience', 'Data-Driven Insights', 'DataPulse offers cutting-edge analytics projects.', 170, 40, FALSE),
(26, 26, '2024-05-01 09:40:00', 'Feedback', 'Smart Agricultural Practices', 'Good place to grow for agricultural engineers.', 140, 35, FALSE),
(27, 27, '2024-05-05 11:30:00', 'Review', 'Innovative Cloud Technologies', 'Great workplace for cloud engineers.', 125, 30, FALSE),
(28, 28, '2024-05-10 14:15:00', 'Insight', 'Artisan Product Design', 'Creative work with room for growth.', 95, 12, FALSE),
(29, 29, '2024-05-15 10:00:00', 'Experience', 'Efficient E-commerce Operations', 'Fast-paced environment with rewarding challenges.', 80, 18, FALSE),
(30, 30, '2024-05-20 15:00:00', 'Feedback', 'Quantum Computing Innovations', 'Fascinating projects but steep learning curve.', 145, 28, FALSE);


INSERT INTO Comments (reviewID, userID, parentCommentID, content, likes, isFlagged) VALUES
(1, 2, NULL, 'This sounds like a fantastic experience! Thanks for sharing.', 10, FALSE),
(1, 3, 1, 'Absolutely agree! I had a similar experience.', 5, FALSE),
(2, 4, NULL, 'Do you think the communication issue is company-wide?', 8, FALSE),
(2, 1, 4, 'Yes, I think it varies by team, but it’s something to improve.', 6, FALSE),
(3, 5, NULL, 'Aerospace is such an exciting field. How was the workload?', 12, FALSE),
(4, 6, NULL, 'I’ve been considering applying here. Any tips for getting in?', 15, FALSE),
(4, 2, 6, 'Focus on renewable energy projects in your portfolio.', 7, FALSE),
(5, 7, NULL, 'I love collaborative environments. Sounds like a great role.', 4, FALSE),
(6, 8, NULL, 'Heavy workloads can be tough. Was the management supportive?', 9, FALSE),
(6, 9, 8, 'They were supportive but often stretched thin.', 3, FALSE),
(7, 10, NULL, 'Smart cities are the future. How innovative were the projects?', 13, FALSE),
(8, 11, NULL, 'What kind of growth opportunities were you hoping for?', 6, FALSE),
(8, 3, 11, 'Leadership roles or cross-functional projects.', 4, FALSE),
(9, 12, NULL, 'Tech companies often have dynamic environments. Did you feel valued?', 11, FALSE),
(10, 13, NULL, 'Supportive workplaces are so important for creatives.', 8, FALSE),
(11, 14, NULL, 'Robotics is fascinating! What kind of robots did you work on?', 14, FALSE),
(11, 15, 14, 'Mostly industrial robots for manufacturing.', 7, FALSE),
(12, 16, NULL, 'Finance is challenging. Did you have a good team?', 10, FALSE),
(13, 17, NULL, 'I’d love to work on autonomous vehicles. Any advice?', 18, FALSE),
(14, 18, NULL, 'How innovative was the genetic research you were involved in?', 20, FALSE),
(14, 19, 18, 'Very cutting-edge, especially in CRISPR technology.', 12, FALSE),
(15, 20, NULL, 'Efficient logistics management is key to success.', 9, FALSE),
(16, 21, NULL, 'What kind of tools were used for cybersecurity?', 11, FALSE),
(16, 22, 21, 'Mostly Splunk, Wireshark, and custom tools.', 5, FALSE),
(17, 23, NULL, 'Tight deadlines can be tough. How was the work-life balance?', 7, FALSE),
(18, 24, NULL, 'Eco-friendly construction is inspiring. What projects stood out?', 14, FALSE),
(19, 25, NULL, 'VR development is fascinating. What applications did you focus on?', 17, FALSE),
(19, 26, 25, 'Medical training simulations. Very impactful.', 10, FALSE),
(20, 27, NULL, 'Gourmet food development sounds interesting! How creative was it?', 8, FALSE),
(21, 28, NULL, 'Interior design is so rewarding. What was your favorite project?', 13, FALSE);


INSERT INTO Badges (badgeName) VALUES
('Top Contributor'),
('Expert Reviewer'),
('Helpful Commenter'),
('Insightful Reviewer'),
('Early Adopter'),
('Collaboration Champion'),
('Creative Thinker'),
('Innovation Advocate'),
('Team Player'),
('Knowledge Sharer'),
('Problem Solver'),
('Critical Thinker'),
('Community Builder'),
('Leadership Star'),
('Data Enthusiast');


INSERT INTO UserBadges (userID, badgeID) VALUES
(1, 1), -- User 1: Top Contributor
(1, 2), -- User 1: Expert Reviewer
(2, 3), -- User 2: Helpful Commenter
(2, 4), -- User 2: Insightful Reviewer
(3, 5), -- User 3: Early Adopter
(4, 6), -- User 4: Collaboration Champion
(4, 7), -- User 4: Creative Thinker
(5, 8), -- User 5: Innovation Advocate
(6, 9), -- User 6: Team Player
(6, 10), -- User 6: Knowledge Sharer
(7, 11), -- User 7: Problem Solver
(8, 12), -- User 8: Critical Thinker
(9, 13), -- User 9: Community Builder
(10, 14), -- User 10: Leadership Star
(11, 15), -- User 11: Data Enthusiast
(12, 1), -- User 12: Top Contributor
(13, 4), -- User 13: Insightful Reviewer
(14, 6), -- User 14: Collaboration Champion
(15, 7), -- User 15: Creative Thinker
(16, 8), -- User 16: Innovation Advocate
(17, 3), -- User 17: Helpful Commenter
(18, 10), -- User 18: Knowledge Sharer
(19, 11), -- User 19: Problem Solver
(20, 12), -- User 20: Critical Thinker
(21, 13), -- User 21: Community Builder
(22, 14), -- User 22: Leadership Star
(23, 15), -- User 23: Data Enthusiast
(24, 5), -- User 24: Early Adopter
(25, 9), -- User 25: Team Player
(26, 2); -- User 26: Expert Reviewer



INSERT INTO Feedback (userID, header, content, status) VALUES
(1, 'Great Service', 'I really appreciate the recent updates to the app.', 'In Progress'),
(2, 'Feature Request', 'Could you add a scheduling feature for tasks?', 'Implemented'),
(3, 'Bug Report', 'The app freezes when trying to generate a report.', 'In Progress'),
(4, 'Login Issue', 'Unable to reset my password using the forgot password option.', 'Rejected'),
(5, 'UI Feedback', 'The new layout is great, but the text is too small.', 'Implemented'),
(6, 'Performance Issue', 'The site becomes unresponsive during peak hours.', 'In Progress'),
(7, 'Dark Mode', 'Dark mode would improve usability at night.', 'Implemented'),
(8, 'Security Concern', 'Is there two-factor authentication available?', 'Rejected'),
(9, 'Account Feature', 'Can you provide an option to link multiple accounts?', 'In Progress'),
(10, 'Pricing Feedback', 'The pricing tiers seem unclear to new users.', 'Rejected'),
(11, 'New Feature', 'Adding analytics dashboards would be a great feature.', 'Implemented'),
(12, 'Mobile App Issue', 'The mobile app crashes when scrolling through large lists.', 'In Progress'),
(13, 'Positive Feedback', 'The team is doing a fantastic job with updates.', 'Implemented'),
(14, 'Bug in Search', 'The search function does not return relevant results.', 'In Progress'),
(15, 'User Permissions', 'Please allow admins to set custom permissions.', 'Implemented'),
(16, 'Customer Support', 'Your customer support resolved my issue quickly!', 'Rejected'),
(17, 'Feature Request', 'It would be great to have offline mode in the app.', 'Implemented'),
(18, 'Slow Loading', 'Pages take a long time to load on mobile devices.', 'In Progress'),
(19, 'API Enhancement', 'Can you add more filters to the API endpoints?', 'Rejected'),
(20, 'Email Notifications', 'The email notifications are inconsistent.', 'In Progress'),
(21, 'Dashboard Update', 'I like the new dashboard, but it feels a bit cluttered.', 'Implemented'),
(22, 'Integration Request', 'Can you integrate with XYZ service?', 'Rejected'),
(23, 'Navigation Issue', 'The navigation menu disappears on smaller screens.', 'In Progress'),
(24, 'Search Enhancement', 'Can you add autocomplete to the search bar?', 'Implemented'),
(25, 'Feature Idea', 'How about a collaborative editing feature?', 'In Progress'),
(26, 'UI Feedback', 'The color contrast is not accessible for all users.', 'Rejected'),
(27, 'Report Generation', 'Reports take too long to generate.', 'Implemented'),
(28, 'Settings Option', 'Allow users to export their settings as a file.', 'In Progress'),
(29, 'Appreciation', 'The recent updates have been excellent!', 'Implemented'),
(30, 'Feedback on Beta', 'The beta version is unstable on older devices.', 'Rejected'),
(1, 'Suggestion', 'Add a save as draft option for posts.', 'Implemented'),
(2, 'Account Settings', 'The account settings are difficult to navigate.', 'In Progress'),
(3, 'Feature Request', 'Include a timer for sessions.', 'Rejected'),
(4, 'UI Improvement', 'The text alignment on the settings page is off.', 'In Progress'),
(5, 'Server Downtime', 'The server goes down frequently in my region.', 'Implemented'),
(6, 'Password Management', 'Add a password strength indicator.', 'Rejected'),
(7, 'Onboarding', 'The onboarding process is not very user-friendly.', 'In Progress'),
(8, 'Localization', 'Can you add support for more languages?', 'Implemented'),
(9, 'Social Media', 'Integrate with popular social media platforms.', 'Rejected'),
(10, 'Billing System', 'The billing system has recurring issues.', 'In Progress');
