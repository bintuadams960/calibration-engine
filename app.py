from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the Calibration Engine!'

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=8080, debug=False)
