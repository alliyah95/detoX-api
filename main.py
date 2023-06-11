from fastapi import FastAPI
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

app = FastAPI()
tokenizer = AutoTokenizer.from_pretrained('albert-base-v2')


@app.get("/")
def root():
    return {1: "Server is up and running"}


@app.get("/api/v1/detect")
def detect(id: str, content: str):
    model = AutoModelForSequenceClassification.from_pretrained("./model/")
    tokens = tokenizer(content, truncation=True, padding=True, return_tensors="pt")
    input_tensors = tokens["input_ids"]
    model.eval()

    with torch.no_grad():
        outputs = model(input_tensors)

    logits = outputs.logits
    predicted_labels = logits.argmax(dim=1)

    return {"id": id, "content": content, "result": predicted_labels.item()}