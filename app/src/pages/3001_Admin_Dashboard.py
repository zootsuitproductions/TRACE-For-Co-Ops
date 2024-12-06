import logging
logger = logging.getLogger(__name__)
import requests
import pandas as pd
import streamlit as st
from streamlit_extras.app_logo import add_logo
import world_bank_data as wb
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
from modules.nav import SideBarLinks

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# set the header of the page
st.header('View Admin Dashboard')

# You can access the session state to make a more customized/personalized app experience
st.write(f"### Hi, {st.session_state['first_name']}.")

# get flagged reviews
try:
    flaggedreviews = requests.get("http://api:4000/r/flagged").json()
except:
    st.write("Could not to conncet to database to get flagged reviews")
    
if "flaggedreviews" not in st.session_state:
    st.session_state.flaggedreviews = pd.DataFrame(flaggedreviews)

# get reviews
try:
    reviews = requests.get("http://api:4000/r/reviews").json()
except:
    st.write("Could not to conncet to database to get flagged reviews")
    
if "reviews" not in st.session_state:
    st.session_state.reviews = pd.DataFrame(reviews)
    
    
# get comments
try:
    comments = requests.get("http://api:4000/r/comments").json()
except:
    st.write("Could not to conncet to database to get comments")
    
if "comments" not in st.session_state:
    st.session_state.comments = pd.DataFrame(comments)


# Sample data for demonstration
user_activity_data = {
    "Metric": ["Total Reviews", "Flagged Reviews", "Flagged Comments"],
    "Count": [len(st.session_state.reviews), len(st.session_state.flaggedreviews), len(st.session_state.comments)],
}



# Title and description
st.title("User Activity Dashboard")
st.write("An interface to manage user activity metrics, flagged reviews, and flagged comments.")

# Display user activity metrics
st.subheader("User Activity Metrics")
metrics_df = pd.DataFrame(user_activity_data)
st.table(metrics_df)


# Filterable list of flagged reviews
st.subheader("Flagged Comments List")

# Add filters
user_filter = st.selectbox("Filter by User ID", sorted(st.session_state.comments["userID"].unique()))
user_df = st.session_state.comments[st.session_state.comments["userID"]==user_filter ]
st.dataframe(user_df)
review_filter = st.selectbox("Filter by Review ID", sorted(st.session_state.comments["reviewID"].unique()))
review_df = st.session_state.comments[st.session_state.comments["reviewID"]==review_filter]
st.dataframe(review_df)






