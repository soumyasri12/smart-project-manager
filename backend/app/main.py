from fastapi import FastAPI

app = FastAPI(title="Smart Project Manager")


@app.get("/")
def home():
    return {"message": "Welcome to Smart Project Manager!"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}