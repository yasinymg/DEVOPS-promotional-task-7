from flask import Flask

app = Flask()

@app.get("/")
def read_root():
    return {"message": "Hello, Welcome to KodeCamp DevOps Bookcamp!"}