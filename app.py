from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Failed to fetch data from API'}), 500

if __name__ == '__main__':
    app.run(debug=True)
