import os
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

from supabase import Client, create_client

from dotenv import load_dotenv

import uvicorn

load_dotenv()


app = FastAPI()

# Adicionando middleware para habilitar o CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/send")
def send(
    name: str = Form(...),
    email: str = Form(...),
    phoneNumber: str = Form(...),
    websiteUrl: str = Form(...),
    message: str = Form(...),
):
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    supabase: Client = create_client(url, key)
    tbl = supabase.table("imprinting")
    tbl.insert(
        {
            "name": name,
            "email": email,
            "phoneNumber": phoneNumber,
            "websiteUrl": websiteUrl,
            "message": message,
        }
    ).execute()
    return "OK"


# ----------------------------------------------------------------
# Main
# ----------------------------------------------------------------
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
