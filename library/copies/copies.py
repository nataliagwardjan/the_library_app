import uuid

from flask import jsonify
from library.copies import copies_bp


@copies_bp.route('/copies', methods=['GET'])
def get_all_copies():
    response = {
        "success": True,
        "data": "get all copies"
    }
    return jsonify(response)


@copies_bp.route('/copies/<uuid:copy_id>', methods=['GET'])
def get_copy(copy_id: uuid):
    response = {
        "success": True,
        "data": f"get author with id = {copy_id}"
    }
    return jsonify(response)


@copies_bp.route('/books/<uuid:book_id>/copies', methods=['GET'])
def get_all_book_copies(book_id: uuid):
    response = {
        "success": True,
        "data": f"get all copies by book with id = {book_id}"
    }
    return jsonify(response)


@copies_bp.route('/books/<uuid:book_id>/copies', methods=['POST'])
def create_copy(book_id: uuid):
    response = {
        "success": True,
        "data": f"new copy for book with id = {book_id} has been created"
    }
    return jsonify(response)


@copies_bp.route('/copies/<uuid:copy_id>/status', methods=['PATCH'])
def copy_status_change(copy_id: uuid):
    response = {
        "success": True,
        "data": f"copy's with id = {copy_id} status has been changed"
    }
    return jsonify(response)


@copies_bp.route('/copies/<uuid:copy_id>', methods=['DELETE'])
def removed_copy(copy_id: uuid):
    response = {
        "success": True,
        "data": f"copy with id = {copy_id} has been removed"
    }
    return jsonify(response)
