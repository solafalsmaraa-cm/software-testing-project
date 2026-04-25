from flask import Flask, request, jsonify, render_template  

app = Flask(__name__)

def add_numbers(a, b):
    return a + b

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/add", methods=["POST"])
def add():
    data = request.json
    a = data.get("a")
    b = data.get("b")

    if a is None or b is None:
        return jsonify({"error": "Missing values"}), 400

    return jsonify({"result": add_numbers(a, b)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)