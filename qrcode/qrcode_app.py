from flask import Flask, request, send_file

from flask_qrcode import QRcode


app = Flask(__name__)
qrcode = QRcode(app)


@app.route("/qrcode", methods=["GET"])
def get_qrcode():
    # please get /qrcode?data=<qrcode_data>
    data = request.args.get("data", "")
    return send_file(qrcode(data, mode="raw"), mimetype="image/png")
