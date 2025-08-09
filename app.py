from flask import Flask, jsonify, request
app = Flask(__name__)
users = {}
users_id = 1

@app.route('/User', methods=['POST'])
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

if __name__ == '__main__':
    app.run(debug=True)