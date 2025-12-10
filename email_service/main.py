from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Service": "Email Service", "Status": "Active"}

@app.get("/send")
def send_email():
    return {"Action": "Sending Email...", "Status": "Sent"}