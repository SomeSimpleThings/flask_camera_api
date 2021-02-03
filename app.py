import io
import os
import picamera
import time

from flask import Flask, render_template, send_file, make_response, jsonify
from flask_bootstrap import Bootstrap

from vars import API_V1

app = Flask(__name__)
Bootstrap(app)


def take_photo():
    stream = io.BytesIO()
    with picamera.PiCamera() as camera:
        camera.start_preview()
        # Camera warm-up time
        time.sleep(2)
        camera.capture(stream, 'png')
        camera.stop_preview()
    stream.seek(0)
    return stream


@app.route('/')
def index():
    return render_template('index.html')


@app.route(f'{API_V1}photos/', methods=['GET'])
def get_photos():
    return send_file(take_photo(),
                     attachment_filename='photo.png',
                     as_attachment=True,
                     mimetype='image/png')


@app.route(f'{API_V1}photos/<int:photo_id>/', methods=['GET'])
def get_photo(photo_id):
    pass


@app.route(f'{API_V1}photos/', methods=['POST'])
def create_photo():
    return send_file(take_photo(),
                     attachment_filename='photo.png',
                     as_attachment=True,
                     mimetype='image/png')


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
