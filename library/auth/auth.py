from library.auth import auth_bp
from flask import jsonify, abort


@auth_bp.route('/register', methods=['POST'])
def register():
    response = {
        "success": True,
        "token": "token"
    }

    return jsonify(response)


@auth_bp.route('/login', methods=['POST'])
def login():
    response = {
        "success": True,
        "token": "token"
    }

    return jsonify(response)

