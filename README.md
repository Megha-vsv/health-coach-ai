# 🩺 Personal Health Coach AI

A simple AI-powered health analysis web application built using **Python** and **Streamlit**.

This project analyzes daily health metrics such as steps, sleep hours, calorie intake, and resting heart rate to provide personalized health status and recommendations.

---

## 🚀 Features

- 📊 Health risk analysis based on user input
- 🧠 Rule-based recommendation system
- 🖥️ Interactive Streamlit dashboard
- 🗂️ Modular Python architecture
- 📁 Sample dataset included

---

## 🛠️ Tech Stack

- Python 3.x
- Streamlit

---

## 📂 Project Structure

```
health-coach-ai/
│
├── app.py              # Streamlit UI
├── health_engine.py    # Core health analysis logic
├── sample_data.csv     # Sample dataset for testing
├── requirements.txt    # Project dependencies
├── LICENSE
├── .gitignore
└── README.md
```

---

## ⚙️ How It Works

1. User inputs daily health metrics.
2. The data is passed to `health_engine.py`.
3. Health parameters are evaluated using rule-based logic.
4. A health status is calculated.
5. Personalized recommendations are displayed on the dashboard.

---

## 💻 How to Run the Project Locally

### 1️⃣ Clone the repository

```
git clone https://github.com/Megha-vsv/health-coach-ai.git
```

### 2️⃣ Navigate into the project folder

```
cd health-coach-ai
```

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Run the Streamlit app

```
streamlit run app.py
```

The application will start at:

```
http://localhost:8501
```

---

## 📊 Sample Data

The project includes a `sample_data.csv` file that can be used for testing or future feature expansion.

---

## 📌 Project Objective

The objective of this project is to demonstrate a structured and functional Python implementation that analyzes health metrics and provides meaningful feedback through an interactive web interface.

This project was developed as part of Challenge 2 submission.

---

## 👩‍💻 Author

Vasava Meghaben Rajeshbhai
