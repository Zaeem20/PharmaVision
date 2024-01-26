from flask import Flask 
from flask import request, jsonify, url_for

app = Flask(__name__)

@app.route('/index', method = ['GET' 'POST']) 
def index():
    return "this is index page"
@app.route('/about', method=['GET', 'POST'])
def about():
    return "About Page"

if __name__ == "__main__":
    app.run(debug=True)
    
