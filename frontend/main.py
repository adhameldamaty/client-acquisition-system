import streamlit as st
import requests
import pandas as pd
import time


st.set_page_config(page_title="Client Acquisition System", layout="wide")
st.title("🚀 DevOps Client Acquisition System")


API_URL = "http://nginx_gateway:80" 


menu = st.sidebar.selectbox("Menu", ["Home", "Trigger Automation", "View Reports"])

if menu == "Home":
    st.write("### Welcome to the Microservices Control Panel")
    st.info("This interface interacts with a Dockerized Microservices Architecture.")
    st.image("https://miro.medium.com/v2/resize:fit:1400/1*5t6I0s6_mF1C9rL6o-3fNg.png", caption="Microservices Architecture")

elif menu == "Trigger Automation":
    st.header("⚡ Start Client Workflow")
    if st.button("Trigger New Client Acquisition"):
        with st.spinner("Contacting Automation Service..."):
            try:
                
                response = requests.get(f"{API_URL}/automation/trigger")
                if response.status_code == 200:
                    data = response.json()
                    st.success("Workflow Started Successfully! ✅")
                    st.json(data)
                else:
                    st.error("Failed to trigger automation.")
            except Exception as e:
                st.error(f"Connection Error: {e}")

elif menu == "View Reports":
    st.header("📊 Live System Reports")
    
    
    if st.button("Refresh Data"):
        st.rerun()

    try:
        response = requests.get(f"{API_URL}/reporting/stats")
        if response.status_code == 200:
            data = response.json()
            
            
            col1, col2 = st.columns(2)
            col1.metric(label="Total Reports in DB", value=data.get("Total_Reports_In_DB", 0))
            col2.metric(label="Last Recorded Value", value=data.get("New_Value", 0))
            
            st.write("---")
            st.write("#### Raw Response from Microservice:")
            st.json(data)
        else:
            st.error("Could not fetch reports.")
    except Exception as e:
        st.error(f"Connection Error: Is the backend running? \n {e}")