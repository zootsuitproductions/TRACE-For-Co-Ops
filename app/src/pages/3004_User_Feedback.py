import logging
logger = logging.getLogger(__name__)
import pandas as pd
import requests
import streamlit as st
from streamlit_extras.app_logo import add_logo
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
from modules.nav import SideBarLinks

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# set the header of the page
st.header('View and Categorize User Feedback')

# You can access the session state to make a more customized/personalized app experience
st.write(f"### Hi, {st.session_state['first_name']}.")

# get the feedbacks
try:
    feedback = requests.get("http://api:4000/f/feedback").json()
    st.dataframe(feedback)
except:
    st.write("Could not to conncet to database to get user feedback")
