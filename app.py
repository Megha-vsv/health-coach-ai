import streamlit as st
from health_engine import analyze_health

st.set_page_config(page_title="Personal Health Coach AI", layout="wide")

st.title("Personal Health Coach AI")
st.write("Analyze your health metrics and get personalized recommendations")

# User inputs
steps = st.number_input("Daily Steps", min_value=0)
sleep_hours = st.number_input("Sleep Hours", min_value=0.0, max_value=24.0, step=0.5)
calories = st.number_input("Daily Calories", min_value=0)
heart_rate = st.number_input("Resting Heart Rate (bpm)", min_value=0)

if st.button("Analyze Health"):
    status, recs = analyze_health(steps, sleep_hours, calories, heart_rate)

    st.subheader("Health Status:")
    st.success(status)

    if recs:
        st.subheader("Recommendations:")
        for r in recs:
            st.write(f"- {r}")
    else:
        st.write("No recommendations needed — keep up the good work!")
