import openai
import streamlit as st
from config import Api_key

openai.api_key = st.screts["api_key"]

template = {
    "Project implementation plan": "create a template for Project implementation plan",
    "Upgrade Plan": "create a template for Upgrade Plan",
    "Deployment plan": "You are playing a role of Project manager for Oracle Revenue Management and Billing for an insurance organization. You have been given the task to prepare deployment plan . The plan should be very much detailed and cover all minor steps with task id, Area, task name, Team, Sub Team, owner, Date, Predecessor, Status, IACR, duration etc. Also make sure below points are included in the plan- 1. Project Governance 2. Service stop 3. Code deployment 4.Data conversion 5. Other technical steps 6. Ingration build/test 7. Service start 8. Technical checkout 9. Function Checkout 10. Go-NoGo Decision etc.Now please help with a detailed deployment plan for this ORMB implementation. show me the same deployment plan in tabular way also include start date and end date",
    "Cutover plan": "create a template for Cutover plan",
    "Test Plan": "create a template for Test Plan"
}

st.title("Template Creation")

Selected_option = st.selectbox("Select a plan", list(template.keys()))

if st.button("Submit"):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": template[Selected_option]}]
    )

    st.write("Generated Response:\n\n", response.choices[0].message.content)
