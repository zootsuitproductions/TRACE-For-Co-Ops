import streamlit as st
import logging

logging.basicConfig(level=logging.INFO)

def alex_admin_home():
    st.title("Welcome, Alex (Admin)")
    st.write("Choose one of the following options to access admin functionalities:")

    if st.button("Go to Admin Dashboard", type="primary", use_container_width=True):
        logging.info("Navigating to 3101_Admin_Dashboard")
        st.switch_page('pages/3101_Admin_Dashboard.py')

    if st.button("Go to Content Moderation Panel", type="primary", use_container_width=True):
        logging.info("Navigating to 3102_Content_Moderation")
        st.switch_page('pages/3102_Content_Moderation.py')

    if st.button("Go to Company and Role Manager", type="primary", use_container_width=True):
        logging.info("Navigating to 3103_Company_Role_Manager")
        st.switch_page('pages/3103_Company_Role_Manager.py')

    if st.button("Go to Feedback and Feature Tracker", type="primary", use_container_width=True):
        logging.info("Navigating to 3104_Feedback_Feature_Tracker")
        st.switch_page('pages/3104_Feedback_Feature_Tracker.py')

    if st.button("Go to Analytics and Trends Page", type="primary", use_container_width=True):
        logging.info("Navigating to 3105_Analytics_Trends")
        st.switch_page('pages/3105_Analytics_Trends.py')

alex_admin_home()