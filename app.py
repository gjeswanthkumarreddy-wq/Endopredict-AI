"""
Endometriosis ML Model Backend API
FINAL HYBRID VERSION
"""

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

import torch
import torch.nn as nn

from torchvision import models, transforms
from PIL import Image

import numpy as np

from datetime import datetime

import logging
import os

# ==================================================
# CONFIG
# ==================================================

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

app = Flask(__name__)

CORS(app)

MODEL_PATH = "endometriosis_model.pth"

DEVICE = torch.device(
    "cuda"
    if torch.cuda.is_available()
    else "cpu"
)

# ==================================================
# FEATURES
# ==================================================

NUMERICAL_COLS = [

    "Age",

    "Menstrual_Irregularity",

    "Chronic_Pain_Level",

    "Hormone_Level_Abnormality",

    "Infertility",

    "BMI",

    "Height",

    "Weight",

    "Blood_Pressure_Systolic",

    "Blood_Pressure_Diastolic",

    "Estrogen_Level",

    "Progesterone_Level"
]

# ==================================================
# IMAGE TRANSFORM
# ==================================================

IMAGE_TRANSFORM = transforms.Compose([

    transforms.Resize((224, 224)),

    transforms.ToTensor()

])

# ==================================================
# MODEL
# ==================================================

class MultiModalModel(nn.Module):

    def __init__(self):

        super().__init__()

        self.cnn = models.resnet18(weights=None)

        self.cnn.fc = nn.Linear(512, 128)

        self.num_fc = nn.Sequential(

            nn.Linear(len(NUMERICAL_COLS), 64),

            nn.ReLU()

        )

        self.classifier = nn.Sequential(

            nn.Linear(128 + 64, 64),

            nn.ReLU(),

            nn.Linear(64, 2)

        )

    def forward(self, image, numerical):

        img_feat = self.cnn(image)

        num_feat = self.num_fc(numerical)

        combined = torch.cat(
            [img_feat, num_feat],
            dim=1
        )

        return self.classifier(combined)

# ==================================================
# LOAD MODEL
# ==================================================

model = None

def load_model():

    global model

    if not os.path.exists(MODEL_PATH):

        logger.error("Model file not found")

        return False

    try:

        model = MultiModalModel().to(DEVICE)

        checkpoint = torch.load(
            MODEL_PATH,
            map_location=DEVICE
        )

        if (
            isinstance(checkpoint, dict)
            and "model_state_dict" in checkpoint
        ):

            model.load_state_dict(
                checkpoint["model_state_dict"]
            )

        else:

            model.load_state_dict(checkpoint)

        model.eval()

        logger.info(
            "Model loaded successfully"
        )

        return True

    except Exception as e:

        logger.error(
            f"Model loading failed: {e}"
        )

        return False

load_model()

# ==================================================
# IMAGE PROCESSOR
# ==================================================

class ImageProcessor:

    @staticmethod
    def process(file):

        try:

            img = Image.open(file).convert("RGB")

            tensor = IMAGE_TRANSFORM(img)

            tensor = tensor.unsqueeze(0)

            return tensor

        except Exception as e:

            logger.error(str(e))

            return torch.zeros(
                (1, 3, 224, 224)
            )

# ==================================================
# FEATURE PROCESSOR
# ==================================================

class FeatureProcessor:

    FEATURE_RANGES = {

        'Age': (18, 70),

        'Menstrual_Irregularity': (0, 1),

        'Chronic_Pain_Level': (0, 10),

        'Hormone_Level_Abnormality': (0, 1),

        'Infertility': (0, 1),

        'BMI': (15, 40),

        'Height': (140, 200),

        'Weight': (40, 150),

        'Blood_Pressure_Systolic': (80, 180),

        'Blood_Pressure_Diastolic': (40, 120),

        'Estrogen_Level': (20, 400),

        'Progesterone_Level': (0.5, 25),
    }

    @staticmethod
    def normalize(val, name):

        min_v, max_v = (
            FeatureProcessor
            .FEATURE_RANGES[name]
        )

        try:

            val = float(val)

        except:

            val = min_v

        val = np.clip(
            val,
            min_v,
            max_v
        )

        normalized = (
            val - min_v
        ) / (
            max_v - min_v
        )

        return normalized

    @staticmethod
    def process(data):

        features = []

        for col in NUMERICAL_COLS:

            value = data.get(col, 0)

            normalized = (
                FeatureProcessor.normalize(
                    value,
                    col
                )
            )

            features.append(normalized)

        tensor = torch.FloatTensor(
            features
        )

        tensor = tensor.unsqueeze(0)

        return tensor

# ==================================================
# PAGE ROUTES
# ==================================================

@app.route("/")
def home():

    return render_template("index.html")

@app.route("/dashboard")
def dashboard():

    return render_template("dashboard.html")

@app.route("/settings")
def settings():

    return render_template("settings.html")

@app.route("/analytics")
def analytics():

    return render_template("analytics.html")

@app.route("/reports")
def reports():

    return render_template("reports.html")

@app.route("/result")
def result():

    return render_template("result.html")

# ==================================================
# HEALTH
# ==================================================

@app.route("/health")
def health():

    return jsonify({

        "status": "healthy",

        "model_loaded":
        model is not None,

        "device":
        str(DEVICE)

    })

# ==================================================
# PREDICTION API
# ==================================================

@app.route("/api/predict", methods=["POST"])
def predict():

    try:

        if model is None:

            return jsonify({

                "success": False,

                "error":
                "Model not loaded"

            }), 500

        # IMAGE

        image_tensor = torch.zeros(
            (1, 3, 224, 224)
        )

        if "image" in request.files:

            file = request.files["image"]

            if (
                file
                and file.filename != ""
            ):

                image_tensor = (
                    ImageProcessor.process(file)
                )

        image_tensor = image_tensor.to(DEVICE)

        # NUMERICAL DATA

        numerical_data = {}

        for col in NUMERICAL_COLS:

            value = request.form.get(col)

            if value is None or value == "":

                return jsonify({

                    "success": False,

                    "error":
                    f"Missing field: {col}"

                }), 400

            try:

                numerical_data[col] = float(value)

            except:

                numerical_data[col] = 0.0

        numerical_tensor = (
            FeatureProcessor.process(
                numerical_data
            )
        )

        numerical_tensor = numerical_tensor.to(
            DEVICE
        )

        # ==============================================
        # MODEL PREDICTION
        # ==============================================

        with torch.no_grad():

            outputs = model(
                image_tensor,
                numerical_tensor
            )

            probs = torch.softmax(
                outputs,
                dim=1
            )

            class_probs = (
                probs[0]
                .cpu()
                .numpy()
            )

            model_probability = float(
                class_probs[1]
            )

        # ==============================================
        # EXTRACT VALUES
        # ==============================================

        pain = numerical_data[
            "Chronic_Pain_Level"
        ]

        infertility = numerical_data[
            "Infertility"
        ]

        hormone = numerical_data[
            "Hormone_Level_Abnormality"
        ]

        estrogen = numerical_data[
            "Estrogen_Level"
        ]

        progesterone = numerical_data[
            "Progesterone_Level"
        ]

        bmi = numerical_data[
            "BMI"
        ]

        irregular = numerical_data[
            "Menstrual_Irregularity"
        ]

        # ==============================================
        # MEDICAL RULE SCORE
        # ==============================================

        score = 0

        if pain >= 8:

            score += 30

        elif pain >= 5:

            score += 15

        if infertility == 1:

            score += 20

        if hormone == 1:

            score += 20

        if estrogen >= 300:

            score += 15

        if progesterone <= 5:

            score += 15

        if bmi >= 30:

            score += 10

        if irregular == 1:

            score += 10

        # ==============================================
        # FINAL HYBRID PROBABILITY
        # ==============================================

        rule_probability = score / 100

        disease_prob = (

            (rule_probability * 0.85)

            +

            (model_probability * 0.15)

        )

        disease_prob = min(
            disease_prob,
            0.99
        )

        # ==============================================
        # CLASSIFICATION
        # ==============================================

        if disease_prob >= 0.70:

            risk = "High"

        elif disease_prob >= 0.40:

            risk = "Moderate"

        else:

            risk = "Low"

        predicted_class = (

            1

            if disease_prob >= 0.40

            else 0
        )

        prediction_label = (

            "Endometriosis Detected"

            if predicted_class == 1

            else

            "No Endometriosis"
        )

        # ==============================================
        # RESPONSE
        # ==============================================

        return jsonify({

            "success": True,

            "prediction":
            predicted_class,

            "prediction_label":
            prediction_label,

            "probability":

            round(
                disease_prob * 100,
                2
            ),

            "risk_level":
            risk,

            "patient_data":
            numerical_data,

            "timestamp":

            datetime.now()
            .strftime("%d-%m-%Y %H:%M")

        })

    except Exception as e:

        logger.error(str(e))

        return jsonify({

            "success": False,

            "error": str(e)

        }), 500

# ==================================================
# MODEL INFO
# ==================================================

@app.route("/api/model/info")
def model_info():

    return jsonify({

        "model_name":
        "Endometriosis Predictor",

        "architecture":
        "ResNet18 + Numerical Features",

        "features":
        len(NUMERICAL_COLS),

        "device":
        str(DEVICE),

        "model_loaded":
        model is not None

    })

# ==================================================
# RUN SERVER
# ==================================================

if __name__ == "__main__":

    app.run(

        host="0.0.0.0",

        port=5000,

        debug=True

    )

