from fastapi import FastAPI
import socket 

app= FastAPI()
@app.get("/")
def root():
    return {"id": socket.gethostname()}