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

# Function to fetch comments for a review
def fetch_comments(review_id):
    try:
        response = requests.get(f"http://api:4000/r/commentsByReview/{review_id}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to fetch comments for review {review_id}: {e}")
        return []

# Fetch companies
try:
    companies_response = requests.get("http://api:4000/r/companies")
    companies_response.raise_for_status()
    companies = companies_response.json()
except requests.exceptions.RequestException as e:
    st.error(f"Error fetching companies: {e}")
    companies = []

# Dropdown to select a company
if companies:
    company_names = [company['company_name'] for company in companies]
    selected_company_name = st.selectbox("Select a Company", company_names)

    # Fetch the selected company ID
    selected_company = next(company for company in companies if company['company_name'] == selected_company_name)
    selected_company_id = selected_company['companyID']

    # Fetch roles for the selected company
    try:
        roles_response = requests.get(f"http://api:4000/r/rolesByCompany/{selected_company_id}")
        roles_response.raise_for_status()
        roles = roles_response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching roles: {e}")
        roles = []

    # Dropdown to select a role
    if roles:
        role_names = [role['roleName'] for role in roles]
        selected_role_name = st.selectbox("Select a Role", role_names)

        # Fetch the selected role ID
        selected_role = next(role for role in roles if role['roleName'] == selected_role_name)
        selected_role_id = selected_role['roleID']

        # Review submission form
        with st.form("new_review_form"):
            st.subheader("Submit an Interview Experience")

            # Pre-fill the form with role info
            st.write(f"Reviewing interview for: {selected_role_name} at {selected_company_name}")

            new_heading = st.text_input("Review Heading")
            new_content = st.text_area("Content")
            new_review_type = "InterviewReport"

            submit_button = st.form_submit_button("Submit Review")

            # Handle form submission
            if submit_button:
                review_data = {
                    "roleID": selected_role_id,
                    "heading": new_heading,
                    "content": new_content,
                    "reviewType": new_review_type,
                    "userID": st.session_state['id']
                }

                try:
                    submit_response = requests.post("http://api:4000/r/submitReview", json=review_data)
                    submit_response.raise_for_status()
                    st.success("Review submitted successfully!")
                except requests.exceptions.RequestException as e:
                    st.error(f"Failed to submit review: {e}")
    
