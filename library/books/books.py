import uuid

from flask import jsonify
from library.books import books_bp


@books_bp.route('/books', methods=['GET'])
def get_all_books():
    response = {
        "success": True,
        "data": "get all books"
    }
    return jsonify(response)


@books_bp.route('/books/<uuid:book_id>', methods=['GET'])
def get_book(book_id: uuid):
    response = {
        "success": True,
        "data": f"get book with id = {book_id}"
    }
    return jsonify(response)


@books_bp.route('/authors/<uuid:author_id>/books', methods=['GET'])
def get_author_books(author_id: uuid):
    response = {
        "success": True,
        "data": f"get all author with id = {author_id} books"
    }
    return jsonify(response)


@books_bp.route('/authors/<uuid:author_id>/books', methods=['POST'])
def create_book(author_id: uuid):
    response = {
        "success": True,
        "data": f"new book wrote by author with id = {author_id} has been created"
    }
    return jsonify(response)


@books_bp.route('/books/<uuid:book_id>', methods=['PUT'])
def update_book(book_id: uuid):
    response = {
        "success": True,
        "data": f"book with id = {book_id} has been updated"
    }
    return jsonify(response)


@books_bp.route('/books/<uuid:book_id>/categories', methods=['PATCH'])
def update_book_categories(book_id: uuid):
    response = {
        "success": True,
        "data": f"categories of book with id = {book_id} has been updated"
    }
    return jsonify(response)


@books_bp.route('/books/<uuid:book_id>/audiobook', methods=['PATCH'])
def update_book_audiobook(book_id: uuid):
    response = {
        "success": True,
        "data": f"audiobook of book with id = {book_id} has been updated"
    }
    return jsonify(response)


@books_bp.route('/books/<uuid:book_id>/ebook', methods=['PATCH'])
def update_book_ebook(book_id: uuid):
    response = {
        "success": True,
        "data": f"ebook of book with id = {book_id} has been updated"
    }
    return jsonify(response)


@books_bp.route('/books/<uuid:book_id>', methods=['DELETE'])
def remove_book(book_id: uuid):
    response = {
        "success": True,
        "data": f"book with id = {book_id} has been removed"
    }
    return jsonify(response)
