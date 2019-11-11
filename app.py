import os

from flask import abort, Flask, jsonify, request


app = Flask(__name__)


def is_request_valid(request):
    is_token_valid = request.form['token'] == os.environ['SLACK_VERIFICATION_TOKEN']
    is_team_id_valid = request.form['team_id'] == os.environ['SLACK_TEAM_ID']

    return is_token_valid and is_team_id_valid


@app.route('/hello', methods=['POST'])
def hello():
    if not is_request_valid(request):
        abort(400)

    return jsonify(
        response_type='in_channel',
        text='<https://icists.org|Welcome!>',
    )

@app.route('/help', methods=['POST'])
def help():
    if not is_request_valid(request):
        abort(400)

    return jsonify(
        response_type='in_channel',
        text='/hello, /drive, /vectormeeting',
    )

@app.route('/drive', methods=['POST'])
def drive():
    if not is_request_valid(request):
        abort(400)

    return jsonify(
        response_type='in_channel',
        text='<https://drive.google.com/drive/u/0/folders/0B20dYYj1TLYDeTJaZERERnl4SFE|Google Drive>',
    )

@app.route('/vectormeeting', methods=['POST'])
def vectormeeting():
    if not is_request_valid(request):
        abort(400)

    return jsonify(
        response_type='in_channel',
        text='<https://drive.google.com/drive/u/0/folders/1VgZNinrKj0-Wt8Pj5nYFu2T4NuTq2YXh|벡미록>',
    )

@app.route('/irs', methods=['POST'])
def irs():
    if not is_request_valid(request):
        abort(400)

    return jsonify(
        response_type='in_channel',
        text='<https://drive.google.com/drive/u/0/folders/1cF4mAV3wsch5wTIirQAcvobSBwOWRrkK|IRS>',
    )