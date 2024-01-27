from roboflow import Roboflow
from dotenv import load_dotenv
import os
import requests
from pprint import pprint 
import cv2
from pathlib import Path
from typing import Union, List

load_dotenv()
API_KEY = os.environ.get('ROBOFLOW_API_KEY')
print(API_KEY)


def get_drug_info():
    url = "https://drug-info-and-price-history.p.rapidapi.com/1/druginfo"

    headers = {
        "X-RapidAPI-Key": "709f237765msh727d254c3e1eab7p1174c0jsn520d034e4002",
        "X-RapidAPI-Host": "drug-info-and-price-history.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params={"drug": 'query_string'})

    if response.status_code == 200:
        data = response.json()
        pprint(data)
    else:
        print(f"Request for drug info failed with status code {response.status_code}")

# get_drug_info()
# 
def predict_pill(img_path_or_url):
    rf = Roboflow(api_key=API_KEY)
    project = rf.workspace().project("pill-detection-llp4r")
    model = project.version(3).model

    # infer on an image hosted elsewhere
    return model.predict(image_path=img_path_or_url, confidence=40, overlap=30).json()



def image_with_bboxes(frame: Union[Path, cv2.Mat], face_data: List[dict]) -> cv2.Mat:
    if isinstance(frame, Path):
        image = cv2.imread(str(frame))
    elif isinstance(frame, cv2.Mat):
        image = frame.copy()
    else:
        raise TypeError('frame type must be Path or cv2.Mat Object')

    boxes = [face['bbox'].values() for face in face_data]
    for (left, top, right, bottom) in boxes:
        cv2.rectangle(image, (left, top), (right, bottom), (0,255,0), 2)

    return image