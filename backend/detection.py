from roboflow import Roboflow
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.environ.get('ROBOFLOW_API_KEY')
print(API_KEY)

def predict_pill(img_path_or_url):
    rf = Roboflow(api_key=API_KEY)
    project = rf.workspace().project("pill-detection-llp4r")
    model = project.version(3).model

    # infer on an image hosted elsewhere
    print(model.predict(image_path=img_path_or_url, hosted=True, confidence=40, overlap=30).json())


