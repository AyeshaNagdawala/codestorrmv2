from __future__ import print_function
from googletrans import Translator
import requests
from cs50 import SQL
from flask import request, Flask, redirect, render_template, session,  send_from_directory
from flask_session import Session
from datetime import date
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
import sys


import datetime

import os.path




from helpers import login_required


app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///storm.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    acc_type = request.form.get("acc_type")
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        email = request.form.get("email")
        # Ensure email was submitted
        if not request.form.get("email"):
            print("1")
            return redirect('/login')
            
        # Ensure password was submitted
        elif not request.form.get("password"):
            print("2")
            return redirect('/login')

        # Query database for email
        rows = db.execute("SELECT * FROM users WHERE email = ?",
                          request.form.get("email"))

        # Ensure email exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            print("3")

            return redirect('/login')
        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        return redirect("/dashboard")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    session.clear()
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # get data through post
        acc_type = request.form.get("acc_type")
        email = request.form.get("email")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        hash = generate_password_hash(password)
        # empty email, password,confirmation
        if not request.form.get("email"):
            print("A")
            return redirect('/register')

        elif not request.form.get("password"):
            print("B")
            return redirect('/register')

        elif not request.form.get("confirmation"):
            print("C")

            return redirect('/register')

        if password != confirmation:
            print("D")

            return redirect('/register')

        try:
            db.execute("INSERT INTO users (email,hash, acc_type) VALUES (? ,? , ?)",
                       email, hash, acc_type)
            rows = db.execute("SELECT * FROM users WHERE email=?", email)
            session["user_id"] = rows[0]["id"]
            if acc_type == "1":
                return redirect("/details1")
            elif acc_type == "2":
                return redirect("/details2")
            elif acc_type == "3":
                return redirect("/details3")
           

        except:

            return redirect('/register')

    else:
        # User reached route via POST (as by submitting a form via GET)
        return render_template("register.html")


@app.route("/logout")
def logout():
    """Log user out"""
    # Forget any user_id
    session.clear()
    # Redirect user to login form
    return redirect("/")

@app.route("/details1", methods=["GET", "POST"])
@login_required
def details1():
    if request.method == "POST":
        # id = session["user_id"]
        # name = request.form.get("name")
        # age = request.form.get("age")
        # speciality = request.form.get("speciality")
        # gender = request.form.get("gender")
        # idlink = request.form.get("idlink")
        # regno = request.form.get("regno")
        # contact = request.form.get("contact")

        # db.execute("INSERT INTO doctor (id, name, age, gender ,speciality,idlink, regno, contact) VALUES (?, ? ,? ,?, ?,?,?,?)",
        #            id, name, age, gender, speciality, idlink, regno, contact)
        return redirect("/drdashboard")
    else:
        return render_template("details1.html")


@app.route("/details2", methods=["GET", "POST"])
@login_required
def details2():
    if request.method == "POST":
        # id = session["user_id"]
        # name = request.form.get("name")
        # age = request.form.get("age")
        # speciality = request.form.get("speciality")
        # gender = request.form.get("gender")
        # idlink = request.form.get("idlink")
        # regno = request.form.get("regno")
        # contact = request.form.get("contact")

        # db.execute("INSERT INTO doctor (id, name, age, gender ,speciality,idlink, regno, contact) VALUES (?, ? ,? ,?, ?,?,?,?)",
        #            id, name, age, gender, speciality, idlink, regno, contact)
        return redirect("/drdashboard")
    else:
        return render_template("details2.html")

@app.route("/details3", methods=["GET", "POST"])
@login_required
def details3():
    if request.method == "POST":
        # id = session["user_id"]
        # name = request.form.get("name")
        # age = request.form.get("age")
        # speciality = request.form.get("speciality")
        # gender = request.form.get("gender")
        # idlink = request.form.get("idlink")
        # regno = request.form.get("regno")
        # contact = request.form.get("contact")

        # db.execute("INSERT INTO doctor (id, name, age, gender ,speciality,idlink, regno, contact) VALUES (?, ? ,? ,?, ?,?,?,?)",
        #            id, name, age, gender, speciality, idlink, regno, contact)
        return redirect("/drdashboard")
    else:
        return render_template("details3.html")




@app.route("/dashboard")
@login_required
def dashboard():
    id = session["user_id"]    
    return render_template("dashboard.html")

@app.route("/checklist")
@login_required
def checklist():
    id = session["user_id"]    
    return render_template("checklist.html")






if __name__ == '__main__':
    main()