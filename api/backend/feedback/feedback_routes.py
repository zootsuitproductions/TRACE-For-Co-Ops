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
feedback = Blueprint('feedback', __name__)


#------------------------------------------------------------
# Get all feedback from the system
@feedback.route('/feedback', methods=['GET'])
def get_feedback():
    try:
        # カーソルの管理
        with db.get_db().cursor() as cursor:
            cursor.execute('''
                SELECT feedbackID, userID, timestamp, header, content, status
                FROM Feedback;
            ''')
            theData = cursor.fetchall()

        # レスポンスを返す
        the_response = make_response(jsonify(theData))
        the_response.status_code = 200
        return the_response

    except Exception as e:
        current_app.logger.error(f"Error fetching feedback: {e}")
        return {"error": "An error occurred while fetching feedback"}, 500


@feedback.route('/feedback', methods=['PUT'])
def update_status():
    current_app.logger.info('PUT /feedback route')
    try:
        feedback_info = request.json

        if 'feedbackID' not in feedback_info or 'status' not in feedback_info:
            return {'error': 'Missing feedbackID or status'}, 400

        status = feedback_info['status']
        feedback_id = feedback_info['feedbackID']
        
        
        query = '''
        UPDATE Feedback
        SET status = %s
        WHERE feedbackID = %s;
        '''
        
        
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
    

