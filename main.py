from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import torch
import random
from transformers import AutoTokenizer, AutoModelForSequenceClassification

app = FastAPI()
tokenizer = AutoTokenizer.from_pretrained('jcblaise/roberta-tagalog-base')

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
    model = AutoModelForSequenceClassification.from_pretrained("./model/")
    tokens = tokenizer(content, truncation=True, padding=True, return_tensors="pt")
    input_tensors = tokens["input_ids"]
    model.eval()

    with torch.no_grad():
        outputs = model(input_tensors)

    logits = outputs.logits
    predicted_labels = logits.argmax(dim=1)

    return {"result": predicted_labels.item()}



@app.get("/api/v1/fake_detect")
def fake_detect(content:str):
    result = random.choice([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) 
    return {"result": result}
