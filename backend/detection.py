from roboflow import Roboflow
from dotenv import load_dotenv
import os
import requests
from pprint import pprint

load_dotenv()
API_KEY = os.environ.get('ROBOFLOW_API_KEY')
print(API_KEY)


def get_drug_info():
    query_string=input("Enter Drug:\n")
    url = "https://drug-info-and-price-history.p.rapidapi.com/1/druginfo"

    headers = {
        "X-RapidAPI-Key": "709f237765msh727d254c3e1eab7p1174c0jsn520d034e4002",
        "X-RapidAPI-Host": "drug-info-and-price-history.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params={"drug": query_string})

    if response.status_code == 200:
        data = response.json()
        pprint(data)
    else:
        print(f"Request for drug info failed with status code {response.status_code}")

get_drug_info()

def predict_pill(img_path_or_url):
    rf = Roboflow(api_key=API_KEY)
    project = rf.workspace().project("pill-detection-llp4r")
    model = project.version(3).model

    # infer on an image hosted elsewhere
    print(model.predict(image_path=img_path_or_url, hosted=True, confidence=40, overlap=30).json())