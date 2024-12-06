import logging
logger = logging.getLogger(__name__)
import requests
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
st.header('View Analytics and Trends')

# You can access the session state to make a more customized/personalized app experience
st.write(f"### Hi, {st.session_state['first_name']}.")
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# get industries
try:
    industries = requests.get("http://api:4000/c/industries").json()
except:
    st.write("Could not to conncet to database to get industries")
    
if "industries" not in st.session_state:
    st.session_state.industries = pd.DataFrame(industries)
    
# get reviews
try:
    reviews = requests.get("http://api:4000/c/reviews").json()
except:
    st.write("Could not to conncet to database to get reviews")
    
if "industries" not in st.session_state:
    st.session_state.industries = pd.DataFrame(industries)
if "reviews" not in st.session_state:
    st.session_state.reviews = pd.DataFrame(reviews)

# Title
st.title("Trends in Student Reviews and Companies")
st.subheader("Trend Data")
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(st.session_state.reviews["Industry"], st.session_state.reviews['NumReviews'], label="reviews", marker="o")
ax.plot(st.session_state.industries["Industry"], st.session_state.industries['NumCompany'], label="Companies", marker="o")
ax.set_ylabel("Count")
ax.set_title("Trends by Category")
ax.set_xticklabels(st.session_state.industries["Industry"], rotation=45, ha="right")
ax.legend()
ax.grid(True)
st.pyplot(fig)

# Actionable Insights
st.subheader("Actionable Insights")
most_companies = st.session_state.industries.sort_values("NumCompany").iloc[-1]
st.write(f"**Industry with Most Companies**: {most_companies['Industry']} ({most_companies['NumCompany']} companies)")


most_reviews = st.session_state.reviews.sort_values("NumReviews").iloc[-1]
st.write(f"**Industry with Most Reviews**: {most_reviews['Industry']} ({most_reviews['NumReviews']} reviews)")


# Display Data Table
df = pd.merge(st.session_state.industries,st.session_state.reviews, on = "Industry")

st.subheader("Data Table")
st.dataframe(df)


