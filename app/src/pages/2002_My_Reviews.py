import logging
import pandas as pd
import streamlit as st
from streamlit_extras.app_logo import add_logo
import requests
import plotly.express as px
from modules.nav import SideBarLinks

# Initialize logger
logger = logging.getLogger(__name__)

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# Set the header of the page
st.header('My Reviews')

# Fetch the user's reviews
try:
    response = requests.get(f'http://api:4000/r/reviewsByUser/{st.session_state["id"]}')
    response.raise_for_status()
    reviews = response.json()
except requests.exceptions.RequestException as e:
    st.error(f"Failed to fetch reviews: {e}")
    reviews = []

# Function to fetch role and company details for each review
def fetch_role_and_company(role_id):
    try:
        response = requests.get(f"http://api:4000/r/roleDetails/{role_id}")
        response.raise_for_status()
        role_data = response.json()
        return role_data.get('roleName', 'N/A'), role_data.get('companyName', 'N/A')
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to fetch role and company for role ID {role_id}: {e}")
        return 'N/A', 'N/A'

# Function to fetch comments for a review
def fetch_comments(review_id):
    try:
        response = requests.get(f"http://api:4000/r/commentsByReview/{review_id}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to fetch comments for review {review_id}: {e}")
        return []

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

# If there are reviews, display them
# Display the edit form for the currently selected review
if "editing_review_id" not in st.session_state:
    st.session_state["editing_review_id"] = None

if reviews:
    for review in reviews:
        with st.container():
            # Fetch role and company details
            role_name, company_name = fetch_role_and_company(review['roleID'])

            # Display review details
            st.markdown(f"### {review['reviewType']}")   # Review type in bold above the title
            st.markdown(f"**Role:** {role_name} at **{company_name}**")
            st.markdown(f"#### {review['heading']}") 
            st.markdown(f"{review['content']}")
            st.markdown(f"**Views:** {review['views']}  |  **Likes:** {review['likes']}")
            

            st.markdown(f"**Published At:** {review['publishedAt']}")
            # Fetch and display comments
            comments = fetch_comments(review['reviewID'])
            st.markdown("#### Comments:")
            if comments:
                for comment in comments:
                    st.markdown(f"- **User {comment['userID']}**: {comment['content']} (Likes: {comment['likes']})")
            else:
                st.markdown("*No comments yet.*")

            
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


            # Display the edit button
            edit_button = st.button(
                f"Edit Review {review['reviewID']}",
                key=f"edit_button_{review['reviewID']}"
            )

            if edit_button:
                # Set the review ID to session state for editing
                st.session_state["editing_review_id"] = review["reviewID"]

            # If this review is being edited, display the edit form
            if st.session_state["editing_review_id"] == review["reviewID"]:
                with st.form(key=f'edit_review_form_{review["reviewID"]}'):
                    st.subheader("Edit this Review")

                    # Pre-fill the form with the current review details
                    new_heading = st.text_input("Heading", value=review["heading"])
                    new_content = st.text_area("Content", value=review["content"])

                    submit_button = st.form_submit_button(label="Update Review")

                    # Handle form submission
                    if submit_button:
                        update_review_data = {
                            "reviewID": review["reviewID"],
                            "heading": new_heading,
                            "content": new_content,
                        }

                        try:
                            update_response = requests.put(
                                f'http://api:4000/r/updateReview', 
                                json=update_review_data
                            )
                            update_response.raise_for_status()
                            st.success("Review updated successfully!")
                            # Reset the editing state
                            st.session_state["editing_review_id"] = None
                        except requests.exceptions.RequestException as e:
                            st.error(f"Failed to update review: {e}")

                # Add a cancel button to stop editing
                if st.button(f"Done {review['reviewID']}", key=f"cancel_button_{review['reviewID']}"):
                    st.session_state["editing_review_id"] = None

             # Add a Delete button
            delete_button = st.button(f"Delete Review {review['reviewID']}", key=f"delete_button_{review['reviewID']}")
            
            if delete_button:
                # Confirm deletion before making the API request
                confirm_delete = "Delete"
                
                if confirm_delete == "Delete":
                    try:
                        delete_response = requests.delete(
                            f'http://api:4000/r/deleteReview/{review["reviewID"]}'
                        )
                        delete_response.raise_for_status()
                        st.success("Review deleted successfully!")
                        # Optionally, refresh the page or remove the deleted review from the list
                        reviews = [rev for rev in reviews if rev["reviewID"] != review["reviewID"]]
                    except requests.exceptions.RequestException as e:
                        st.error(f"Failed to delete review: {e}")

            st.markdown("---")
else:
    st.info("No reviews found. Start by adding your first review!")
