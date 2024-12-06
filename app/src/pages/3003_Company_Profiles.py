import logging
logger = logging.getLogger(__name__)
import datetime as dt
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
st.header('Edit and Updata Company Files')

# You can access the session state to make a more customized/personalized app experience
st.write(f"### Hi, {st.session_state['first_name']}.")


# get the feedbacks
try:
    companies = requests.get("http://api:4000/c/companies").json()
except:
    st.write("Could not to conncet to database to get companies and roles")
    
# Save DataFrame in session state
if "companies_df" not in st.session_state:
    st.session_state.companies_df = pd.DataFrame(companies)

# Title
st.title("Company and Role Manager")

# Filter settings
st.subheader("Filter and Highlight Options")
filter_by_time = st.checkbox("Filter by Last Updated Time", value=False)
hide_location = st.checkbox("Hide Location", value=False)
highlight_missing = st.checkbox("Highlight Missing Data", value=True)


# Time filter input
if filter_by_time:
    time_threshold = st.date_input(
        "Show records updated after:", dt.date(2024, 1, 1)
    )
    # Convert to datetime for comparison
    time_threshold = dt.datetime.combine(time_threshold, dt.datetime.min.time())
    


company_df = st.session_state.companies_df.copy()
company_df = company_df.rename(columns={'I.name': 'Industry', 'R.description':'Role Description', 'address':'Address', 'city':'City', 'country': 'Country', 'description':'Company Description', 'name': 'Company Name', 'roleName': 'Role Name', 'skillsRequired':'Skills Required', 'state_province':'State Province','updatedAT': 'Last Updated'})
display_columns = ["Company Name", "Last Updated", "Industry", "Company Description", "Role Name", "Skills Required", "Role Description", "Address", "City", "State Province", "Country"]
company_df = company_df[display_columns]
company_df['Last Updated'] = pd.to_datetime(company_df['Last Updated'])


# Apply filters and highlights
if filter_by_time:
    company_df = company_df[company_df["Last Updated"] > time_threshold]

if hide_location:
    company_df = company_df.drop(columns = ["Address", "City", "State Province", "Country"])
#st.dataframe(company_df)

if highlight_missing:
    def highlight_null_rows(df):
        def highlight_row(row):
            if row.isnull().any():
                return ['background-color: yellow'] * len(row)
            else:
                return [''] * len(row)
                
        return df.style.apply(highlight_row, axis=1)

    styled_df = highlight_null_rows(company_df)
    st.dataframe(styled_df)
else:
    st.dataframe(company_df)

'''
# Update or edit company profiles
st.subheader("Edit or Update Company Profiles")
company_id = st.selectbox("Select Company ID to Edit", company_df["CompanyID"])

# Fetch selected company data
selected_company = company_df[company_df["CompanyID"] == company_id].iloc[0]

# Form for editing
with st.form(key="edit_form"):
    company_name = st.text_input("Company Name", selected_company["CompanyName"])
    role = st.text_input("Role Description", selected_company["Role"])
    interview_details = st.text_area(
        "Interview Details", selected_company["InterviewDetails"]
    )
    submit_button = st.form_submit_button(label="Update Details")

    if submit_button:
        st.session_state.company_data.loc[
            st.session_state.company_data["CompanyID"] == company_id, "CompanyName"
        ] = company_name
        st.session_state.company_data.loc[
            st.session_state.company_data["CompanyID"] == company_id, "Role"
        ] = role
        st.session_state.company_data.loc[
            st.session_state.company_data["CompanyID"] == company_id, "InterviewDetails"
        ] = interview_details
        st.session_state.company_data.loc[
            st.session_state.company_data["CompanyID"] == company_id, "LastUpdated"
        ] = dt.datetime.now()
        st.session_state.company_data.loc[
            st.session_state.company_data["CompanyID"] == company_id, "Status"
        ] = "Complete" if role and interview_details else "Missing Data"

        st.success("Company details updated successfully!")

# Display updated data
st.subheader("Updated Company Data")
updated_company_df = st.session_state.company_data.copy()
st.dataframe(updated_company_df)
'''
