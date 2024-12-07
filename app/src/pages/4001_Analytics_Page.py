import logging

logger = logging.getLogger(__name__)
import requests
import pandas as pd
import streamlit as st
from streamlit_extras.app_logo import add_logo
import matplotlib.pyplot as plt

# Safe initialization of session state variables
if "first_name" not in st.session_state:
    st.session_state.first_name = "Guest"

# Call the SideBarLinks from the nav module
from modules.nav import SideBarLinks

SideBarLinks()

# Set the header of the page
st.header("View Analytics and Trends")
st.write(f"### Hi, {st.session_state['first_name']}.")

# Fetch industries
industries = []
try:
    industries = requests.get("http://api:4000/c/industries").json()
except Exception as e:
    st.write(f"Error: {e}")
    st.write("Could not connect to database to get industries.")
if "industries" not in st.session_state:
    st.session_state.industries = pd.DataFrame(industries)

# Fetch reviews
reviews = []
try:
    reviews = requests.get("http://api:4000/c/reviews").json()
except Exception as e:
    st.write(f"Error: {e}")
    st.write("Could not connect to database to get reviews.")
if "reviews" not in st.session_state:
    st.session_state.reviews = pd.DataFrame(reviews)

# Title
st.title("Trends in Student Reviews and Companies")
st.subheader("Trend Data")

# Plot trends if data is valid
if not st.session_state.industries.empty and not st.session_state.reviews.empty:
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(
        st.session_state.reviews["Industry"],
        st.session_state.reviews["NumReviews"],
        label="reviews",
        marker="o",
    )
    ax.plot(
        st.session_state.industries["Industry"],
        st.session_state.industries["NumCompany"],
        label="Companies",
        marker="o",
    )
    ax.set_ylabel("Count")
    ax.set_title("Trends by Category")
    ax.set_xticklabels(st.session_state.industries["Industry"], rotation=45, ha="right")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)
else:
    st.write("Insufficient data to display trends.")

# Actionable Insights
st.subheader("Actionable Insights")
if not st.session_state.industries.empty:
    most_companies = st.session_state.industries.sort_values("NumCompany").iloc[-1]
    st.write(
        f"**Industry with Most Companies**: {most_companies['Industry']} ({most_companies['NumCompany']} companies)"
    )

if not st.session_state.reviews.empty:
    most_reviews = st.session_state.reviews.sort_values("NumReviews").iloc[-1]
    st.write(
        f"**Industry with Most Reviews**: {most_reviews['Industry']} ({most_reviews['NumReviews']} reviews)"
    )

# Display Data Table
if "Industry" in st.session_state.industries and "Industry" in st.session_state.reviews:
    df = pd.merge(st.session_state.industries, st.session_state.reviews, on="Industry")
    st.subheader("Data Table")
    st.dataframe(df)
else:
    st.write("Data table cannot be displayed due to missing columns.")
