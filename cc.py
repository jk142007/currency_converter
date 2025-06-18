from flask import Flask, render_template, request

app = Flask(__name__)

# Static conversion rates (for demo)
rates = {
    "INR": 1,
    "USD": 0.012,
    "EURO": 0.011,
    "DHM": 0.044,
    "POUND": 0.0095
}

@app.route("/", methods=["GET", "POST"])
def convert():
    result = ""
    if request.method == "POST":
        try:
            amount = float(request.form["amount"])
            from_curr = request.form["from_currency"]
            to_curr = request.form["to_currency"]
            converted = amount * rates[to_curr] / rates[from_curr]
            result = f"{amount:.2f} {from_curr} = {converted:.2f} {to_curr}"
        except:
            result = "Invalid input"
    return render_template("cc.html", result=result)

if __name__ == "__main__":
    app.run(port=5002,debug=True)
