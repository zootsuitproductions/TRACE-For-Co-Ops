########################################################
# Companies blueprint of endpoints
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
companies = Blueprint('companies', __name__)


#------------------------------------------------------------
# Get all feedback from the system
@companies.route('/companies', methods=['GET'])
def get_feedback():
    try:
        with db.get_db().cursor() as cursor:
            cursor.execute('''
                SELECT C.name, C.description, C.updatedAT, I.name, L.address, L.city, L.state_province, L.country, R.roleName, R.description, R.skillsRequired
                FROM Companies C JOIN Location L
                ON C.companyID = L.companyID JOIN CompanyIndustry CI
                ON CI.companyID = C.companyID JOIN Industries I
                ON I.industryID = CI.industryID JOIN Role R
                ON R.companyID = C.companyID
                ORDER BY C.name ASC;
            ''')
            theData = cursor.fetchall()

        the_response = make_response(jsonify(theData))
        the_response.status_code = 200
        return the_response

    except Exception as e:
        current_app.logger.error(f"Error fetching companies: {e}")
        return {"error": "An error occurred while fetching companies"}, 500

'''
@feedback.route('/feedback', methods=['PUT'])
def update_status():
    current_app.logger.info('PUT /feedback route')
    try:
        feedback_info = request.json

        if 'feedbackID' not in feedback_info or 'status' not in feedback_info:
            return {'error': 'Missing feedbackID or status'}, 400

        status = feedback_info['status']
        feedback_id = feedback_info['feedbackID']
        
        
        query = 
        UPDATE Feedback
        SET status = %s
        WHERE feedbackID = %s;
        
        
        
        data = (status, feedback_id)

        cursor = db.get_db().cursor()
        cursor.execute(query, data)
        db.get_db().commit()

        return {'message': 'Feedback status updated successfully'}, 200

    except KeyError as e:
        current_app.logger.error(f"Missing key in request JSON: {str(e)}")
        return {'error': f'Missing key: {str(e)}'}, 400
    except Exception as e:
        current_app.logger.error(f"Error updating feedback: {str(e)}")
        return {'error': 'An error occurred while updating feedback status'}, 500
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
'''
