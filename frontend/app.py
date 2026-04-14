import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

# -----------------------------
# SESSION STATE INIT
# -----------------------------
if "token" not in st.session_state:
    st.session_state["token"] = None

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False


# -----------------------------
# TITLE
# -----------------------------
st.title("📅 Appointment System")

mode = st.radio("Select Mode", ["Customer", "Admin"])

st.markdown("---")


# =========================================================
# 👤 CUSTOMER MODE
# =========================================================
if mode == "Customer":

    st.subheader("📅 Book Appointment")

    name = st.text_input("Your Name")
    phone = st.text_input("Phone Number")

    service = st.selectbox("Select Service", ["Haircut", "Shave", "Consultation"])

    date = st.date_input("Select Date")

    # -----------------------------
    # GET AVAILABLE TIMES
    # -----------------------------
    available_times = []

    if date:
        try:
            response = requests.get(
                f"{API_URL}/availability",
                params={"date": str(date)}
            )

            if response.status_code == 200:
                available_times = response.json()["available_slots"]

        except:
            st.error("Backend not running")

    # -----------------------------
    # TIME SELECTION
    # -----------------------------
    if available_times:
        time = st.selectbox("Select Time", available_times)
    else:
        st.warning("No available slots")
        time = None

    # -----------------------------
    # BOOK
    # -----------------------------
    if st.button("Book Appointment") and time:

        data = {
            "name": name,
            "phone": phone,
            "service": service,
            "date": str(date),
            "time": time
        }

        try:
            response = requests.post(
                f"{API_URL}/book",
                json=data
            )

            result = response.json()

            if "error" in result:
                st.error(result["error"])
            else:
                st.success("✅ Appointment booked!")

        except:
            st.error("Backend error")


# =========================================================
# 🧑‍💼 ADMIN MODE
# =========================================================
if mode == "Admin":

    st.subheader("🔐 Admin Panel")

    # -----------------------------
    # LOGIN (ONLY IF NOT LOGGED IN)
    # -----------------------------
    if not st.session_state["logged_in"]:

        admin_user = st.text_input("Username")
        admin_pass = st.text_input("Password", type="password")

        if st.button("Login"):

            response = requests.post(
                f"{API_URL}/admin/login",
                params={"username": admin_user, "password": admin_pass}
            )

            result = response.json()

            if "token" in result:
                st.session_state["token"] = result["token"]
                st.session_state["logged_in"] = True
                st.success("Login successful 🔥")
                st.rerun()
            else:
                st.error("Invalid credentials")

    # -----------------------------
    # DASHBOARD (ONLY IF LOGGED IN)
    # -----------------------------
    else:

        st.success("Logged in as admin")

        # LOGOUT
        if st.button("🚪 Logout"):
            st.session_state["token"] = None
            st.session_state["logged_in"] = False
            st.rerun()

        # LOAD APPOINTMENTS
        if st.button("Load Appointments"):

            headers = {"token": st.session_state["token"]}

            response = requests.get(
                f"{API_URL}/admin/appointments",
                headers=headers
            )

            if response.status_code == 200:
                data = response.json()

                if len(data) == 0:
                    st.info("No appointments found")
                else:
                    for appt in data:
                        st.write(f"""
                        👤 Name: {appt['name']}  
                        📞 Phone: {appt['phone']}  
                        💇 Service: {appt['service']}  
                        📅 Date: {appt['date']}  
                        ⏰ Time: {appt['time']}
                        """)
                        st.markdown("---")
            else:
                st.error("Failed to load data")