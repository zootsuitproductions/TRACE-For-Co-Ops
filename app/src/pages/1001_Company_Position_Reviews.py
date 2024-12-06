import logging
import requests
import streamlit as st
from modules.nav import SideBarLinks

# Set up logger
logger = logging.getLogger(__name__)

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# Set the header of the page
st.header('Find Company and Position Reviews')

# Access the session state for personalization
st.write(f"### Hi, {st.session_state['first_name']}.")

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
        return response.json()  # Assuming the API returns the created comment or success message
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to add comment to review {review_id}: {e}")
        return None

# Fetch companies with reviews
try:
    results = requests.get('http://api:4000/s/companiesWithReviews').json()
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
            reviews = requests.get(f'http://api:4000/s/reviewsForCompany/{selected_company}').json()
        except Exception as e:
            st.error("Failed to fetch reviews. Please try again later.")
            logger.error(f"Error fetching reviews: {e}")
            reviews = []

        # Display reviews
        if reviews:
            st.write("### Reviews for this Company:")

            for review in reviews:
                st.subheader(f"Review by User {review['userID']}")
                st.write(f"**Role ID:** {review['roleID']}")
                st.write(f"**Published At:** {review['publishedAt']}")
                st.write(f"**Heading:** {review['heading']}")
                st.write(f"**Content:** {review['content']}")
                st.write(f"**Views:** {review['views']} | **Likes:** {review['likes']}")
                st.write("---")

                # Fetch comments for the current review
                try:
                    comments = requests.get(f"http://api:4000/r/commentsByReview/{review['reviewID']}").json()
                except Exception as e:
                    st.error("Failed to fetch comments. Please try again later.")
                    logger.error(f"Error fetching comments: {e}")
                    comments = []

                # Display comments
                if comments:
                    st.write("#### Comments:")
                    for comment in comments:
                        st.write(f"- **User {comment['userID']}**: {comment['content']} (Likes: {comment['likes']})")
                else:
                    st.write("No comments yet for this review.")

                # Add a form to post a new comment
                with st.form(key=f"add_comment_form_{review['reviewID']}"):
                    st.subheader("Add a Comment")
                    new_comment_content = st.text_area("Your Comment", key=f"comment_content_{review['reviewID']}")
                    submit_comment_button = st.form_submit_button(label="Post Comment")

                    if submit_comment_button and new_comment_content:
                        user_id = st.session_state.get("id")  # Assuming user ID is stored in session state
                        comment_response = add_comment(review['reviewID'], user_id, new_comment_content)
                        if comment_response:
                            st.success("Comment added successfully!")
                            # Optionally refresh comments
                            comments.append({
                                "userID": user_id,
                                "content": new_comment_content,
                                "likes": 0,
                            })
                        else:
                            st.error("Failed to post comment. Please try again.")
        else:
            st.write("No reviews available for this company.")
else:
    st.write("No companies available to select.")
