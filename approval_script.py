import time
from sqlalchemy.orm import Session
from purchase_request_app.database import engine
from purchase_request_app.models import Acknowledgment


def approve_requests():
    db = Session(bind=engine)
    while True:
        requests = (
            db.query(Acknowledgment)
            .filter(
                Acknowledgment.acknowledged == True, Acknowledgment.approved == False
            )
            .all()
        )
        for ack in requests:
            time.sleep(120)
            ack.approved = True
            db.commit()
        time.sleep(10)
    db.close()


if __name__ == "__main__":
    approve_requests()
