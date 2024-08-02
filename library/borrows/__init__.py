from flask import Blueprint

borrows_bp = Blueprint("borrows", __name__)

from library.borrows import borrows