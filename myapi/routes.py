from myapi.models import users, users_id
from flask import Blueprint, jsonify, request

bp = Blueprint('users', __name__)

@bp.route('/Users', methods=['POST'])
def createuser():
    global users_id
    data_json = request.get_json()
    user = {
        "id": users_id,
        "name": data_json.get("name"),
        "email": data_json.get("email")
    }
    users[users_id] = user
    users_id += 1
    return jsonify(user)

@bp.route('/Users/<int:id>', methods=['GET'])
def get_id(id):
    if id in users:
        return jsonify(users[id])
    else:
        return jsonify({"Erro": "User not found"})
    
@bp.route('/Users/<int:id>', methods=['PUT'])
def upgrade_user(id):
    if id in users:
        data_json = request.get_json()
        users[id]["name"] = data_json.get("name")
        users[id]["email"] = data_json.get("email")
        return jsonify(users[id])
    else:
        return jsonify({"User": "not found"})
    
@bp.route('/Users/<int:id>', methods=['DELETE'])
def delete_user(id):
    if id in users:
        del(users[id])
        return jsonify({"User": "Deleted successfully"})
    else:
        return jsonify({"User": "not found"})