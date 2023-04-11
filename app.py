from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    image_url = requests.get('http://thecatapi.com/api/images/get').url
    return render_template('index.html', image_url=image_url)

@app.route('/new')
def get_new_cat():
    image_url = requests.get('http://thecatapi.com/api/images/get').url
    return jsonify({'image_url': image_url})

if __name__ == "__main__":
    app.run(host="0.0.0.0")
