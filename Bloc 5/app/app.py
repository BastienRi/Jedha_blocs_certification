from flask import Flask, url_for, request, jsonify, render_template
import joblib

app = Flask(__name__)

welcome_message = "Welcome on the API for wine prediction."

@app.route("/")
def index():
    return render_template("api_doc.html")

@app.route("/predict/", methods=["POST"])
def predict():
    if request.method == "POST" and request.is_json:
        model = joblib.load("model.joblib")
        json_data = request.get_json()
        json_data_input = json_data["input"]
        prediction = model.predict(json_data_input).tolist()
        return jsonify("predict : ", prediction)
    else:
        return jsonify({"msg": "Wrong input format please try again."})


if __name__ == "__main__":
    app.run(threaded=True, port=5000)