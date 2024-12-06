import logging
logger = logging.getLogger(__name__)
import pandas as pd
import streamlit as st
from streamlit_extras.app_logo import add_logo
import requests
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
import plotly.express as px
from modules.nav import SideBarLinks

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# set the header of the page
st.header('View and Moderate Flagged Posts')

# You can access the session state to make a more customized/personalized app experience
st.write(f"### Hi, {st.session_state['first_name']}.")

# get flagged posts
try:
    reviews = requests.get("http://api:4000/r/flagged").json()
except:
    st.write("Could not to conncet to database to get flagged reviews")

if "reviews" not in st.session_state:
    st.session_state.reviews = pd.DataFrame(reviews)

if "History" not in st.session_state:
    st.session_state.History = []
    
if "timestamp" not in st.session_state:
    st.session_state.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Streamlit app
st.title("Flagged Posts Review Interface")

# Display flagged posts in a table
st.subheader("Flagged Posts")
selected_post_id = st.selectbox(
    "Select a review to review:",
    st.session_state.reviews["reviewID"],
    format_func=lambda x: f"Review {x}: {st.session_state.reviews.loc[st.session_state.reviews['reviewID'] == x, 'heading'].values[0]}"
)


# Show details of the selected post
selected_post = st.session_state.reviews[st.session_state.reviews["reviewID"] == selected_post_id].iloc[0]
st.write(f"**Review ID:** {selected_post['reviewID']}")
st.write(f"**Content:** {selected_post['content']}")
st.write(f"**Review Type:** {selected_post['reviewType']}")

# Action options
st.subheader("Actions")
action = st.radio("Select an action to perform:", ["None", "Approve", "Edit", "Remove"],index = 0)
# Execute selected action

if action == "Approve":
    st.session_state.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {
            "reviewID": selected_post_id, 
            "isFlagged": False
        }

    response = requests.put("http://api:4000/r/approveflagged", json=data)

    # reflect the response
    if response.status_code == 200:
        print("Success:", response.json())
    else:
        print("Error:", response.status_code, response.json())
    st.success(f"Review {selected_post_id} approved.")
    


elif action == "Edit":
    new_content = st.text_area("Edit Content", selected_post['content'])
    if st.button("Save Changes"):
        st.session_state.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.session_state.reviews.loc[st.session_state.reviews["reviewID"] == selected_post_id, "Content"] = new_content
        data = {
            "reviewID": selected_post_id, 
            "content": new_content
        }

        response = requests.put("http://api:4000/r/editflagged", json=data)

        # reflect the response
        if response.status_code == 200:
            print("Success:", response.json())
        else:
            print("Error:", response.status_code, response.json())
        st.success(f"Post {selected_post_id} updated.")

elif action == "Remove":
    st.session_state.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {
        "reviewID": selected_post_id, 
    }
    response = requests.delete("http://api:4000/r/removeflagged", json=data)
    if response.status_code == 200:
        print("Success:", response.json())
    else:
        try:
            error_message = response.json()
        except ValueError:
            error_message = "No error details provided"
        print("Error:", response.status_code, error_message)
    st.warning(f"Review {selected_post_id} removed.")

st.session_state.History.append(f"- {st.session_state.timestamp} - Review {selected_post_id} - {action}")
# Display action history
st.subheader("Action History")
for entry in st.session_state.History:
    st.write(entry)

'''
#st.write(history)
if selected_post_id is not Nonest.session_state.History[selected_post_id]:
    history = st.session_state.History[selected_post_id]
    for entry in history:
        st.write(f"- {entry['Timestamp']} - {entry['Action']} ({entry.get('Reason', 'No Reason')})")
else:
    st.write("No actions taken yet.")
'''
