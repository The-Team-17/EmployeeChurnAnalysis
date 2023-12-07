from flask import Flask, request, render_template
import pickle

# Create flask app
flask_app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/predict", methods = ["POST"])
def predict():
    import pandas as pd
    uploaded_file = request.files['csvFile']
    print(uploaded_file)
    df = pd.read_csv(uploaded_file)
    prediction = model.predict(df)
    return render_template("successful.html", len = len(prediction), prediction = prediction)


if __name__ == "__main__":
    flask_app.run(debug=True)