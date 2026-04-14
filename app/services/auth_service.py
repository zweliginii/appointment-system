ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "1234"  # we will upgrade this later

def login(username: str, password: str):
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        return {"token": "secure_admin_token"}
    return {"error": "Invalid credentials"}

def verify_token(token: str):
    return token == "secure_admin_token"