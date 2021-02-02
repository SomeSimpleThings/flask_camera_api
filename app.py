import os
import picamera
from flask import Flask, render_template, redirect, url_for, request, send_file, make_response, jsonify, abort
from flask_bootstrap import Bootstrap

from vars import API_V1

app = Flask(__name__)
Bootstrap(app)

camera = picamera.PiCamera()


@app.route('/')
def index():
    return render_template('index.html')


@app.route(f'{API_V1}photos/', methods=['GET'])
def get_photos():
    filename = 'static/image.png'
    camera.start_preview()
    camera.capture(filename)
    camera.close()
    return send_file(filename, mimetype='image/png')


@app.route(f'{API_V1}photos/<int:photo_id>/', methods=['GET'])
def get_photo(photo_id):
    pass


# @app.route(f'{API_V1}photos', methods=['POST'])
# def create_photo():
#     filename = 'static/image.png'
#     camera.start_preview()
#     camera.capture(filename)
#     camera.close()
#     return send_file(filename, mimetype='image/png')


@app.route(f'{API_V1}photos/<int:photo_id>/', methods=['PUT'])
def update_photo(photo_id):
    pass


@app.route(f'{API_V1}photos/<int:photo_id>/', methods=['DELETE'])
def delete_photo(photo_id):
    return jsonify({'result': True})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run('0.0.0.0')
