from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import torch
from transformers import pipeline

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Content-Type"],
)

@app.get("/")
def root():
    return {1: "Server is up and running"}

@app.get("/api/v1/detect")
def detect(content: str):
    classifier = pipeline("text-classification", model="./model")
    if (classifier(content)[0]['label'] == "HATE"):
        return {'result': 1}
    else:
        return {'result': 0}
    