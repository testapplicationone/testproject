import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from datetime import datetime



# Page title and description
st.title("Project Management Dashboard")
st.write("Track project tasks, deadlines, and progress.")

# Create a DataFrame to store tasks
tasks_df = pd.DataFrame(columns=["Task", "Deadline", "Status"])
task_name = st.text_input("Enter task name:")

# Add a task
if st.button("Add Task"):
    deadline = st.date_input("Task Deadline", min_value=datetime.today())
    tasks_df = tasks_df.append({"Task": task_name, "Deadline": deadline, "Status": "Pending"}, ignore_index=True)

# Display tasks
st.subheader("Tasks")
st.write(tasks_df)

# Update task status
task_index = st.number_input("Enter task index to update status:", min_value=0, max_value=len(tasks_df)-1, value=0, step=1)
status_options = ["Pending", "In Progress", "Completed"]
new_status = st.selectbox("Update Status", options=status_options)
if st.button("Update Status"):
    tasks_df.at[task_index, "Status"] = new_status
    st.write("Task status updated successfully.")

# Filter tasks by status
status_filter = st.selectbox("Filter tasks by status:", options=["All"] + status_options)
if status_filter != "All":
    filtered_tasks_df = tasks_df[tasks_df["Status"] == status_filter]
    st.write(filtered_tasks_df)
else:
    st.write(tasks_df)
