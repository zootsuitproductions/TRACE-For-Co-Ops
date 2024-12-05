import logging
logger = logging.getLogger(__name__)
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
st.header('View and Categorize User Feedback')

# You can access the session state to make a more customized/personalized app experience
st.write(f"### Hi, {st.session_state['first_name']}.")


# get the feedbacks
try:
    feedback = requests.get("http://api:4000/f/feedback").json()
    st.dataframe(feedback)
except:
    st.write("Could not to conncet to database to get user feedback")
'''
# 初期データ（フィードバックのサンプルデータ）
feedback_data = [
    {"ID": 1, "Feedback": "Add dark mode feature", "Status": "Pending"},
    {"ID": 2, "Feedback": "Improve app performance", "Status": "Pending"},
    {"ID": 3, "Feedback": "Add more language support", "Status": "Pending"},
]

# データフレームとして管理
feedback_df = pd.DataFrame(feedback_data)

# Streamlitアプリ
st.title("ユーザーフィードバック管理インターフェース")

# フィードバックテーブルを表示
st.subheader("フィードバック一覧")
st.dataframe(feedback_df)

# フィードバックの更新フォーム
st.subheader("フィードバックのステータスを更新")
selected_id = st.selectbox("フィードバックIDを選択", feedback_df["ID"])
new_status = st.radio(
    "新しいステータスを選択",
    ["In Progress", "Implemented", "Rejected"],
    index=0,
)

if st.button("ステータスを更新"):
    # 該当するフィードバックのステータスを更新
    feedback_df.loc[feedback_df["ID"] == selected_id, "Status"] = new_status
    st.success(f"フィードバックID {selected_id} のステータスを '{new_status}' に更新しました！")

# 更新後のフィードバックテーブルを表示
st.subheader("更新後のフィードバック一覧")
st.dataframe(feedback_df)
'''
