import uuid

from flask import jsonify
from library.authors import authors_bp


@authors_bp.route('/authors', methods=['GET'])
def get_all_authors():
    response = {
        "success": True,
        "data": "get all authors"
    }
    return jsonify(response)


@authors_bp.route('/authors/<uuid:author_id>', methods=['GET'])
def get_author(author_id: uuid):
    response = {
        "success": True,
        "data": f"get author with id = {author_id}"
    }
    return jsonify(response)


@authors_bp.route('/authors', methods=['POST'])
def create_author():
    response = {
        "success": True,
        "data": "new author has been created"
    }
    return jsonify(response)


@authors_bp.route('/authors/<uuid:author_id>', methods=['PUT'])
def update_author(author_id: uuid):
    response = {
        "success": True,
        "data": f"author with id = {author_id} has been updated"
    }
    return jsonify(response)


@authors_bp.route('/authors/<uuid:author_id>', methods=['DELETE'])
def removed_author(author_id: uuid):
    response = {
        "success": True,
        "data": f"author with id = {author_id} has been removed"
    }
    return jsonify(response)
