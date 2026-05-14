# 📅 Appointment Booking System

A full-stack appointment booking system built with **FastAPI (backend)** and **Streamlit (frontend)**. This project allows customers to book appointments and admins to manage bookings through a secure dashboard.

---

## 🚀 Features

### 👤 Customer

* Book appointments
* View available time slots
* Prevent double booking

### 🧑‍💼 Admin

* Login authentication
* View all appointments
* Secure dashboard access

---

## 🧱 Tech Stack

| Layer           | Technology   |
| --------------- | ------------ |
| Backend         | FastAPI      |
| Frontend        | Streamlit    |
| Database        | SQLite       |
| Server          | Uvicorn      |
| Version Control | Git + GitHub |

---

## 📂 Project Structure

```
appointment_system/
│
├── app/
│   ├── api/
│   ├── db/
│   ├── schemas/
│   ├── services/
│   └── main.py
│
├── frontend/
│   └── app.py
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/YOUR_USERNAME/appointment-system.git
cd appointment-system
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Running the Application

### 🔵 Start Backend (FastAPI)

```
uvicorn app.main:app --reload
```

Backend runs on:

```
http://127.0.0.1:8000
```

API Docs:

```
http://127.0.0.1:8000/docs
```

---

### 🟣 Start Frontend (Streamlit)

```
streamlit run frontend/app.py
```

Frontend runs on:

```
http://localhost:8501
```

---

## 🔐 Admin Login

Default credentials:

```
Username: admin
Password: 1234
```

---

## 🌐 Deployment (Overview)

### Backend

* Deploy on Render
* Uses FastAPI + Uvicorn

### Frontend

* Deploy on Streamlit Cloud

---

## 🔄 Git Workflow

```
git add .
git commit -m "message"
git push
```

---

## 🧠 Future Improvements

* PostgreSQL database
* JWT authentication
* Payment integration
* Notifications (SMS/Email)
* Docker containerization
* Scalable cloud architecture

---

## 📌 Summary

This project demonstrates:

* Full-stack development
* API design with FastAPI
* UI development with Streamlit
* Git & GitHub workflow
* Deployment-ready architecture

---

## 👨‍💻 Author

zweli_gini
---

## 📄 License

This project is open-source and available under the MIT License.
