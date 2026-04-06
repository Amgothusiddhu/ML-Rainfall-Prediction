from flask import Flask, render_template, request
import numpy as np

# CREATE APP (this was missing ❗)
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = [float(x) for x in request.form.values()]
        prediction = sum(data)

        # Convert to cm
        rainfall_cm = round(prediction / 10, 2)

        # Classification
        if rainfall_cm < 1:
            result = "☀️ No Rain"
        elif rainfall_cm < 3:
            result = "🌦️ Light Rain"
        elif rainfall_cm < 6:
            result = "🌧️ Moderate Rain"
        elif rainfall_cm < 10:
            result = "⛈️ Heavy Rain"
        else:
            result = "🌪️ Very Heavy Rain"

        return render_template(
            'index.html',
            prediction_text=f"🌧️ Rainfall: {rainfall_cm} cm → {result}"
        )

    except:
        return render_template('index.html', prediction_text="Invalid input")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
