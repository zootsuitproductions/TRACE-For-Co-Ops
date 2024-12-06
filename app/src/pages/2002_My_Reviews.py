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

# Display personalized greeting
st.write(f"### Hi, {st.session_state['first_name']}!")

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

# If there are reviews, display them
if reviews:
    st.subheader("Your Reviews")
    for review in reviews:
        with st.container():
            # Fetch role and company details
            role_name, company_name = fetch_role_and_company(review['roleID'])

            # Display review details
            st.markdown(f"### {review['heading']} ({review['reviewType']})")
            st.markdown(f"**Published At:** {review['publishedAt']}")
            st.markdown(f"**Views:** {review['views']}  |  **Likes:** {review['likes']}")
            st.markdown(f"**Role:** {role_name} at **{company_name}**")
            st.markdown(f"**Content:** {review['content']}")

            # Fetch and display comments
            comments = fetch_comments(review['reviewID'])
            st.markdown("#### Comments:")
            if comments:
                for comment in comments:
                    st.markdown(f"- **User {comment['userID']}**: {comment['content']} (Likes: {comment['likes']})")
            else:
                st.markdown("*No comments yet.*")

            # Display the edit button
            edit_button = st.button(f"Edit Review {review['reviewID']}")

            if edit_button:
                # If the button is clicked, show the edit form
                with st.form(key=f'edit_review_{review["reviewID"]}'):
                    st.subheader("Edit this Review")

                    # Pre-fill the form with the current review details
                    new_heading = st.text_input("Heading", value=review["heading"])
                    new_content = st.text_area("Content", value=review["content"])
                    new_review_type = st.selectbox("Review Type", ["Experience", "Feedback", "Other"], index=["Experience", "Feedback", "Other"].index(review["reviewType"]))

                    submit_button = st.form_submit_button(label="Update Review")

                    # Handle form submission
                    if submit_button:
                        update_review_data = {
                            "reviewID": review["reviewID"],
                            "heading": new_heading,
                            "content": new_content,
                            "reviewType": new_review_type
                        }

                        try:
                            update_response = requests.put(f'http://api:4000/r/updateReview', json=update_review_data)
                            update_response.raise_for_status()
                            st.success("Review updated successfully!")
                        except requests.exceptions.RequestException as e:
                            st.error(f"Failed to update review: {e}")

            st.markdown("---")
else:
    st.info("No reviews found. Start by adding your first review!")
