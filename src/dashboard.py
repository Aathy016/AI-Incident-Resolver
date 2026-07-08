import requests
import streamlit as st

st.set_page_config(
    page_title="AI Incident Resolver"
)

st.title(
    "AI Incident Resolver"
)

issue = st.text_input(
    "Enter Incident"
)

if st.button("Analyze"):

    with st.spinner(
        "Analyzing incident..."
    ):

        response = requests.get(
            "http://localhost:8000/incident",
            params={
                "issue": issue
            }
        )

        result = response.json()

        st.subheader(
            "AI Analysis"
        )

        st.write(
            result["result"]
        )