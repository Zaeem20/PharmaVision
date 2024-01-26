import os
from flask import Flask, request, render_template
from flask import Request

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/index', methods= ['GET' 'POST']) 
def index():
    return "this is index page"

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about_us.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    
    if file.filename == '':
        return "No selected file"
    
    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        return "File uploaded successfully"

if __name__ == "__main__":
    app.run(debug=True)
    
