from bingScrap import search
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    q = request.args.get('q')
    data = search(q)
    return jsonify(data)
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='80')
