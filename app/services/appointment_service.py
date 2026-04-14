from sqlalchemy.orm import Session
from app.db import models

ALL_TIMES = [
    "09:00", "10:00", "11:00", "12:00",
    "13:00", "14:00", "15:00"
]

def create_appointment(db: Session, appointment):
    db_appointment = models.Appointment(**appointment.dict())
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment


def get_by_date(db: Session, date: str):
    return db.query(models.Appointment).filter(models.Appointment.date == date).all()


def get_all(db: Session):
    return db.query(models.Appointment).all()


def is_available(db: Session, date: str, time: str):
    existing = db.query(models.Appointment).filter(
        models.Appointment.date == date,
        models.Appointment.time == time
    ).first()

    return existing is None


def get_available_slots(db: Session, date: str):
    booked = get_by_date(db, date)
    booked_times = [b.time for b in booked]

    return [t for t in ALL_TIMES if t not in booked_times]