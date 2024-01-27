import requests
from pprint import pprint

url = "https://drug-info-and-price-history.p.rapidapi.com/1/druginfo"

headers = {
    "X-RapidAPI-Key": "709f237765msh727d254c3e1eab7p1174c0jsn520d034e4002",
	"X-RapidAPI-Host": "drug-info-and-price-history.p.rapidapi.com"
}
#allurl=url,url1
query_string=input("Enter Drug: \n")
response=requests.get(url,headers=headers,params={"drug": query_string})


if response.status_code==200:
    data=response.json()
   

pprint(response.json())