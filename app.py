import os
from flask import Flask, request, render_template, redirect
from flask import Request, Response, url_for, jsonify
from pathlib import Path
from backend.detection import predict_pill
from werkzeug.datastructures import FileStorage

app = Flask(__name__, template_folder='frontend', static_folder='frontend/static')
 
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/index', methods= ['GET']) 
def index():
    return render_template('index.html')

@app.route('/result')
def resul():
    r : Request = request
    return render_template('re.html',content =  r.args.get('content'))

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about_us.html')

@app.route('/upload', methods=['GET','POST'])
def upload():
    r: Request = request
    if 'file' not in r.files: 
        return "No file part"
    
    file: FileStorage = r.files['file']
    print(file)
    
    if file.filename == '':
        return "No selected file"
    
    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)

        
        path =os.path.join(os.getcwd(), os.listdir('uploads')[0])
        if path:
            data = predict_pill(path)
            classi = data['predictions'][0]['class']
            print(classi)
            return jsonify({'class': classi})



@app.route('/')
def homepage():
    return "running"




if __name__ == "__main__":

    # Run the Flask app
    app.run("127.0.0.1", port=8080, debug=True)
    
