from flask import Flask, render_template,redirect, url_for, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

@app.route("/")
def index():
    session["test"] = "test"
    return render_template ('index.html')
