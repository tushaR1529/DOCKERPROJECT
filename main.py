from fastapi import FastAPI

app = FastAPI(title="Docker CI Learning Project")


@app.get("/")
def home():
    return {"message": "FastAPI application running"}


@app.get("/about")
def about():
    return {"message": "Docker and GitHub Actions learning project"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/products")
def get_products():
    return [
        {"id": 1, "name": "Laptop"},
        {"id": 2, "name": "Mobile"},
        {"id": 3, "name": "Keyboard"},
    ]