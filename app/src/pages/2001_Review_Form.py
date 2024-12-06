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
<<<<<<< HEAD
=======
import requests
>>>>>>> 1a7805cdae2c5c2a740b690b50489d4caf4191d4

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# set the header of the page
<<<<<<< HEAD
st.header('Find Company and Position Reviews')
=======
st.header('Write A Co-Op Review')
>>>>>>> 1a7805cdae2c5c2a740b690b50489d4caf4191d4

# You can access the session state to make a more customized/personalized app experience
st.write(f"### Hi, {st.session_state['first_name']}.")

<<<<<<< HEAD
# get the countries from the world bank data
with st.echo(code_location='above'):
    countries:pd.DataFrame = wb.get_countries()
   
    st.dataframe(countries)

# the with statment shows the code for this block above it 
with st.echo(code_location='above'):
    arr = np.random.normal(1, 1, size=100)
    test_plot, ax = plt.subplots()
    ax.hist(arr, bins=20)

    st.pyplot(test_plot)


with st.echo(code_location='above'):
    slim_countries = countries[countries['incomeLevel'] != 'Aggregates']
    data_crosstab = pd.crosstab(slim_countries['region'], 
                                slim_countries['incomeLevel'],  
                                margins = False) 
    st.table(data_crosstab)
=======
st.header("Submit a New Review")

# Create a form
with st.form("new_review_form"):
    role_id = st.selectbox("Role", options=[1, 2, 3], format_func=lambda x: f"Role {x}")
    review_type = st.selectbox("Review Type", options=["Experience", "Feedback", "Complaint"])
    heading = st.text_input("Heading", placeholder="Enter a brief heading for your review")
    content = st.text_area("Content", placeholder="Write your review here...")
    published_at = st.date_input("Published At")
    
    # Form submit button
    submitted = st.form_submit_button("Submit")

if submitted:
    # Step 2: Prepare the data
    new_review = {
        "userID": st.session_state["id"],  # Assuming the user's ID is stored in session_state
        "roleID": role_id,
        "publishedAt": published_at.isoformat(),  # Convert to ISO format
        "reviewType": review_type,
        "heading": heading,
        "content": content,
        "views": 0,  # Default value
        "likes": 0,  # Default value
        "isFlagged": False  # Default value
    }

    # Step 3: Send the data to the API
    try:
        response = requests.post("http://api:4000/r/addReview", json=new_review)
        response.raise_for_status()
        st.success("Review submitted successfully!")
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
>>>>>>> 1a7805cdae2c5c2a740b690b50489d4caf4191d4
