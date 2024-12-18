from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    me = {
        "first_name": "Ava",
        "last_name": "Tuttle",
        "hobbies": "video games, DnD, guitar",
        "is_online": True
    }
    return me