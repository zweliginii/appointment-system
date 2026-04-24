from pydantic import BaseModel

class AppointmentCreate(BaseModel):
    name: str
    phone: str
    service: str
    date: str
    time: str
