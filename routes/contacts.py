from flask import Blueprint

contacts = Blueprint('contacts', __name__)


@contacts.route('/')
def home():
    return "Lista de contactos"


@contacts.route('/new')
def new():
    return "saving contact"
