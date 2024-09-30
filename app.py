import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from purchase_request_app.purchase_request_app import app as purchase_request_app
from read_acknowledge_app.read_acknowledge_app import app as read_acknowledge_app

main_app = FastAPI()

main_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

main_app.mount("/purchase", purchase_request_app)
main_app.mount("/acknowledge", read_acknowledge_app)

if __name__ == "__main__":
    uvicorn.run("app:main_app", host="0.0.0.0", port=8000, reload=True)
