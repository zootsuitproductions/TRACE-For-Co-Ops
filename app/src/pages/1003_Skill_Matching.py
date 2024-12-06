import logging
import requests
import streamlit as st
from modules.nav import SideBarLinks
import pandas as pd

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# Set the header of the page
st.header('Find positions with matching skills')

# You can access the session state to make a more customized/personalized app experience
st.write(f"### Hi, {st.session_state['first_name']}.")

# Fetch the list of possible skills from the API
skills = requests.get('http://api:4000/s/possibleSkills').json()


# Extract and split skillsRequired into a set of unique skills
skillsRequired = set()
for item in skills:
    # Split the skills by commas and strip any surrounding whitespace
    skills = item["skillsRequired"].split(",")
    # Add each skill to the set
    skillsRequired.update(skill.strip() for skill in skills)


# Display a dropdown menu with company names
selected_skill = st.selectbox("Select a Skill:", skillsRequired)

# If the user enters a skill
if selected_skill:
    try:
        # Send the GET request to the API endpoint with the skill
        response = requests.get(f'http://api:4000/s/rolesForSkill/{selected_skill}')
        
        # Check if the response is successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            
            # If there is data, display it in a table
            if data:
                # Convert the data into a Pandas DataFrame for easy display
                df = pd.DataFrame(data, columns=['roleName', 'companyName', 'skillsRequired'])
                st.write(f"### Roles that require the skill: {selected_skill}")
                st.dataframe(df)  # Display the DataFrame in Streamlit table format
            else:
                st.warning(f"No roles found that require the skill '{selected_skill}'.")
        else:
            st.error("Failed to fetch data from the server. Please try again later.")
    
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
