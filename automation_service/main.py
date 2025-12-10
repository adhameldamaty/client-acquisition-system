from fastapi import FastAPI
import httpx  

app = FastAPI()

@app.get("/")
def read_root():
    return {"Service": "Automation Service", "Status": "Active"}

@app.get("/trigger")
async def trigger_automation():
    
    
    
    
    async with httpx.AsyncClient() as client:
        response = await client.get("http://email_service:80/send")
    
    
    return {
        "Automation_Action": "Workflow Started",
        "Email_Service_Response": response.json()
    }