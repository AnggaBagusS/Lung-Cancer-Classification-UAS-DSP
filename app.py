from flask import Flask, render_template, request, jsonify
from model_util import get_model, load_model, set_features, predict
import pandas as pd
import os

app = Flask(__name__)


# ===============================
# HOME
# ===============================
@app.route('/')
def home():
    return render_template('home.html')


# ===============================
# DASHBOARD
# ===============================
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard_view.html')


# ===============================
# DOWNLOAD MODEL FROM MLFLOW
# ===============================
@app.route('/model')
def download_model():
    model = get_model()
    if model:
        print("Model berhasil diunduh dan disimpan.")
    else:
        print("Gagal mengunduh model.")
    return render_template('home.html')


# ===============================
# PREDICTION (WEB FORM)
# ===============================
@app.route('/predict', methods=['GET', 'POST'])
def predict_view():
    feature_names = set_features()
    model = load_model()

    prediction_label = None
    input_data = {f: 0 for f in feature_names}

    if request.method == "POST":
        input_data = {
            f: int(request.form.get(f, 0))
            for f in feature_names
        }

        pred = predict(model, input_data)

        # mapping level
        prediction_label = (
            "Low" if pred == 1 else
            "Medium" if pred == 2 else
            "High"
        )

    return render_template(
        "predict_view.html",
        features=input_data,
        prediction=prediction_label
    )


# ===============================
# PREDICTION (API)
# ===============================
@app.route('/api/predict', methods=['POST'])
def api_predict():
    data = request.get_json()

    feature_names = set_features()
    input_data = {f: int(data.get(f, 0)) for f in feature_names}

    model = load_model()
    pred = predict(model, input_data)

    prediction_label = (
        "Low" if pred == 1 else
        "Medium" if pred == 2 else
        "High"
    )

    return jsonify({
        "prediction": prediction_label,
        "raw_prediction": int(pred),
        "input": input_data
    })


# ===============================
# RUN APP
# ===============================
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
