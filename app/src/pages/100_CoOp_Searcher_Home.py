import logging
logger = logging.getLogger(__name__)
import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Co-op searcher, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('View Company and Position Reviews', 
             type='primary', 
             use_container_width=True):
    st.switch_page('pages/1001_Company_Position_Reviews.py')

if st.button('View Interview Information', 
             type='primary', 
             use_container_width=True):
    st.switch_page('pages/1002_Interview_Information.py')

if st.button('View Positions with Matching Skills', 
             type='primary', 
             use_container_width=True):
    st.switch_page('pages/1003_Skill_Matching.py')

if st.button('Enter My Interview Experiences', 
             type='primary', 
             use_container_width=True):
    st.switch_page('pages/1004_Enter_Interview_Info.py')
