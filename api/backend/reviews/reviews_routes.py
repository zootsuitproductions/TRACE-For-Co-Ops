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

from datetime import datetime

#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of 
# routes.
reviews = Blueprint('reviews', __name__)
@reviews.route('/reviews', methods=['GET'])
def get_reviews():
    try:
        with db.get_db().cursor() as cursor:
            cursor.execute('''
                SELECT *
                FROM Reviews;
            ''')
            theData = cursor.fetchall()

        the_response = make_response(jsonify(theData))
        the_response.status_code = 200
        return the_response

    except Exception as e:
        current_app.logger.error(f"Error fetching reviews: {e}")
        return {"error": "An error occurred while fetching reviews"}, 500

@reviews.route('/comments', methods=['GET'])
def get_comments():
    try:
        with db.get_db().cursor() as cursor:
            cursor.execute('''
                SELECT *
                FROM Comments
                WHERE isFlagged = TRUE;
            ''')
            theData = cursor.fetchall()

        the_response = make_response(jsonify(theData))
        the_response.status_code = 200
        return the_response

    except Exception as e:
        current_app.logger.error(f"Error fetching comments: {e}")
        return {"error": "An error occurred while fetching comments"}, 500

@reviews.route('/flagged', methods=['GET'])
def get_flaggedreview():
    try:
        with db.get_db().cursor() as cursor:
            cursor.execute('''
                SELECT reviewID, reviewType, heading, content
                FROM Reviews
                WHERE  isFlagged = TRUE;
            ''')
            theData = cursor.fetchall()

        the_response = make_response(jsonify(theData))
        the_response.status_code = 200
        return the_response

    except Exception as e:
        current_app.logger.error(f"Error fetching flagged reviewss: {e}")
        return {"error": "An error occurred while fetching flagged reviews"}, 500
    
@reviews.route('/approveflagged', methods=['PUT'])
def approve_flaggedreview():
    current_app.logger.info('PUT /reviews route')
    try:
        review_info = request.json

        if 'reviewID' not in review_info or 'isFlagged' not in review_info:
            return {'error': 'Missing reviewID or isFlagged'}, 400

        review_id = review_info['reviewID']
        if_flagged = review_info['isFlagged']
        
        
        query = '''
        UPDATE Reviews
        SET isFlagged = %s
        WHERE reviewID= %s;
        '''
        
        data = (if_flagged, review_id)

        cursor = db.get_db().cursor()
        cursor.execute(query, data)
        db.get_db().commit()

        return {'message': 'Reviews status updated successfully'}, 200

    except KeyError as e:
        current_app.logger.error(f"Missing key in request JSON: {str(e)}")
        return {'error': f'Missing key: {str(e)}'}, 400
    except Exception as e:
        current_app.logger.error(f"Error updating reviews: {str(e)}")
        return {'error': 'An error occurred while updating reviews status'}, 500
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()   

@reviews.route('/editflagged', methods=['PUT'])
def edit_flaggedreview():
    current_app.logger.info('PUT /reviews route')
    try:
        review_info = request.json

        if 'reviewID' not in review_info or 'content' not in review_info:
            return {'error': 'Missing reviewID or content'}, 400

        review_id = review_info['reviewID']
        content = review_info['content']
        
        
        query = '''
        UPDATE Reviews
        SET isFlagged = FALSE,
            content = %s
        WHERE reviewID= %s;
        '''
        
        data = (content, review_id)

        cursor = db.get_db().cursor()
        cursor.execute(query, data)
        db.get_db().commit()

        return {'message': 'Reviews status updated successfully'}, 200

    except KeyError as e:
        current_app.logger.error(f"Missing key in request JSON: {str(e)}")
        return {'error': f'Missing key: {str(e)}'}, 400
    except Exception as e:
        current_app.logger.error(f"Error updating reviews: {str(e)}")
        return {'error': 'An error occurred while updating reviews status'}, 500
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()   
            
@reviews.route('/removeflagged', methods=['DELETE'])
def remove_flaggedreview():
    current_app.logger.info('DELETE /removeflagged route')
    try:
        review_info = request.json

        if 'reviewID' not in review_info:
            return {'error': 'Missing reviewID'}, 400

        review_id = review_info['reviewID']

        try:
            review_id = int(review_id)
        except ValueError:
            return {'error': 'Invalid reviewID format'}, 400

        query = '''
        DELETE FROM Reviews
        WHERE reviewID = %s;
        '''
        data = (review_id,)

        cursor = db.get_db().cursor()
        cursor.execute(query, data)
        db.get_db().commit()

        return {'message': 'Review deleted successfully'}, 200

    except KeyError as e:
        current_app.logger.error(f"Missing key in request JSON: {str(e)}")
        return {'error': f'Missing key: {str(e)}'}, 400
    except Exception as e:
        current_app.logger.error(f"Error deleting review: {str(e)}")
        return {'error': 'An error occurred while deleting the review.'}, 500
    finally:
        if cursor is not None:
            cursor.close()


@reviews.route('/submitReview', methods=['POST'])
def add_review():
    review_data = request.json
    try:
        # Get current timestamp for publishedAt
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Construct SQL query to insert the review
        query = """
        INSERT INTO Reviews (userID, roleID, publishedAt, reviewType, heading, content, views, likes, isFlagged)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            review_data["userID"],
            review_data["roleID"],
            current_time,  # Use the current timestamp for publishedAt
            review_data["reviewType"],
            review_data["heading"],
            review_data["content"],
            0,  # Default views
            0,  # Default likes
            False  # Default isFlagged
        )

        # Execute the query
        cursor = db.get_db().cursor()
        cursor.execute(query, values)
        db.get_db().commit()

        # Return success response
        return jsonify({"message": "Review added successfully!"}), 201

    except Exception as e:
        # Handle errors and return an error response
        error_message = str(e)
        print("Error:", error_message)
        print(traceback.format_exc())
        return jsonify({"error": error_message}), 500


# Assuming `reviews` is your Blueprint for this module
@reviews.route('/addComment', methods=['POST'])
def add_comment():
    comment_data = request.json
    try:
        # Get current timestamp for createdAt
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Construct SQL query to insert the comment
        query = """
        INSERT INTO Comments (reviewID, userID, content, createdAt, likes)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (
            comment_data["reviewID"],  # Review ID to link the comment to
            comment_data["userID"],   # User ID of the commenter
            comment_data["content"],  # The comment text
            current_time,             # Use the current timestamp for createdAt
            0                         # Default likes to 0
        )

        # Execute the query
        cursor = db.get_db().cursor()
        cursor.execute(query, values)
        db.get_db().commit()

        # Return success response
        return jsonify({"message": "Comment added successfully!"}), 201

    except Exception as e:
        # Handle errors and return an error response
        error_message = str(e)
        print("Error:", error_message)
        print(traceback.format_exc())
        return jsonify({"error": error_message}), 500

# ------------------------------------------------------------
# get product information about a specific product
# notice that the route takes <id> and then you see id
# as a parameter to the function.  This is one way to send 
# parameterized information into the route handler.
@reviews.route('/reviewsByUser/<id>', methods=['GET'])
def get_product_detail (id):

    query = f'''
        SELECT 
    r.reviewID,
    r.roleID,
    r.createdAt,
    r.updatedAt,
    r.publishedAt,
    r.reviewType,
    r.heading,
    r.content,
    r.views,
    r.likes,
    r.isFlagged
FROM 
    Reviews r
WHERE 
    r.userID = {str(id)};
    '''
    
    # get the database connection, execute the query, and 
    # fetch the results as a Python Dictionary
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

@reviews.route('/roleDetails/<role_id>', methods=['GET'])
def get_role_details(role_id):
    query = f'''
        SELECT 
            r.roleName, 
            c.name
        FROM 
            Role r
        JOIN 
            Companies c ON r.companyID = c.companyID
        WHERE 
            r.roleID = {str(role_id)};
    '''
    
    # Get the database connection, execute the query, and fetch the results as a Python Dictionary
    cursor = db.get_db().cursor()
    cursor.execute(query)
    role_data = cursor.fetchone()  # Assuming the result is a single row
    
    # If no result is found
    if not role_data:
        return jsonify({'error': 'Role not found'}), 404
    
    response = {
        'roleName': role_data['roleName'],
        'companyName': role_data['name']
    }
    
    return make_response(jsonify(response), 200)

@reviews.route('/companies', methods=['GET'])
def get_companies():
    query = '''
        SELECT 
            c.companyID,
            c.name AS company_name,
            c.description AS company_description,
            c.createdAt AS company_createdAt,
            c.updatedAt AS company_updatedAt
        FROM 
            Companies c
    '''
     # Execute the query
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

@reviews.route('/rolesByCompany/<int:company_id>', methods=['GET'])
def get_roles_by_company(company_id):
    query = f'''
        SELECT 
            r.roleID,
            r.roleName,
            r.description AS role_description,
            r.skillsRequired,
            c.name AS company_name,
            c.description AS company_description,
            c.createdAt AS company_createdAt,
            c.updatedAt AS company_updatedAt
        FROM 
            Role r
        JOIN 
            Companies c ON r.companyID = c.companyID
        WHERE 
            r.companyID = {company_id};
    '''
    
    # Get the database connection, execute the query, and fetch the results as a Python Dictionary
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    # Create the response
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response



@reviews.route('/commentsByReview/<reviewID>', methods=['GET'])
def get_comments_by_review(reviewID):
    query = f'''
        SELECT 
            c.commentID,
            c.userID,
            c.parentCommentID,
            c.createdAt,
            c.content,
            c.likes
        FROM 
            Comments c
        WHERE 
            c.reviewID = {str(reviewID)}
        ORDER BY 
            c.createdAt ASC;
    '''
    
    # Get the database connection, execute the query, and 
    # fetch the results as a Python Dictionary
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

@reviews.route('/deleteReview/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    try:
        # Define the query to delete the review
        query = f'''
            DELETE FROM Reviews
            WHERE reviewID = {review_id};
        '''

        # Get the database connection and execute the query
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()

        # Check if any row was affected (deleted)
        if cursor.rowcount > 0:
            response = make_response(jsonify({"message": "Review deleted successfully"}))
            response.status_code = 200
        else:
            response = make_response(jsonify({"message": "Review not found"}))
            response.status_code = 404
    except Exception as e:
        # Log the exception and return a 500 error
        logger.error(f"Error deleting review: {e}")
        response = make_response(jsonify({"message": "Internal Server Error", "error": str(e)}))
        response.status_code = 500

    return response

@reviews.route('/updateReview', methods=['PUT'])
def update_review():
    data = request.get_json()
    
    reviewID = data.get('reviewID')
    heading = data.get('heading')
    content = data.get('content')

    print("NEW CONTENT: ", content)
    
    query = '''
        UPDATE Reviews
        SET heading = %s, content = %s
        WHERE reviewID = %s;
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query, (heading, content, reviewID))
    db.get_db().commit()

    response = make_response(jsonify({"message": "Review updated successfully"}))
    response.status_code = 200
    return response

    

#------------------------------------------------------------
# Get all the products from the database, package them up,
# and return them to the client
@reviews.route('/products', methods=['GET'])
def get_products():
    query = '''
        SELECT 
    r.reviewID,
    r.roleID,
    r.createdAt,
    r.updatedAt,
    r.publishedAt,
    r.reviewType,
    r.heading,
    r.content,
    r.views,
    r.likes,
    r.isFlagged
FROM 
    Reviews r
WHERE 
    r.userID = ;
    '''
    
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute(query)

    # fetch all the data from the cursor
    # The cursor will return the data as a 
    # Python Dictionary
    theData = cursor.fetchall()

    # Create a HTTP Response object and add results of the query to it
    # after "jasonify"-ing it.
    response = make_response(jsonify(theData))
    # set the proper HTTP Status code of 200 (meaning all good)
    response.status_code = 200
    # send the response back to the client
    return response


    
# ------------------------------------------------------------
# Get the top 5 most expensive products from the database
@reviews.route('/mostExpensive')
def get_most_pop_products():

    query = '''
        SELECT product_code, 
               product_name, 
               list_price, 
               reorder_level
        FROM products
        ORDER BY list_price DESC
        LIMIT 5
    '''
    
    # Same process as handler above
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
 
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# ------------------------------------------------------------
# Route to get the 10 most expensive items from the 
# database.
@reviews.route('/tenMostExpensive', methods=['GET'])
def get_10_most_expensive_products():
    
    query = '''
        SELECT product_code, 
               product_name, 
               list_price, 
               reorder_level
        FROM products
        ORDER BY list_price DESC
        LIMIT 10
    '''
    
    # Same process as above
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response
    

# ------------------------------------------------------------
# This is a POST route to add a new product.
# Remember, we are using POST routes to create new entries
# in the database. 
@reviews.route('/product', methods=['POST'])
def add_new_product():
    
    # In a POST request, there is a 
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    name = the_data['product_name']
    description = the_data['product_description']
    price = the_data['product_price']
    category = the_data['product_category']
    
    query = f'''
        INSERT INTO products (product_name,
                              description,
                              category, 
                              list_price)
        VALUES ('{name}', '{description}', '{category}', {str(price)})
    '''
    # TODO: Make sure the version of the query above works properly
    # Constructing the query
    # query = 'insert into products (product_name, description, category, list_price) values ("'
    # query += name + '", "'
    # query += description + '", "'
    # query += category + '", '
    # query += str(price) + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response("Successfully added product")
    response.status_code = 200
    return response

# ------------------------------------------------------------
### Get all product categories
@reviews.route('/categories', methods = ['GET'])
def get_all_categories():
    query = '''
        SELECT DISTINCT category AS label, category as value
        FROM products
        WHERE category IS NOT NULL
        ORDER BY category
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
        
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# ------------------------------------------------------------
# This is a stubbed route to update a product in the catalog
# The SQL query would be an UPDATE. 
@reviews.route('/product', methods = ['PUT'])
def update_product():
    product_info = request.json
    current_app.logger.info(product_info)

    return "Success"