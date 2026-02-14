# Personal Health Coach AI

Personal Health Coach AI is a working health monitoring and recommendation system built using Python and Streamlit.

The application analyzes user health inputs (steps, sleep hours, calories intake, heart rate) and provides risk scoring and personalized recommendations.

---

## 🚀 How to Run

1. Install dependencies:
   pip install -r requirements.txt

2. Run the application:
   streamlit run app.py

The app will open in your browser at:
http://localhost:8501

---

## 🧠 Project Architecture

- app.py → Streamlit user interface
- health_engine.py → Core health risk analysis engine
- sample_data.csv → Sample wearable health dataset
- requirements.txt → Project dependencies

---

## ⚙️ Core Features

- Health risk scoring system
- Rule-based anomaly detection
- Personalized health recommendations
- Interactive Streamlit dashboard
- Modular architecture (UI + engine separation)

---

## 🛠 Tech Stack

- Python
- Streamlit
- Pandas

---

## 🧩 Health Analysis Logic

The system evaluates:

- Low daily steps (< 5000)
- Insufficient sleep (< 6 hours)
- High calorie intake (> 2500)
- High resting heart rate (> 100 bpm)

Based on detected risk factors, a health status is generated:
- Excellent Health
- Moderate Risk
- High Risk

---

## 📌 Future Improvements

- Integration with real wearable APIs
- Machine learning-based risk prediction
- Long-term trend visualization
- Database integration

---

## License

MIT License