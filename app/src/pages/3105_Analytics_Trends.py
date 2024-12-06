import streamlit as st

def analytics_trends_page():
    st.title("Analytics and Trends Page")
    st.subheader("Trends in Reviews")
    st.write("Visualize trends in student reviews, company searches, and engagement.")

    st.line_chart({
        "2024-12-01": [10, 15, 20],
        "2024-12-02": [20, 25, 30],
        "2024-12-03": [30, 35, 40]
    })

    st.subheader("Category Insights")
    st.write("View insights by category or industry.")
    st.bar_chart({
        "Industry A": [5, 10, 15],
        "Industry B": [10, 20, 30],
        "Industry C": [15, 25, 35]
    })

    st.subheader("Engagement Metrics")
    st.write("Track user engagement metrics.")
    st.metric(label="Active Users Today", value=100, delta=10)
    st.metric(label="Reviews Submitted", value=50, delta=5)

# Display the screen
analytics_trends_page()