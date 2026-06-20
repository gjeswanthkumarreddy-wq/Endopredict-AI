# EndoPredict AI - Setup Guide

This guide explains how to install and run the EndoPredict AI project on your local system.

---

# System Requirements

Before starting, make sure your system has:

* Python 3.10 or higher
* VS Code or any code editor
* Git installed
* Internet connection for package installation

---

# Step 1 - Clone Repository

Open terminal and run:

```bash
git clone https://github.com/yourusername/endopredict-ai.git
```

---

# Step 2 - Open Project Folder

```bash
cd endopredict-ai
```

---

# Step 3 - Create Virtual Environment (Optional)

## Windows

```bash
python -m venv venv
```

Activate environment:

```bash
venv\Scripts\activate
```

## Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# Step 4 - Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

---

# Step 5 - Verify Project Structure

Your project should look like this:

```bash
Endometriosis/
│
├── static/
├── templates/
├── app.py
├── endometriosis_model.pth
├── requirements.txt
├── README.md
```

---

# Step 6 - Run Flask Application

Start the Flask server:

```bash
python app.py
```

---

# Step 7 - Open Browser

After running successfully, open:

```bash
http://127.0.0.1:5000
```

---

# Available Pages

| Page       | Route        |
| ---------- | ------------ |
| Prediction | `/`          |
| Dashboard  | `/dashboard` |
| Analytics  | `/analytics` |
| Reports    | `/reports`   |
| Settings   | `/settings`  |

---

# API Endpoint

## Prediction API

```http
POST /api/predict
```

Used for:

* Patient disease prediction
* Risk level analysis
* Confidence score generation

---

# Common Errors & Fixes

## Model File Not Found

Error:

```bash
Model file not found
```

Fix:

* Ensure `endometriosis_model.pth` exists in root folder.

---

## Flask Module Not Found

Fix:

```bash
pip install flask
```

---

## Torch Installation Issue

Install manually:

```bash
pip install torch torchvision
```

---

# Technologies Used

* Python
* Flask
* PyTorch
* HTML
* CSS
* JavaScript
* NumPy

---

# Author

G Jeswanth Kumar Reddy
B.Tech Computer Science (AI & ML)
GITAM University
