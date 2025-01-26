from fastapi import FastAPI
import requests #type: ignore

app = FastAPI()

@app.get("/")
def read_root():
    response_ip = requests.get('https://api.ipify.org?format=json')

    response_location = requests.get(f'https://api.ipquery.io/{response_ip.json()["ip"]}')

    return response_location.json()