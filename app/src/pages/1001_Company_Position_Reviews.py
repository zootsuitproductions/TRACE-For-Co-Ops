import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks
import requests

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# set the header of the page
st.header('Find Company and Position Reviews')

# You can access the session state to make a more customized/personalized app experience
st.write(f"### Hi, {st.session_state['first_name']}.")

results = requests.get(f'http://api:4000/s/companiesWithReviews').json()

# Extract company names into a list
company_names = [item["CompanyName"] for item in results]

# Display a dropdown menu with company names
selected_company = st.selectbox("Select a Company:", company_names)
