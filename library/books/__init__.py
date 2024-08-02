from flask import Blueprint

books_bp = Blueprint("books", __name__)

from library.books import books