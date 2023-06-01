from flask import Blueprint, render_template, request, redirect, url_for, flash
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
        flash('Contact created successfully!')
        return redirect(url_for('contacts.home'))
    except:
        return "error al guardar"


@contacts.route("/update/<id>", methods=["POST", "GET"])
def update(id):
    contact = Contact.query.get(id)
    if request.method == "POST":
        try:
            contact.fullname = request.form["fullname"]
            contact.email = request.form["email"]
            contact.phone = request.form["phone"]
            db.session.commit()
            flash("Contact updated")
            return redirect(url_for('contacts.home'))
        except:
            return render_template("ErrorSaving.html")
    return render_template("update.html", contact=contact)


@contacts.route("/delete/<id>")
def delete(id):
    try:
        contact = Contact.query.get(id)
        db.session.delete(contact)
        db.session.commit()
        flash("Contact deleted")
        return redirect(url_for('contacts.home'))
    except:
        return render_template("ErrorDeleting.html")
