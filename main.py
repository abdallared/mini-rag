from fastapi import FastAPI, File, UploadFile
app = FastAPI() 


@app.get("/welcome")


def welcome():
    return {"message": "Welcome to the mini RAG project!"}