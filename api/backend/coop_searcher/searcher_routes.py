########################################################
# Sample customers blueprint of endpoints
# Remove this file if you are not using it in your project
########################################################
from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db
from backend.ml_models.model01 import predict

#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of 
# routes.
searcher = Blueprint('coop_searcher', __name__)

#------------------------------------------------------------
# Get all customers from the system
@searcher.route('/companiesWithReviews', methods=['GET'])
def get_companies_with_reviews():

    query = '''
                    SELECT DISTINCT c.name AS CompanyName
                    FROM Companies c
                    JOIN Role r ON c.companyID = r.companyID
                    JOIN Reviews rv ON r.roleID = rv.roleID;
    '''
    
    # get the database connection, execute the query, and 
    # fetch the results as a Python Dictionary
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# Get reviews for a specific company
@searcher.route('/reviewsForCompany/<company_name>', methods=['GET'])
def get_reviews_for_company(company_name):

    # Use parameterized query to prevent SQL injection
    query = '''
    SELECT 
        rv.content,
        rv.publishedAt,
        rv.userID,
        rv.reviewID,
        rv.views,
        rv.likes,
        rv.heading,
        r.roleName,
        r.roleID,
        rv.reviewType
    FROM 
        Reviews rv
    JOIN 
        Role r ON rv.roleID = r.roleID
    JOIN 
        Companies c ON r.companyID = c.companyID
    WHERE 
        c.name = %s
    '''
    
    # Get the database connection, execute the query, and 
    # fetch the results as a Python Dictionary
    cursor = db.get_db().cursor()
    cursor.execute(query, (company_name,))  # Passing company_name as a parameter
    theData = cursor.fetchall()
    
    # Format the results into a structured dictionary
    results = [
        {
            "content": row["content"],
            "heading": row["heading"],
            "roleName": row["roleName"],
            "reviewID": row["reviewID"],
            "likes": row["likes"],
            "views": row["views"],
            "roleID": row["roleID"],
            "publishedAt": row["publishedAt"],
            "reviewType": row["reviewType"],
            "userID": row["userID"]
        }
        for row in theData
    ]
    
    # Make the response
    response = make_response(jsonify(results))
    response.status_code = 200
    return response


# Get reviews for a specific company
@searcher.route('/interviewReportsForCompany/<company_name>', methods=['GET'])
def get_interview_reports_for_company(company_name):

    # Use parameterized query to prevent SQL injection
    query = '''
    SELECT 
        rv.content
    FROM 
        Reviews rv
    JOIN 
        Role r ON rv.roleID = r.roleID
    JOIN 
        Companies c ON r.companyID = c.companyID
    WHERE 
        c.name = %s
        AND
        rv.reviewType = 'InterviewReport'

    '''
    
    # get the database connection, execute the query, and 
    # fetch the results as a Python Dictionary
    cursor = db.get_db().cursor()
    cursor.execute(query, (company_name,))  # Passing company_name as a parameter
    theData = cursor.fetchall()
    
    # Make the response
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response


# Get possible skills
@searcher.route('/possibleSkills', methods=['GET'])
def get_possible_skills():
    # Query to get the skillsRequired for all roles
    query = '''
        SELECT r.skillsRequired
        FROM Role r;
    '''
    
    # Get the database connection, execute the query, and fetch the results
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# Get roles that require a specific skill
@searcher.route('/rolesForSkill/<skill>', methods=['GET'])
def get_roles_for_skill(skill):
    try:
        # Query to find roles that require the specified skill
        query = '''
            SELECT r.roleName, c.name AS companyName, r.skillsRequired
            FROM Role r
            JOIN Companies c ON r.companyID = c.companyID
            WHERE r.skillsRequired LIKE %s;
        '''
        
        # Get the database connection, execute the query, and fetch the results
        cursor = db.get_db().cursor()
        cursor.execute(query, ('%' + skill + '%',))  # Using LIKE to match the skill within skillsRequired
        theData = cursor.fetchall()
        
        # If no roles are found, log a warning
        if not theData:
            current_app.logger.warning(f"No roles found requiring the skill: {skill}")
        
        # Make the response
        response = make_response(jsonify(theData))
        response.status_code = 200
        return response
        
    except Exception as e:
        # Log the error and return a 500 error response
        current_app.logger.error(f"Error fetching roles for skill {skill}: {e}")
        return make_response(jsonify({"error": "Database query failed"}), 500)


# Increment likes for a specific review
@searcher.route('/review/<int:review_id>/like', methods=['POST'])
def like_review(review_id):
    try:
        # Query to increment the likes for the given review ID
        query = '''
            UPDATE Reviews
            SET likes = likes + 1
            WHERE reviewID = %s;
        '''
        
        # Get the database connection and execute the query
        cursor = db.get_db().cursor()
        cursor.execute(query, (review_id,))
        db.get_db().commit()
        
        # Check if any row was updated
        if cursor.rowcount == 0:
            return make_response(jsonify({"message": "Review not found"}), 404)
        
        # Return a success response
        return make_response(jsonify({"message": "Review liked successfully!"}), 200)
    
    except Exception as e:
        # Log the error and return a 500 error response
        current_app.logger.error(f"Error liking review with ID {review_id}: {e}")
        return make_response(jsonify({"error": "Database query failed"}), 500)


# Flag a review
@searcher.route('/review/<int:review_id>/flag', methods=['POST'])
def flag_review(review_id):
    try:
        # Query to flag the review
        query = '''
            UPDATE Reviews
            SET isFlagged = TRUE
            WHERE reviewID = %s;
        '''
        
        # Get the database connection and execute the query
        cursor = db.get_db().cursor()
        cursor.execute(query, (review_id,))
        db.get_db().commit()
        
        # Check if any row was updated
        if cursor.rowcount == 0:
            return make_response(jsonify({"message": "Review not found"}), 404)
        
        # Return a success response
        return make_response(jsonify({"message": "Review flagged successfully!"}), 200)
    
    except Exception as e:
        # Log the error and return a 500 error response
        current_app.logger.error(f"Error flagging review with ID {review_id}: {e}")
        return make_response(jsonify({"error": "Database query failed"}), 500)