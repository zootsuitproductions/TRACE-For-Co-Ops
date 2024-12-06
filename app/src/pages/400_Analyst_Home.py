import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Analyst, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')


if st.button('View Analytics and Trends', 
             type='primary', 
             use_container_width=True):
    st.switch_page('pages/4001_Analytics_Page.py')

if st.button('View Feedback Data', 
             type='primary', 
             use_container_width=True):
    st.switch_page('pages/4002_Feedback_Data.py')

