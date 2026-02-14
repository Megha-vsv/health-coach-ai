import pandas as pd
import streamlit as st
from health_engine import analyze_health_metrics

st.title("Personal Health Coach AI")

st.markdown("Enter your health data to receive recommendations")

steps = st.number_input("Daily Steps", min_value=0)
sleep = st.number_input("Hours of Sleep", min_value=0.0, max_value=24.0, step=0.5)
calories = st.number_input("Daily Calories", min_value=0)
heartrate = st.number_input("Resting Heart Rate", min_value=0)

if st.button("Analyze"):
    result = analyze_health_metrics(steps, sleep, calories, heartrate)
    st.write(result)
