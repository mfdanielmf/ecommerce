from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({'msg': 'OK'}), 200


if __name__ == "__main__":
    app.run('0.0.0.0', 8080, debug=True)
