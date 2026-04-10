from fastapi import FastAPI 

app = FastAPI()


@app.get("/")
def home():
    return "welcome to the fastapi.. "

@app.get("/contact")
def contact():
    return "you can contact us any time"    