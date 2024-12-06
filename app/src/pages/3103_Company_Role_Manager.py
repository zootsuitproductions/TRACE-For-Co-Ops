import streamlit as st

def company_role_manager():
    st.title("Company and Role Manager")
    st.subheader("Edit Company Profiles")
    st.write("Update information about companies and roles.")

    company = st.selectbox("Choose a company to update:", ["Company A", "Company B", "Company C"])
    st.text_area("Company Description", value="Edit the company's profile details here.")
    if st.button("Save Changes"):
        st.success(f"Profile for {company} updated.")

    st.subheader("Incomplete Data")
    st.write("Companies with missing or outdated profiles:")
    st.table([["Company", "Missing Details"],
              ["Company D", "Contact Information"],
              ["Company E", "Role Descriptions"]])

# Display the screen
company_role_manager()