import streamlit as st
st.set_page_config(page_title="NERVS", layout="wide")

st.title("NERVS")
st.subheader("National Elastic Resilience & Vulnerability System")

st.write("""NERVS is an AI-driven stress-test engine that models how contries absorb,
amplify, and recover from global shocks.""")

st.header("Input Country Stress Indicators")

countries=["India", "China","USA", "Japan", "Russia"]

indicators = ["Economic Stability,
              "Defence & Security", "Healthcare Readiness", "Cyber Infrastructure", "Energy Security"]
data ={}

for country in countries:
  st.subheader(country)
  data[country] = {}
  for indicator in indicators:
    value = st.slider(f"{indicator} ({country})",
                      min-value=1,
                      max_value=10,
                      value= 5,
                      key=f"{country}_{indicator}")
    data[country][indicator] = value
