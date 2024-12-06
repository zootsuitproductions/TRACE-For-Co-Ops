import logging
logger = logging.getLogger(__name__)
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
st.header('View and Moderate Flagged Posts')

# You can access the session state to make a more customized/personalized app experience
st.write(f"### Hi, {st.session_state['first_name']}.")

import streamlit as st
import pandas as pd
from datetime import datetime

# Sample data for flagged posts
sample_data = [
    {"Post ID": 1, "Content": "This is a flagged post.", "Flag Reason": "Inappropriate Language", "History": []},
    {"Post ID": 2, "Content": "Another flagged post here.", "Flag Reason": "Spam", "History": []},
]

# Convert sample data to DataFrame
posts_df = pd.DataFrame(sample_data)

# Function to log actions
def log_action(post_id, action, reason=None):
    for post in sample_data:
        if post["Post ID"] == post_id:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            post["History"].append({"Action": action, "Reason": reason, "Timestamp": timestamp})

# Streamlit app
st.title("Flagged Posts Review Interface")

# Display flagged posts
st.subheader("Flagged Posts")

for index, row in posts_df.iterrows():
    st.write(f"**Post ID:** {row['Post ID']}")
    st.write(f"**Content:** {row['Content']}")
    st.write(f"**Flag Reason:** {row['Flag Reason']}")

    # Buttons for actions
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button(f"Approve Post {row['Post ID']}"):
            log_action(row['Post ID'], "Approved")
            st.success(f"Post {row['Post ID']} approved.")

    with col2:
        if st.button(f"Edit Post {row['Post ID']}"):
            new_content = st.text_area(f"Edit Content for Post {row['Post ID']}", row['Content'])
            if st.button(f"Save Changes to Post {row['Post ID']}"):
                posts_df.loc[index, "Content"] = new_content
                log_action(row['Post ID'], "Edited", f"Updated content to: {new_content}")
                st.success(f"Post {row['Post ID']} updated.")

    with col3:
        if st.button(f"Remove Post {row['Post ID']}"):
            log_action(row['Post ID'], "Removed")
            st.warning(f"Post {row['Post ID']} removed.")

    # Display action history
    st.write("**Action History:**")
    history = row['History']
    if history:
        for entry in history:
            st.write(f"- {entry['Timestamp']} - {entry['Action']} ({entry.get('Reason', 'No Reason')})")
    else:
        st.write("No actions taken yet.")

    st.divider()

st.write("**Note:** This interface uses sample data. Replace with actual data for production.")
