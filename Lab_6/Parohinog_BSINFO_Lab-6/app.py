from flask import Flask, request,jsonify

app = Flask(__name__)

@app.route('/api/greetings', methods=['GET'])
def greetings():
    return jsonify({"message": "Hello, World!"})

@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify({"echo": data})

if __name__ == '__main__':
    app.run(debug=True)