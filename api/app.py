from flask import jsonify, Blueprint, request
from flask_jwt_extended import create_access_token, JWTManager, jwt_required


api = Blueprint("api", __name__, url_prefix="/api")


@api.route("/")
def main():
    return jsonify(["API goes here"])


@api.route("/login", methods=["POST"])
def login():
    print(request.json)
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    
    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    if username != 'test' or password != 'test':
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200



@api.route("/jwttest", methods=['GET'])
@jwt_required
def jwttest():
    return jsonify(["Bravo! You're in."])
