from flask import Flask, request, jsonify, send_file
import os

UPLOAD_DIRECTORY = "uploads"

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('FileShare.html')

@app.route('/files')
def list_files():
    files = os.listdir(UPLOAD_DIRECTORY)
    return jsonify(files)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part in the request', 400

    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400

    filename = os.path.join(UPLOAD_DIRECTORY, file.filename)
    file.save(filename)
    return 'File uploaded successfully', 200

@app.route('/uploads/<filename>', methods=['GET'])
def download_file(filename):
    return send_file(os.path.join(UPLOAD_DIRECTORY, filename), as_attachment=True)

if __name__ == '__main__':
    app.run(host='1.1.1.1', port=1111)
