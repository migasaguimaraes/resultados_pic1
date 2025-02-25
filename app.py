from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# The directory where index.html and image are located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/images/<filename>')
def serve_image(filename):
    return send_from_directory(BASE_DIR, filename)

if __name__ == '__main__':
    app.run(debug=True)
