from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, IPvAnyAddress
import requests #type: ignore


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST", "GET", "PUT", "PATCH", "DELETE"],
    allow_headers=["Authorization", "Content-Type", "X-API-Key"],
)

class IpSchema(BaseModel):
    ip_address: IPvAnyAddress

@app.get("/")
def read_root(ip_address: IpSchema = Query(..., title="IP Address", description="IP Address to get location")):
    ip = ip_address.ip_address

    response_location = requests.get(f'https://api.ipquery.io/{ip}')

    return response_location.json()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=80)