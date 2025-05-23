from flask import Flask, json, render_template, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/disease', methods=['GET'])
def camera():
    return render_template('camera.html')

@app.route('/price')
def price():
    with open('data.json', 'r') as file:
        data = json.load(file)
    
    return render_template('price.html', data=json.dumps(data))
    

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/seed')
def seed():
    return render_template('seed.html')

@app.route('/market')
def market():
    return render_template('market.html')

# app.run(debug=True)