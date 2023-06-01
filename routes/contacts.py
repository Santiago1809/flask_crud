from flask import Blueprint, render_template, request, redirect
from models.contact import Contact
from utils.db import db

contacts = Blueprint('contacts', __name__)


@contacts.route('/')
def home():
    contacts = Contact.query.all()
    return render_template("index.html", contacts=contacts)


@contacts.route('/new', methods=['POST'])
def new():
    fullname = request.form['fullname']
    email = request.form['email']
    phone = request.form['phone']

    new_contact = Contact(fullname, email, phone)
    try:
        db.session.add(new_contact)
        db.session.commit()
        return redirect("/")
    except:
        return "error al guardar"


@contacts.route("/about")
def about():
    return render_template("about.html")


@contacts.route("/update")
def update():
    return render_template("update.html")


@contacts.route("/delete")
def delete():
    return "delete"
