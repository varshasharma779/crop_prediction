import joblib
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Load the model
model = joblib.load('crop_app.pkl')

@app.route('/')
def prediction():
    return render_template("Index.html")

@app.route('/predict', methods=["POST"])
def brain():
    try:
        Nitrogen = float(request.form['Nitrogen'])
        Phosphorus = float(request.form['Phosphorus'])
        Potassium = float(request.form['Potassium'])
        Temperature = float(request.form['Temperature'])
        Humidity = float(request.form['Humidity'])
        Ph = float(request.form['Ph'])
        Rainfall = float(request.form['Rainfall'])

        values = [Nitrogen, Phosphorus, Potassium, Temperature, Humidity, Ph, Rainfall]

        if 0 < Ph < 14 and Temperature < 100 and Humidity > 0:
            
            prediction = model.predict([values])
            return render_template("index.html", prediction=prediction)
        else:
            return "Invalid input values", 400
    except ValueError as e:
        return f"Invalid input: {str(e)}", 400

if __name__ == '__main__':
    app.run(debug=True)
