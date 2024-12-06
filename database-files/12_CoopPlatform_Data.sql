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

INSERT INTO Companies (name, description) VALUES
('TechNova Inc.', 'A leading company in AI and machine learning solutions.'),
('GreenFields Ltd.', 'Specializing in sustainable agriculture and organic farming techniques.'),
('SkyHigh Aerospace', 'An innovator in aerospace engineering and satellite technology.'),
('EcoEnergy Co.', 'Focused on renewable energy solutions, including solar and wind power.'),
('BrightFuture Education', 'Providing online and in-person educational programs worldwide.'),
('HealthCore Pharmaceuticals', 'Researching and developing cutting-edge medications.'),
('UrbanBuilders LLC', 'An urban construction and architecture firm creating smart cities.'),
('AquaLife Systems', 'Revolutionizing water purification and desalination technologies.'),
('GlobalTech Solutions', 'Delivering IT consulting and software development services.'),
('Stellar Entertainment', 'Producing films, music, and streaming content for a global audience.'),
('NextGen Robotics', 'Designing robots for industrial, medical, and household applications.'),
('FinPro Banking', 'A financial services firm offering innovative banking solutions.'),
('AutoFuture Ltd.', 'Developing electric and autonomous vehicles.'),
('BioGenomics Inc.', 'Advancing genetic research and biotechnology applications.'),
('BlueOcean Logistics', 'A global logistics provider specializing in ocean freight.'),
('CyberShield Security', 'Protecting businesses with advanced cybersecurity solutions.'),
('Peak Performance Sports', 'Manufacturing high-quality sports equipment and apparel.'),
('EcoHomes Construction', 'Building eco-friendly and energy-efficient homes.'),
('VirtuMed Technologies', 'Developing virtual reality solutions for medical training.'),
('Gourmet World Foods', 'An international distributor of gourmet and specialty foods.'),
('Visionary Designs', 'Offering innovative and stylish interior design services.'),
('PetCare Innovations', 'Creating cutting-edge products for pet health and wellness.'),
('TravelSphere Ltd.', 'Providing unique travel experiences and adventure tours.'),
('FusionTech Manufacturing', 'Specializing in advanced manufacturing and automation.'),
('DataPulse Analytics', 'Helping businesses harness big data for decision-making.'),
('GreenTech Farms', 'Implementing innovative vertical farming solutions.'),
('CloudNet Systems', 'Offering cloud computing and data storage services.'),
('ArtisanCrafts Co.', 'Supporting local artisans through handcrafted product sales.'),
('BrightPath Logistics', 'Providing last-mile delivery solutions for e-commerce.'),
('QuantumLeap Solutions', 'Researching quantum computing and its applications.');




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
(1, 1, '2024-01-01 10:00:00', 'InterviewReport', 'Tricky questions about Python', 'It was so hard to figure out their python related questions.', 150, 35, FALSE),
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

INSERT INTO Reviews (userID, roleID, publishedAt, reviewType, heading, content, views, likes, isFlagged) VALUES
(2, 1, '2024-01-05 15:30:00', 'InterviewReport', 'Machine Learning Frameworks', 'They grilled me on machine learning frameworks like TensorFlow and PyTorch. Be ready for some deep technical discussions.', 130, 40, FALSE),
(3, 2, '2024-01-10 09:45:00', 'InterviewReport', 'Sustainability Practices in Agriculture', 'Expect detailed questions on sustainable farming techniques. They tested my knowledge of real-world agricultural challenges.', 180, 50, FALSE),
(4, 2, '2024-01-15 14:20:00', 'InterviewReport', 'Sustainability Metrics', 'They focused on sustainability metrics and how I would apply them to optimize farming practices.', 120, 30, FALSE),
(5, 3, '2024-01-20 11:10:00', 'InterviewReport', 'Aerospace Engineering Concepts', 'Be prepared for questions on spacecraft propulsion and satellite design. Technical, but stimulating!', 160, 45, FALSE),
(6, 3, '2024-01-25 17:00:00', 'InterviewReport', 'Advanced Aerospace Technology', 'They asked about advanced aerospace technologies and how I would improve existing designs.', 150, 40, FALSE),
(7, 4, '2024-02-01 08:00:00', 'InterviewReport', 'Renewable Energy Challenges', 'They asked about the challenges in renewable energy, especially regarding solar technology. Make sure to know your data.', 140, 38, FALSE),
(8, 4, '2024-02-05 10:30:00', 'InterviewReport', 'Solar Energy Design', 'The interview focused on solar energy design and real-life applications of green energy.', 110, 28, FALSE),
(9, 5, '2024-02-10 13:15:00', 'InterviewReport', 'Curriculum Design in Education', 'They asked how to design curricula for diverse learners, focusing on interactive learning strategies.', 180, 50, FALSE),
(10, 6, '2024-02-15 16:45:00', 'InterviewReport', 'Educational Content Challenges', 'Expect questions about educational content development under time constraints and adapting materials to different learning styles.', 140, 35, FALSE),
(11, 7, '2024-02-20 19:20:00', 'InterviewReport', 'Clinical Trials and Data Analysis', 'The focus was on clinical trial design, including statistical methods and data analysis challenges.', 200, 55, FALSE),
(12, 6, '2024-02-25 07:30:00', 'InterviewReport', 'Pharmaceutical Research Experience', 'Expect to discuss your past experience in pharmaceutical research, including data-driven decision making.', 170, 45, FALSE),
(13, 7, '2024-03-01 11:50:00', 'InterviewReport', 'Urban Development Strategies', 'They asked about sustainable urban development strategies and smart city concepts.', 150, 38, FALSE),
(14, 8, '2024-03-05 09:40:00', 'InterviewReport', 'Smart City Design', 'Expect to discuss your approach to designing smart city infrastructures, focusing on technological integration.', 140, 35, FALSE),
(15, 9, '2024-03-10 12:25:00', 'InterviewReport', 'Water Purification Systems', 'They asked about advanced water purification technologies and challenges in real-world applications.', 130, 33, FALSE),
(16, 10, '2024-03-15 14:00:00', 'InterviewReport', 'Water Systems Engineering Problems', 'The interview involved real-life engineering problems related to water desalination and purification.', 120, 30, FALSE),
(17, 11, '2024-03-20 15:30:00', 'InterviewReport', 'Software Development Process', 'The interview focused on software development methodologies and tools, including problem-solving during live coding challenges.', 200, 55, FALSE),
(18, 12, '2024-03-25 16:45:00', 'InterviewReport', 'Coding Challenges in Software Engineering', 'Expect live coding challenges focusing on algorithms, data structures, and system design.', 180, 50, FALSE),
(19, 13, '2024-03-30 10:10:00', 'InterviewReport', 'Creative Video Production', 'Expect questions on how to manage video projects from pre-production to distribution.', 140, 38, FALSE),
(20, 14, '2024-04-01 13:00:00', 'InterviewReport', 'Creative Content Production Techniques', 'They wanted to know my approach to creative video production, including time management and collaborating with teams under tight deadlines.', 130, 35, FALSE),
(21, 15, '2024-04-05 14:30:00', 'InterviewReport', 'Robotics Engineering Solutions', 'They focused on advanced robotics engineering, including the integration of AI into robotic systems.', 190, 50, FALSE),
(22, 15, '2024-04-10 09:15:00', 'InterviewReport', 'Robotics Project Management', 'Expect questions on managing large-scale robotics projects, especially in an industrial setting.', 180, 48, FALSE),
(23, 16, '2024-04-15 10:45:00', 'InterviewReport', 'Financial Modeling Techniques', 'Expect in-depth questions about financial modeling, with a focus on real-world applications in the financial sector.', 170, 45, FALSE),
(24, 16, '2024-04-20 11:30:00', 'InterviewReport', 'Advanced Financial Analysis', 'They asked me to walk through complex financial analysis and forecasting techniques under tight deadlines.', 160, 42, FALSE),
(25, 17, '2024-04-25 16:00:00', 'InterviewReport', 'Automotive Engineering Challenges', 'The interview focused on automotive systems design and innovative testing methods.', 150, 40, FALSE),
(26, 18, '2024-04-30 09:40:00', 'InterviewReport', 'Vehicle System Design', 'They asked about the design of autonomous vehicle systems and the technologies driving them.', 140, 38, FALSE),
(27, 18, '2024-05-05 11:30:00', 'InterviewReport', 'Biotechnology Research and Development', 'Expect to discuss biotechnology innovations, particularly in gene editing and CRISPR technology.', 160, 45, FALSE),
(28, 19, '2024-05-10 14:15:00', 'InterviewReport', 'Innovations in Genetic Engineering', 'I had to talk about the latest advancements in genetic engineering and their real-world applications.', 170, 50, FALSE),
(29, 20, '2024-05-15 10:00:00', 'InterviewReport', 'Logistics and Supply Chain Optimization', 'Expect to be questioned on logistics challenges and supply chain optimization techniques under pressure.', 130, 35, FALSE),
(30, 21, '2024-05-20 15:00:00', 'InterviewReport', 'Supply Chain Process Optimization', 'They asked how I would optimize supply chain processes and improve operational efficiency.', 140, 38, FALSE);

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



INSERT INTO Feedback (userID, header, content) VALUES
(1, 'Platform Improvement Suggestion', 'It would be great to have a dark mode feature for the platform.'),
(2, 'Bug Report', 'I encountered an error when trying to submit my review.'),
(3, 'Feature Request', 'A section for trending roles and reviews would be very useful.'),
(4, 'Positive Experience', 'The platform is user-friendly and intuitive. Keep up the great work!'),
(5, 'Role Matching Feedback', 'Role recommendations based on my skills are very accurate.'),
(6, 'Data Visualization Suggestion', 'Adding charts for role trends and analytics would be helpful.'),
(7, 'User Profile Customization', 'I’d like more options to customize my profile page.'),
(8, 'Slow Loading Issue', 'The reviews page sometimes loads very slowly.'),
(9, 'Mobile App Suggestion', 'A dedicated mobile app would improve accessibility.'),
(10, 'Content Moderation Concern', 'Some comments seem inappropriate and should be flagged faster.'),
(11, 'Review Sorting', 'Adding filters for reviews by date or popularity would be helpful.'),
(12, 'Badge System Feedback', 'The badge system is great but could be expanded with more levels.'),
(13, 'Search Functionality', 'The search bar could use better predictive text features.'),
(14, 'Community Engagement', 'The platform could host live events to foster more engagement.'),
(15, 'Navigation Improvement', 'The navigation menu could be more streamlined for new users.'),
(16, 'Privacy Concerns', 'I’d like more clarity on how my data is being used.'),
(17, 'Content Quality', 'Some reviews lack depth and could benefit from a word minimum.'),
(18, 'Notification Settings', 'Customizing notifications would make the experience better.'),
(19, 'Integration Request', 'Integration with LinkedIn would be highly beneficial.'),
(20, 'Overall Feedback', 'This platform has a lot of potential and is already very useful.'),
(21, 'Search Filter Request', 'Filters for location-based role searches would be very helpful.'),
(22, 'Comment Editing Option', 'It would be great if users could edit their comments after posting.'),
(23, 'Collaboration Features', 'Adding group discussions for roles or industries would foster collaboration.'),
(24, 'Enhanced Analytics', 'Role analytics could include average salaries and career growth trends.'),
(25, 'Email Notification Issues', 'I am not receiving email notifications for new comments on my reviews.'),
(26, 'Review Draft Saving', 'The ability to save a review as a draft would be helpful.'),
(27, 'Expanded Industry List', 'The platform could include more industries to choose from.'),
(28, 'User Verification', 'Adding user verification would increase trust in the community.'),
(29, 'Role Comparison Tool', 'A feature to compare roles side-by-side would be useful.'),
(30, 'Feedback Acknowledgement', 'It would be nice to get updates on submitted feedback.'),
(1, 'Improved Role Details', 'Providing detailed role descriptions with responsibilities would be helpful.'),
(2, 'Live Chat Support', 'Adding a live chat feature for user support would be beneficial.'),
(3, 'More Badge Categories', 'The badge system could include categories for mentorship and learning.'),
(4, 'Mentorship Program', 'A mentorship program linking experienced users with newcomers would be valuable.'),
(5, 'Content Curation', 'Curating high-quality reviews or featuring top contributors could inspire others.');

