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


company_df = company_df.rename(columns={'companyID':'Company ID','I.name': 'Industry', 'R.description':'Role Description', 'address':'Address', 'city':'City', 'country': 'Country', 'description':'Company Description', 'name': 'Company Name', 'roleName': 'Role Name', 'skillsRequired':'Skills Required', 'state_province':'State Province','updatedAT': 'Last Updated'})
display_columns = ["Company ID", "Company Name", "Last Updated", "Industry", "Company Description", "Role Name", "Skills Required", "Role Description", "Address", "City", "State Province", "Country",  'Industry ID', 'Role ID','Location ID']
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
            # Check for NaN or empty strings in the row
            if row.isnull().any() or row.eq('').any():
                return ['background-color: yellow'] * len(row)
            else:
                return [''] * len(row)

        # Apply the highlighting function row-wise
        return df.style.apply(highlight_row, axis=1)

    styled_df = highlight_null_rows(company_df)
    st.dataframe(styled_df)
else:
    st.dataframe(company_df)

st.subheader("Update Company Profiles")

st.subheader("Delete Company Profiles")

st.subheader("Edit Company Profiles")


company_id = st.selectbox("Select Company ID", sorted(company_df["Company ID"].unique()))
industry_id = st.selectbox("Select Industry ID", sorted(company_df["Industry ID"].unique()))
role_id = st.selectbox("Select Role ID", sorted(company_df["Role ID"].unique()))
location_id = st.selectbox("Select Location ID", sorted(company_df["Location ID"].unique()))



if "flg" not in st.session_state:
    st.session_state.flg = False
if "ssh" not in st.session_state:
    st.session_state.ssh = False
if "company_df" not in st.session_state:
    st.session_state.company_df = company_df


if st.button("Confirm") and not st.session_state.flg:
    selected_company = company_df[company_df["Company ID"] == company_id]
    filtered_company = selected_company[
        (selected_company["Industry ID"] == industry_id) &
        (selected_company["Role ID"] == role_id) &
        (selected_company["Location ID"] == location_id)
    ]
    if filtered_company.empty:
        st.warning("No company meets your requirements. Please select again.")
    else:
        st.session_state.final_company = filtered_company
        st.dataframe(filtered_company)
        st.session_state.flg = True


if st.session_state.flg:
    with st.form(key="edit_form"):
        company_name = st.text_input("Company Name", st.session_state.final_company["Company Name"].iloc[0], disabled=True)
        company_discription = st.text_input("Company Description", st.session_state.final_company["Company Description"].iloc[0])
        skill = st.text_input("Skills Required", st.session_state.final_company["Skills Required"].iloc[0])
        role_description = st.text_input("Role Description", st.session_state.final_company["Role Description"].iloc[0])
        
        submitted = st.form_submit_button(label="Update Details")
        if submitted:
            condition = (
                (st.session_state.company_df["Company ID"] == company_id) &
                (st.session_state.company_df["Industry ID"] == industry_id) &
                (st.session_state.company_df["Role ID"] == role_id) &
                (st.session_state.company_df["Location ID"] == location_id)
            )
            
            st.session_state.company_df.loc[(st.session_state.company_df["Company ID"] == company_id), "Company Description"] = company_discription
            st.session_state.company_df.loc[(st.session_state.company_df["Company ID"] == company_id) & (st.session_state.company_df["Role ID"] == role_id), "Skills Required"] = skill
            st.session_state.company_df.loc[(st.session_state.company_df["Company ID"] == company_id) & (st.session_state.company_df["Role ID"] == role_id), "Role Description"] = role_description
            

            data = {
                "companyID": company_id, 
                "RoleID": role_id,
                "Company Description": company_discription,
                "Skills Required": skill, 
                "Role Description": role_description
            }
            data = {
                key: (int(value) if isinstance(value, np.int64) else value)
                for key, value in data.items()
            }
         
            response_company = requests.put("http://api:4000/c/companies/companies", json=data)
            if response_company.status_code == 200:
                print("Success:", response_company.json())
            else:
                print("Error:", response_company.status_code, response_company.json())
                
            response_role = requests.put("http://api:4000/c/companies/roles", json=data)
            if response_role.status_code == 200:
                print("Success:", response_role.json())
            else:
                print("Error:", response_role.status_code, response_role.json())
            
            st.session_state.ssh = True
            


if st.session_state.ssh:
    st.success("Company details updated successfully!")
    st.subheader("Updated Company Data")
    st.dataframe(st.session_state.company_df)