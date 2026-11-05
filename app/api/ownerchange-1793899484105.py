from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route("/calculate/1793899484105", methods=["POST"])
def calculate():
    expression = request.get_json()["expression"]
    result = eval(expression)
    return jsonify({"result": str(result)})
