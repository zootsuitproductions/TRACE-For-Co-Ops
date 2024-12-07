# video link
https://drive.google.com/file/d/1L7Nu3Phfua9m765dMDErn2DCuctszMql/view?usp=drive_link 


## How to Run Locally
1. Clone this repository:  
   ```bash
   git clone https://github.com/zootsuitproductions/coupe.git
   docker compose up -d

# COUPE: TRACE for Co-Ops

COUPE is a data-driven platform designed to revolutionize the co-op search process for Northeastern University students by offering peer-to-peer insights into company experiences. Our mission is to provide students with transparent, verified, and meaningful reviews on workplace culture, roles, and interview processes to help them find their ideal co-op match.

## Key Features
- **Peer-Reviewed Insights**  
  Access authentic reviews about company culture, roles, and work-life balance written by fellow students.  
- **Application and Interview Guidance**  
  Gain detailed insights into application processes, interview questions, and preparation tips.  
- **Incentivized Contribution System**  
  Share your own co-op experiences to unlock access to additional content and earn platform rewards.

---

## Target Users
### **Persona 1: Sebastian Studentson**  
A second-year CS student seeking guidance for his first co-op, overwhelmed by options and in need of peer insights to confidently navigate his search.

### **Persona 2: Riley Reviewer**  
A fourth-year marketing major who wants to share detailed feedback on their co-op experience to help others make informed decisions.

### **Persona 3: Alex Admin**  
The platform administrator responsible for moderating reviews, resolving disputes, and maintaining the integrity of the platform.

### **Persona 4: Annalise Analyst**  
A data analyst evaluating user trends and engagement to drive improvements in platform features and user experience.

---

## Technology Stack
- **Frontend:** Streamlit  
- **Middleware:** Python Flask  
- **Backend:** MySQL  
- **Containerization:** Docker  
- **Development Tools:** VSCode, DataGrip

---

## Database Schema
The database consists of multiple interconnected tables, including:
- **User:** Stores user information, including roles (e.g., Admin, Analyst).  
- **Companies:** Lists companies with associated industries and locations.  
- **Role:** Details job roles, required skills, and associated companies.  
- **Reviews:** Houses peer reviews with fields for headings, content, and engagement metrics.  
- **Comments:** Allows threaded discussions on reviews.  
- **Badges:** Tracks user achievements and contributions.  



---

## REST API Endpoints
Here is an example of the REST API matrix. For detailed documentation

| Resource             | GET                                       | POST                          | PUT                 | DELETE            |
|----------------------|-------------------------------------------|-------------------------------|---------------------|-------------------|
| `/companiesWithReviews` | Return all companies with reviews.       | N/A                           | N/A                 | N/A               |
| `/reviews`            | Retrieve reviews based on filters.        | Submit a new review.          | Update an existing review. | Delete a review. |
| `/admin/flaggedContent` | Retrieve flagged reviews for moderation. | N/A                           | Resolve flagged content. | Remove flagged content. |

---

## ✨ User Stories
### Sebastian Studentson
- As a co-op searcher, I want to find detailed insights about a company’s culture and values to ensure alignment with my work style.

### Riley Reviewer
- As a former co-op student, I want an easy-to-use feedback submission form to share structured and meaningful reviews.

### Alex Admin
- As an admin, I need to moderate flagged reviews efficiently to maintain the platform's integrity.

### Annalise Analyst
- As an analyst, I need tools to identify gaps in content, such as underrepresented industries, and track user engagement.

---

