from myapi import db
from myapi.models import User
from flask import Blueprint, jsonify, request

bp = Blueprint('users', __name__)

@bp.route('/Users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(name=data.get("name"), email=data.get("email"))

    db.session.add(user)
    db.session.commit()

    return jsonify({"id": user.id, "name": user.name, "email": user.email})

@bp.route('/Users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    if user:
        return jsonify({"id": user.id, "name": user.name, "email": user.email})
    return jsonify({"error": "User not found"}), 404

@bp.route('/Users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get(id)
    if user:
        data = request.get_json()
        user.name = data.get("name")
        user.email = data.get("email")
        db.session.commit()
        return jsonify({"id": user.id, "name": user.name, "email": user.email})
    return jsonify({"error": "User not found"}), 404
    
@bp.route('/Users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted successfully"})
    return jsonify({"error": "User not found"}), 404
