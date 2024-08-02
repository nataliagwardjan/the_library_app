from flask import Blueprint

copies_bp = Blueprint("copies", __name__)

from library.copies import copies