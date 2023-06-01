from flask import Blueprint, render_template, request

contacts = Blueprint('contacts', __name__)


@contacts.route('/')
def home():
    return render_template("index.html")


@contacts.route('/new')
def new():
    return render_template("new.html")


@contacts.route("/about")
def about():
    return render_template("about.html")


@contacts.route("/update")
def update():
    return render_template("update.html")


@contacts.route("/delete")
def delete():
    return "delete"
