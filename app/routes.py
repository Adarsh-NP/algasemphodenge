import datetime
from app import app, db
from flask import render_template, request, flash, redirect, url_for

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")