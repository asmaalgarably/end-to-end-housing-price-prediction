# 🏠 End-to-End Housing Price Prediction System

An intelligent web application that predicts house prices in California using Machine Learning.  
This project demonstrates a complete **MLOps** workflow, featuring a decoupled architecture with a **FastAPI** backend and a **Streamlit** frontend.

---

## 🏗️ Project Architecture

The system is designed with a modular approach to separate the AI logic from the user interface, ensuring scalability and ease of deployment.

- **Data Mining & ML:** Data cleaning and model training using Scikit-Learn.
- **Backend (API):** High-performance API built with FastAPI to serve model predictions.
- **Frontend (UI):** Interactive web dashboard built with Streamlit for real-time user input.

---

## 🛠️ Tech Stack

- **Language:** Python 3.13  
- **Machine Learning:** Scikit-Learn, Pandas, NumPy  
- **API Framework:** FastAPI, Uvicorn  
- **Web Interface:** Streamlit  
- **Deployment Readiness:** Docker-ready, modular code structure  

---

## 🚀 How to Run the Project

### 1️⃣ Installation
Clone the repository and install the dependencies:

```bash
pip install fastapi uvicorn streamlit scikit-learn pandas numpy requests
```

---

### 2️⃣ Train the Model
Generate the model files (`train_model.pkl` and `scaler.pkl`):

```bash
python train_model.py
```

---

### 3️⃣ Start the Backend (API)
In a new terminal, launch the FastAPI server:

```bash
uvicorn main:app --reload
```

API documentation will be available at:  
http://127.0.0.1:8000/docs

---

### 4️⃣ Start the Frontend (UI)
In another terminal, launch the Streamlit dashboard:

```bash
streamlit run app.py
```

---

✅ The system is now ready to predict housing prices through an interactive web interface.
"# end-to-end-housing-price-prediction" 
