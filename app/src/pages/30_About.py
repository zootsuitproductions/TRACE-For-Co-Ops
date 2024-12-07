import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks


SideBarLinks()

st.sidebar.page_link("Home.py", label="Home", icon="🏠")

st.write("# About this App")


st.markdown (
    """
    COUPE is a data-driven platform designed to revolutionize the Co-Op search process for Northeastern students by providing peer-to-peer insights into specific company experiences. While platforms like NUWorks provide job listings, they often fall short in detailing the real day-to-day life, culture, and interview dynamics students will encounter. COUPE fills this gap by giving students a space to share and access honest feedback about what it’s truly like working for various employers—covering everything from workplace culture to interview formats and application tips.

    """
        )
