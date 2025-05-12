from flask import Flask, json, render_template, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/penyakit', methods=['GET'])
def kamera():
    return render_template('kamera.html')

@app.route('/price')
def price():
    with open('data.json', 'r') as file:
        data = json.load(file)
    
    return render_template('price.html', data=json.dumps(data))
    

@app.route('/about')
def about():
    return render_template('about.html')

# app.run(debug=True)