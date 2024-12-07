import logging
import requests
import streamlit as st
from modules.nav import SideBarLinks

# Set up logger
logger = logging.getLogger(__name__)

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# Set the header of the page
st.header("Find Company and Position Reviews")

# Access the session state for personalization
st.write(f"### Hi, {st.session_state.get('first_name', 'Guest')}!")


# Function to add a comment to a review
def add_comment(review_id, user_id, content):
    try:
        response = requests.post(
            f"http://api:4000/r/addComment",
            json={
                "reviewID": review_id,
                "userID": user_id,
                "content": content,
            },
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to add comment to review {review_id}: {e}")
        return None


# Function to like a review
def like_review(review_id):
    try:
        response = requests.post(f"http://api:4000/s/review/{review_id}/like")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to like review {review_id}: {e}")
        return None


# Function to flag a review
def flag_review(review_id):
    try:
        response = requests.post(f"http://api:4000/s/review/{review_id}/flag")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to flag review {review_id}: {e}")
        return None


# Fetch companies with reviews
try:
    results = requests.get("http://api:4000/s/companiesWithReviews").json()
    company_names = [item["CompanyName"] for item in results]
except Exception as e:
    st.error("Failed to fetch company data. Please try again later.")
    logger.error(f"Error fetching companies: {e}")
    company_names = []

# Dropdown for selecting a company
if company_names:
    selected_company = st.selectbox("Select a Company:", company_names)

    if selected_company:
        # Fetch reviews for the selected company
        try:
            reviews = requests.get(
                f"http://api:4000/s/reviewsForCompany/{selected_company}"
            ).json()
        except Exception as e:
            st.error("Failed to fetch reviews. Please try again later.")
            logger.error(f"Error fetching reviews: {e}")
            reviews = []

        # Display reviews
        if reviews:
            st.write("### Reviews for this Company:")

            for review in reviews:
                st.markdown(
                    f"""
                    <div style="
                        border: 1px solid #ddd;
                        border-radius: 8px;
                        padding: 20px;
                        margin-bottom: 20px;
                        background-color: #f9f9f9;
                        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
                    ">
                        <h4>Review by User {review['userID']}</h4>
                        <p><b>Role ID:</b> {review['roleID']}</p>
                        <p><b>Published At:</b> {review['publishedAt']}</p>
                        <p><b>Heading:</b> {review['heading']}</p>
                        <p><b>Content:</b> {review['content']}</p>
                        <p><b>Views:</b> {review['views']} | <b>Likes:</b> {review['likes']}</p>
                        <hr>
                """,
                    unsafe_allow_html=True,
                )

                st.markdown('<div style="padding: 10px;">', unsafe_allow_html=True)

                # Fetch and display comments
                try:
                    comments = requests.get(
                        f"http://api:4000/r/commentsByReview/{review['reviewID']}"
                    ).json()
                except Exception as e:
                    st.error("Failed to fetch comments. Please try again later.")
                    logger.error(f"Error fetching comments: {e}")
                    comments = []

                if comments:
                    st.markdown("#### Comments:", unsafe_allow_html=True)
                    for comment in comments:
                        st.markdown(
                            f"""
                            <div style="
                                margin-left: 10px;
                                border-left: 2px solid #ccc;
                                padding-left: 10px;
                                margin-bottom: 10px;
                            ">
                                <p><b>User {comment['userID']}:</b> {comment['content']} <br />
                                <b>Likes:</b> {comment['likes']}</p>
                            </div>
                            """,
                            unsafe_allow_html=True,
                        )
                else:
                    st.markdown("<p>No comments yet.</p>", unsafe_allow_html=True)

                # Add a form to post a new comment
                with st.form(key=f"add_comment_form_{review['reviewID']}"):
                    st.write("#### Add a Comment")
                    new_comment_content = st.text_area(
                        "Your Comment", key=f"comment_content_{review['reviewID']}"
                    )
                    submit_comment_button = st.form_submit_button(label="Post Comment")

                    if submit_comment_button and new_comment_content:
                        user_id = st.session_state.get(
                            "id"
                        )  # Assuming user ID is stored in session state
                        comment_response = add_comment(
                            review["reviewID"], user_id, new_comment_content
                        )
                        if comment_response:
                            st.success("Comment added successfully!")
                        else:
                            st.error("Failed to post comment. Please try again.")

                st.markdown("</div>", unsafe_allow_html=True)  # Close inner div

                st.markdown("</div>", unsafe_allow_html=True)  # Close outer div
        else:
            st.write("No reviews available for this company.")
else:
    st.write("No companies available to select.")
