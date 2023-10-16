from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

import uvicorn

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
    return name, email, phoneNumber, websiteUrl, message


# ----------------------------------------------------------------
# Main
# ----------------------------------------------------------------
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
