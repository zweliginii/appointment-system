from fastapi import FastAPI
from app.db.database import Base, engine
from app.api.routes import router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Appointment System Running"}