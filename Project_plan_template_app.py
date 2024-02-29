import openai
import streamlit as st

openai.api_key = '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'

template = ["Project implementation plan", "Upgrade Plan", "Deployment plan", "Cutover plan", "Test Plan"]

st.title("Template Creation")

Selected_option = st.selectbox("Select a plan", template)

if st.button("Submit"):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "create a template for " + Selected_option}]
    )

    st.write("Generated Response:\n\n", response.choices[0].message.content)

