import requests
import json
from pprint import pprint

url = "https://drug-info-and-price-history.p.rapidapi.com/1/druginfo"
#url1=       "https://myhealthbox.p.rapidapi.com/search/updatedDocuments"
headers = {
	"X-RapidAPI-Key": "dfd5904948mshea0180e7ead8fbfp161f57jsn01fb9cfdea58",
    #"X-RapidAPI-Key": "dfd5904948mshea0180e7ead8fbfp161f57jsn01fb9cfdea58",
	#"X-RapidAPI-Host": "myhealthbox.p.rapidapi.com",
	"X-RapidAPI-Host": "drug-info-and-price-history.p.rapidapi.com"
}
#allurl=url,url1
query_string=input("Enter Drug: \n")
response=requests.get(url,headers=headers,params={"drug": query_string})

if response.status_code==200:
    data=response.json()
pprint(response.json())