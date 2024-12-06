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
            rv.content
        FROM 
            Reviews rv
        JOIN 
            Role r ON rv.roleID = r.roleID
        JOIN 
            Companies c ON r.companyID = c.companyID
        WHERE 
            c.name = %s;
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

