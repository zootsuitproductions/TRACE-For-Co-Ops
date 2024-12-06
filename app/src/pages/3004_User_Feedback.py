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
except:
    st.write("Could not to conncet to database to get user feedback")

if "feedback_df" not in st.session_state:
    st.session_state.feedback_df = pd.DataFrame(feedback)

# title
st.title("User Feedback Management Interface")

# Sort by status
st.subheader("Filter or Sort Feedback")
filter_option = st.radio(
    "Select Filter or Sort Option",
    ["Default", "Show Only In Progress", "Show Only Implemented", "Show Only Rejected", "Sort by FeedbackID"],
    index=0,
)

# Apply sorting or filtering
filtered_feedback_df = st.session_state.feedback_df.copy()

if filter_option == "Show Only In Progress":
    filtered_feedback_df = filtered_feedback_df[
        filtered_feedback_df["status"] == "In Progress"
    ]
elif filter_option == "Show Only Implemented":
    filtered_feedback_df = filtered_feedback_df[
        filtered_feedback_df["status"] == "Implemented"
    ]
elif filter_option == "Show Only Rejected":
    filtered_feedback_df = filtered_feedback_df[
        filtered_feedback_df["status"] == "Rejected"
    ]
elif filter_option == "Sort by FeedbackID":
    filtered_feedback_df = filtered_feedback_df.sort_values('feedbackID')
    
else:
    filtered_feedback_df["status"] = pd.Categorical(
        filtered_feedback_df["status"],
        categories=["In Progress", "Implemented", "Rejected"],
        ordered=True,
    )
    filtered_feedback_df = filtered_feedback_df.sort_values("status")

# Select and rearrange columns
display_columns = ["status", "feedbackID", "userID", "timestamp", "header", "content"]
filtered_feedback_df = filtered_feedback_df[display_columns]

filtered_feedback_df = filtered_feedback_df.reset_index(drop=True)

# Display feedback table without index
st.subheader("Feedback List")
st.dataframe(filtered_feedback_df)


# Feedback update form
st.subheader("Update Feedback Status")
input_id = st.text_input("Enter Feedback ID")
new_status = st.radio(
    "Select New Status",
    ["In Progress", "Implemented", "Rejected"],
    index=0,
)


if st.button("Update Status"):
    # Validate ID
    if input_id.isdigit() and int(input_id) in st.session_state.feedback_df["feedbackID"].values:
        selected_id = int(input_id)
          
        # Update the status of the selected feedback in the current dataframe
        st.session_state.feedback_df.loc[
            st.session_state.feedback_df["feedbackID"] == selected_id, "status"
        ] = new_status
        st.success(f"Feedback ID {selected_id} status updated to '{new_status}'!")
        
        filtered_feedback_df.loc[filtered_feedback_df["feedbackID"] == int(input_id), "status"] = new_status
        # Update the status of the selected feedback in the SQL database
      
        # data which is used for update
        data = {
            "feedbackID": selected_id, 
            "status": new_status 
        }

        response = requests.put("http://api:4000/f/feedback", json=data)

        # reflect the response
        if response.status_code == 200:
            print("Success:", response.json())
        else:
            print("Error:", response.status_code, response.json())
            
    else:
        st.error("Please enter a valid Feedback ID.")

# Display updated feedback table
st.subheader("Updated Feedback List")

st.dataframe(filtered_feedback_df)


