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

#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of 
# routes.
reviews = Blueprint('reviews', __name__)


@reviews.route('/addReview', methods=['POST'])
def add_review():
    review_data = request.json
    try:
        query = """
        INSERT INTO Reviews (userID, roleID, publishedAt, reviewType, heading, content, views, likes, isFlagged)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            review_data["userID"],
            review_data["roleID"],
            review_data["publishedAt"],
            review_data["reviewType"],
            review_data["heading"],
            review_data["content"],
            review_data["views"],
            review_data["likes"],
            review_data["isFlagged"]
        )
        cursor = db.get_db().cursor()
        cursor.execute(query, values)
        db.get_db().commit()
        return jsonify({"message": "Review added successfully!"}), 201
    except Exception as e:
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

@reviews.route('/updateReview', methods=['PUT'])
def update_review():
    data = request.get_json()
    
    reviewID = data.get('reviewID')
    heading = data.get('heading')
    content = data.get('content')
    reviewType = data.get('reviewType')
    
    query = '''
        UPDATE Reviews
        SET heading = %s, content = %s, reviewType = %s
        WHERE reviewID = %s;
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query, (heading, content, reviewType, reviewID))
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