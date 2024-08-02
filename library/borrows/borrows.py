import uuid

from flask import jsonify
from library.borrows import borrows_bp


@borrows_bp.route('/borrows', methods=['GET'])
def get_all_borrows():
    response = {
        "success": True,
        "data": "get all borrows"
    }
    return jsonify(response)


@borrows_bp.route('/borrows/<uuid:borrow_id>', methods=['GET'])
def get_borrow(borrow_id: uuid):
    response = {
        "success": True,
        "data": f"get author with id = {borrow_id}"
    }
    return jsonify(response)


@borrows_bp.route('/users/<uuid:user_id>/borrows', methods=['GET'])
def get_all_user_borrows(user_id: uuid):
    response = {
        "success": True,
        "data": f"get all borrows by user with id = {user_id}"
    }
    return jsonify(response)


@borrows_bp.route('/users/<uuid:user_id>/borrows', methods=['POST'])
def create_borrow(user_id: uuid):
    response = {
        "success": True,
        "data": f"new borrow for user with id = {user_id} has been created"
    }
    return jsonify(response)


@borrows_bp.route('/borrows/<uuid:borrow_id>/extend', methods=['PATCH'])
def extend_borrow(borrow_id: uuid):
    response = {
        "success": True,
        "data": f"borrow with id = {borrow_id} has been extended"
    }
    return jsonify(response)


@borrows_bp.route('/borrows/<uuid:borrow_id>/return', methods=['PATCH'])
def return_borrow(borrow_id: uuid):
    response = {
        "success": True,
        "data": f"borrow with id = {borrow_id} has been returned"
    }
    return jsonify(response)


@borrows_bp.route('/borrows/<uuid:borrow_id>', methods=['DELETE'])
def removed_borrow(borrow_id: uuid):
    response = {
        "success": True,
        "data": f"borrow with id = {borrow_id} has been removed"
    }
    return jsonify(response)
