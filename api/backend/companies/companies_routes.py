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
                SELECT C.companyID, C.name, C.description, C.updatedAT, I.name, L.address, L.city, L.state_province, L.country, R.roleName, R.description, R.skillsRequired, L.locationID AS `Location ID`, I.IndustryID AS `Industry ID`, R.roleID AS `Role ID`
                FROM Companies C JOIN Location L
                ON C.companyID = L.companyID JOIN CompanyIndustry CI
                ON CI.companyID = C.companyID JOIN Industries I
                ON I.industryID = CI.industryID JOIN Role R
                ON R.companyID = C.companyID
                ORDER BY C.companyID, C.name ASC;
            ''')
            theData = cursor.fetchall()

        the_response = make_response(jsonify(theData))
        the_response.status_code = 200
        return the_response

    except Exception as e:
        current_app.logger.error(f"Error fetching companies: {e}")
        return {"error": "An error occurred while fetching companies"}, 500


@companies.route('/companies/companies', methods=['PUT'])
def update_company():
    current_app.logger.info('PUT /feedback route')
    try:
        companies_info = request.json

        if 'companyID' not in companies_info or 'Company Description' not in companies_info:
            return {'error': 'Missing companyID or Company Description'}, 400

        company_id = companies_info['companyID']
        company_discription = companies_info['Company Description']
        
        
        query = '''
        UPDATE Companies
        SET description = %s
        WHERE companyID = %s
        '''
        
        data = (company_discription, company_id)

        cursor = db.get_db().cursor()
        cursor.execute(query, data)
        db.get_db().commit()

        return {'message': 'Companies updated successfully'}, 200

    except KeyError as e:
        current_app.logger.error(f"Missing key in request JSON: {str(e)}")
        return {'error': f'Missing key: {str(e)}'}, 400
    except Exception as e:
        current_app.logger.error(f"Error updating feedback: {str(e)}")
        return {'error': 'An error occurred while updating companies'}, 500
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
            
            
@companies.route('/companies/roles', methods=['PUT'])
def update_roles():
    current_app.logger.info('PUT /feedback route')
    try:
        companies_info = request.json

        if 'RoleID' not in companies_info or 'Skills Required' not in companies_info or 'Role Description' not in companies_info:
            return {'error': 'Missing RoleID or Skills Required or Role Description'}, 400

        company_id = companies_info['companyID']
        role_id = companies_info['RoleID']
        skill = companies_info['Skills Required']
        role_description = companies_info['Role Description']
        
        query = '''
        UPDATE Role
        SET description = %s,
            skillsRequired = %s
        WHERE companyID = %s AND roleID = %s;
        '''
        
        data = (role_description, skill, company_id, role_id)

        cursor = db.get_db().cursor()
        cursor.execute(query, data)
        db.get_db().commit()

        return {'message': 'Roles updated successfully'}, 200

    except KeyError as e:
        current_app.logger.error(f"Missing key in request JSON: {str(e)}")
        return {'error': f'Missing key: {str(e)}'}, 400
    except Exception as e:
        current_app.logger.error(f"Error updating roles: {str(e)}")
        return {'error': 'An error occurred while updating roles'}, 500
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()

