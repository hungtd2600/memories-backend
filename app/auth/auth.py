import jwt
import datetime
import os
from app.models.models import DatabaseManager

SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")

def generate_token(username):
    payload = {
        'username': username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

def verify_login(username, password):
    db = DatabaseManager(db_path='database/memories.db')
    user = db.get_user(username)
    if user and user[1] == password:
        return True
    return False

def verify_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload['username']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None