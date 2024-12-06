import streamlit as st

def content_moderation_panel():
    st.title("Content Moderation Panel")
    st.subheader("Flagged Posts")
    st.write("Review flagged posts and take appropriate action.")
    st.table([["Post ID", "User", "Reason", "Date Flagged"],
              [201, "User X", "Spam", "2024-12-06"],
              [202, "User Y", "Hate Speech", "2024-12-05"]])

    st.subheader("Moderation Actions")
    st.write("Select a post to approve, edit, or remove.")

    selected_post = st.selectbox("Choose a post to moderate:", ["Post 201", "Post 202"])
    if st.button("Approve"):
        st.success(f"Post {selected_post} approved.")
    if st.button("Edit"):
        st.info(f"Post {selected_post} marked for editing.")
    if st.button("Remove"):
        st.error(f"Post {selected_post} removed.")

    st.subheader("Moderation History")
    st.write("View the history of actions taken on flagged posts.")
    st.table([["Post ID", "Action Taken", "Moderator", "Date"],
              [201, "Approved", "Admin A", "2024-12-06"]])

# Display the screen
content_moderation_panel()