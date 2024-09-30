from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from . import models, database

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)


class PurchaseRequestCreate(BaseModel):
    description: str


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/purchase_request/")
def create_purchase_request(
    request: PurchaseRequestCreate, db: Session = Depends(get_db)
):
    new_request = models.PurchaseRequest(description=request.description)
    db.add(new_request)
    db.commit()
    db.refresh(new_request)
    return new_request
