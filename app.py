import re
from flask import Flask, render_template, request
import sqlite3

from flask.scaffold import _matching_loader_thinks_module_is_package

app = Flask(__name__)
DATABASE = "beautyslayers.db"
booksite = "https://booksy.com/en-us/613987_beauty-slayers-salon_hair-salon_14741_lake-havasu-city"


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute("SELECT * FROM main ORDER BY other")
        slayerList = cur.fetchall()
        return render_template("index.html", slayerList=slayerList, booksite=booksite)
    if request.method == "POST":
        if request.form.get("moreInfo") == "moreInfo":
            slayerChoice = request.form.get("slayerChoice")
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("SELECT * FROM main WHERE other  = ?", (slayerChoice,))
            slayer = cur.fetchall()
            return render_template("bio.html", booksite=booksite, slayer=slayer)


@app.route('/add', methods=["GET", "POST"])
def add():
    if request.method == "GET":
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute("SELECT * FROM main ORDER BY other")
        slayerList = cur.fetchall()
        return render_template("add.html", slayerList=slayerList)

    if request.method == "POST":
        if request.form.get("submit") == "submit":
            photo = request.form.get("photo")
            firstName = request.form.get("fName")
            lastName = request.form.get("lName")
            businessName = request.form.get("bName")
            position = request.form.get("position")
            phone = request.form.get("phone")
            instaGram = request.form.get("instagram")
            faceBook = request.form.get("facebook")
            profile = request.form.get("profile")
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("INSERT INTO main (photo, firstName, lastName, businessName, position, phone, instaGram, faceBook, profile) VALUES (?,?,?,?,?,?,?,?,?)",
                        (photo, firstName, lastName, businessName, position, phone, instaGram, faceBook, profile))
            conn.commit()
            cur.execute("SELECT * FROM main ORDER BY other")
            slayerList = cur.fetchall()
            return render_template("add.html", slayerList=slayerList)

        if request.form.get("delete") == "delete":
            other = request.form.get("other")
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("DELETE FROM main WHERE other = ?", (other,))
            conn.commit()
            cur.execute("SELECT * FROM main ORDER BY other")
            slayerList = cur.fetchall()
        return render_template("add.html", slayerList=slayerList)


@app.route('/about', methods=["GET", "POST"])
def about():
    return render_template("about.html")


@app.route('/services', methods=["GET", "POST"])
def services():
    return render_template("services.html", booksite=booksite)


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute("SELECT * FROM main ORDER BY other")
        slayerList = cur.fetchall()
        return render_template("contact.html", slayerList=slayerList, booksite=booksite)


@app.route('/careers', methods=["GET", "POST"])
def careers():
    if request.method == "GET":
        return render_template("careers.html")


@app.route('/shop', methods=["GET", "POST"])
def shop():
    if request.method == "GET":
        return render_template("shop.html")
