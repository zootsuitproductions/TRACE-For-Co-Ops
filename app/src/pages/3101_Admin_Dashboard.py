import streamlit as st

def admin_dashboard():
    st.title("Admin Dashboard")
    st.subheader("User Activity Metrics")
    st.write("Metrics for platform engagement and activity (e.g., number of active users, reviews submitted).")

    st.subheader("Flagged Reviews")
    st.write("List of reviews flagged by users or detected by the system for inappropriate content.")
    st.table([["Review ID", "User", "Reason for Flagging", "Timestamp"],
              [1, "User A", "Spam", "2024-12-06 10:00"],
              [2, "User B", "Inappropriate Language", "2024-12-05 15:30"]])

    st.subheader("New Submissions")
    st.write("Monitor new content added by users, awaiting admin approval.")
    st.table([["Submission ID", "Type", "Submitted By", "Date"],
              [101, "Review", "User C", "2024-12-06"],
              [102, "Interview", "User D", "2024-12-05"]])

# Display the screen
admin_dashboard()