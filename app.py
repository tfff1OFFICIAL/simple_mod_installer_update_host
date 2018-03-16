from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/currentversion.json")
def send_version_data():
    return jsonify({
        "1.0": "https://s3-ap-southeast-2.amazonaws.com/tfff1-data/simple+mod+installer/simple.mod.installer.v3.0.4.msi"
    })
