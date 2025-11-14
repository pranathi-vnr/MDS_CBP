from flask import Flask, request, render_template
import numpy as np, pickle
from feature import FeatureExtraction

app = Flask(__name__)

# Load ML model
model = pickle.load(open("pickle/model.pkl","rb"))

@app.route("/", methods=["GET","POST"])
def index():
    prediction = ""
    url_text = ""

    if request.method == "POST":
        url_text = request.form["url"]
        obj = FeatureExtraction(url_text)

        # Extract 30 features for prediction
        x = np.array(obj.getFeaturesList()).reshape(1, 30)

        # Model prediction
        pred = model.predict(x)[0]

        # Better, UI-friendly prediction messages:
        if pred == 1:
            prediction = "Legitimate Website ✔"
        else:
            prediction = "⚠ Phishing Website Detected!"

    return render_template("index.html", prediction=prediction, url=url_text)

if __name__ == "__main__":
    app.run(debug=True)

