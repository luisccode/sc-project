from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, database

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/read_request/")
def read_request(request_id: int, db: Session = Depends(get_db)):
    request = (
        db.query(models.PurchaseRequest)
        .filter(models.PurchaseRequest.id == request_id)
        .first()
    )
    if not request:
        raise HTTPException(status_code=404, detail="Request not found")

    request.is_read = True
    db.commit()
    return request


@app.post("/acknowledge/")
def acknowledge_request(request_id: int, db: Session = Depends(get_db)):
    acknowledgment = models.Acknowledgment(request_id=request_id, acknowledged=True)
    db.add(acknowledgment)
    db.commit()
    db.refresh(acknowledgment)
    return acknowledgment
