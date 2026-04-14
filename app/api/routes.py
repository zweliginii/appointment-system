from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services import auth_service
from fastapi import Header

from app.db.database import SessionLocal
from app.schemas.appointment import AppointmentCreate
from app.services import appointment_service as service

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/admin/login")
def admin_login(username: str, password: str):
    return auth_service.login(username, password)

@router.post("/book")
def book(appointment: AppointmentCreate, db: Session = Depends(get_db)):
    if not service.is_available(db, appointment.date, appointment.time):
        return {"error": "Time slot not available"}

    return service.create_appointment(db, appointment)


@router.get("/appointments")
def get_by_date(date: str, db: Session = Depends(get_db)):
    return service.get_by_date(db, date)


@router.get("/admin/appointments")
def get_all(token: str = Header(None), db: Session = Depends(get_db)):
    if not auth_service.verify_token(token):
        return {"error": "Unauthorized"}

    return service.get_all(db)

@router.get("/availability")
def availability(date: str, db: Session = Depends(get_db)):
    return {"available_slots": service.get_available_slots(db, date)}