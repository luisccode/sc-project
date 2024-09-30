from sqlalchemy import Column, Integer, String, Boolean
from .database import Base


class PurchaseRequest(Base):
    __tablename__ = "purchase_requests"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    is_read = Column(Boolean, default=False)
    is_approved = Column(Boolean, default=False)


class Acknowledgment(Base):
    __tablename__ = "acknowledgments"

    id = Column(Integer, primary_key=True, index=True)
    request_id = Column(Integer, index=True)
    acknowledged = Column(Boolean, default=False)
    approved = Column(Boolean, default=False)
