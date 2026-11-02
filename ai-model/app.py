
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "AI Model is Running"}

@app.post("/predict")
def predict(data: dict):
    text = data.get("text", "")

    result = "AI Processed: " + text

    return {"prediction": result}
