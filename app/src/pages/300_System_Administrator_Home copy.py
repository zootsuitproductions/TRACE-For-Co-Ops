import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome System Administrator, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('View Admin Dashboard', 
             type='primary', 
             use_container_width=True):
    st.switch_page('pages/3001_Admin_Dashboard.py')

if st.button('View and Moderate Flagged Posts', 
             type='primary', 
             use_container_width=True):
    st.switch_page('pages/3002_Flagged_Posts.py')

if st.button('Edit and Update Company Profiles', 
             type='primary', 
             use_container_width=True):
    st.switch_page('pages/3003_Company_Profiles.py')

if st.button('View and Categorize User Feedback', 
             type='primary', 
             use_container_width=True):
    st.switch_page('pages/3004_User_Feedback.py')
    
if st.button('View Analytics and Trends', 
             type='primary', 
             use_container_width=True):
    st.switch_page('pages/3005_Analytics_and_Trends.py')

