from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests #type: ignore


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST", "GET", "PUT", "PATCH", "DELETE"],
    allow_headers=["Authorization", "Content-Type", "X-API-Key"],
)

@app.get("/")
def read_root():
    response_ip = requests.get('https://api.ipify.org?format=json')

    response_location = requests.get(f'https://api.ipquery.io/{response_ip.json()["ip"]}')

    return response_location.json()