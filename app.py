from flask import Flask, request, render_template
from bmi_debugger import categorize_BMI

app= Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods= ["POST"])
def predict():
    
        # weight = float(request.form["weight"])
        # height= float(request.form["height"])
    weight = request.form.get('weight')
    height = request.form.get('height')
    if weight is None or height is None:
        # return the keys received so you can verify what came in
        received = dict(request.form)
        return (
            "Missing form fields. Expected 'weight' and 'height'. "
            f"Received keys: {list(received.keys())}"
        ), 400    
    # convert to float safely
    try:
        weight = float(weight)
        height = float(height)
    except ValueError:
        return "Invalid numeric values for weight or height.", 400
    try:
        category= categorize_BMI(weight,height)
        return f"BMI Category: {category}"
    except ValueError as e:
        return f"Error: {e}"
    except Exception as e:
        return f"Unexpected error: {e}", 500
if __name__=="__main__":
    app.run(debug=True)