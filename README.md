# EndoPredict AI

AI-powered Endometriosis Prediction and Clinical Decision Support System built using Flask, PyTorch, HTML, CSS, and JavaScript.

---

# Project Overview

EndoPredict AI is a machine learning-based healthcare application designed to assist in predicting the likelihood of Endometriosis using patient clinical data and medical scan images.

The system combines:

* Deep Learning Image Analysis
* Numerical Clinical Features
* AI-based Risk Prediction
* Interactive Dashboard UI

---

# Features

* Endometriosis prediction using AI
* Multimodal deep learning model
* Upload scan image support
* Patient clinical data analysis
* Risk level prediction
* Confidence score generation
* Dashboard and analytics pages
* Reports management
* Dark mode support
* Multi-language support
* Responsive frontend UI

---

# Technologies Used

## Frontend

* HTML5
* CSS3
* JavaScript

## Backend

* Python
* Flask
* Flask-CORS

## Machine Learning

* PyTorch
* ResNet18
* NumPy
* Torchvision

---

# Project Structure

```bash
Endometriosis/
│
├── static/
│   ├── global.css
│   ├── global.js
│
├── templates/
│   ├── index.html
│   ├── dashboard.html
│   ├── analytics.html
│   ├── reports.html
│   ├── settings.html
│   ├── result.html
│
├── app.py
├── endometriosis_model.pth
├── requirements.txt
├── README.md
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/endopredict-ai.git
```

## Navigate to Project Folder

```bash
cd endopredict-ai
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Application

```bash
python app.py
```

Server will start at:

```bash
http://127.0.0.1:5000
```

---

# API Endpoint

## Predict Endpoint

```http
POST /api/predict
```

### Input

* Patient numerical data
* Optional medical scan image

### Output

* Prediction Result
* Confidence Score
* Risk Level

---

# Machine Learning Model

The system uses:

* ResNet18 CNN architecture for image processing
* Numerical feature processing network
* Combined multimodal classifier

---

# Prediction Features

* Age
* Menstrual Irregularity
* Chronic Pain Level
* Hormone Level Abnormality
* Infertility
* BMI
* Height
* Weight
* Blood Pressure
* Estrogen Level
* Progesterone Level

---

# Future Improvements

* Real medical dataset integration
* Model retraining pipeline
* Database integration
* User authentication
* PDF report generation
* Cloud deployment

---

# Author

G Jeswanth Kumar Reddy
B.Tech Computer Science (AI & ML)
GITAM University

---

# License

This project is developed for educational and research purposes.
