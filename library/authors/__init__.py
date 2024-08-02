from flask import Blueprint

authors_bp = Blueprint("authors", __name__)

from library.authors import authors