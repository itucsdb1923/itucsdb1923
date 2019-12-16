from operations import *
from flask import jsonify, Blueprint, request
from flask_jwt_extended import (
    create_access_token, JWTManager, jwt_required, get_jwt_identity)
import datetime

api = Blueprint("api", __name__, url_prefix="/api")


@api.route("/")
def main():
    return jsonify(getLists())


@api.route("/movies")
def movies():
    return jsonify(getMovies())


@api.route("/books")
def books():
    return jsonify(getBooks())


@api.route("/music")
def musics():
    return jsonify(getMusics())


@api.route("/movie/<movie_id>")
def movie(movie_id):
    return jsonify(getMovie(movie_id))


@api.route("/book/<book_id>")
def book(book_id):
    return jsonify(getBook(book_id))


@api.route("/music/<music_id>")
def music(music_id):
    return jsonify(getMusic(music_id))


@jwt_required
@api.route("/user/<username>/lists")
def userlists(username):
    return jsonify(getUserLists(username))

    
@jwt_required
@api.route("/<username>")
def profilelists(username):
    return jsonify(getProfileLists(username))


@api.route("/list/<list_id>")
def list(list_id):
    return jsonify(getListItems(list_id))


@api.route("/createlist")
@jwt_required
def newList():
    username = request.args.get("username")
    if get_jwt_identity() == username:
        name = request.args.get("name")
        date = datetime.datetime.now()
        createList(name, date, username)
        return jsonify({"msg": "Success"}), 200
    return jsonify({"msg": "Something went wrong"}), 401


@api.route("/list/additem")
@jwt_required
def addItem():

    if get_jwt_identity() == request.args.get("username"):
        type = request.args.get("type")
        itemId = request.args.get("itemId")
        listId = request.args.get("listId")
        addListItem(type, itemId, listId)
        return jsonify({"msg": "Success"}), 200
    return jsonify({"msg": "Something went wrong"}), 401


@api.route("/list/removeitem")
@jwt_required
def removeItem():

    if get_jwt_identity() == request.args.get("username"):
        type = request.args.get("type")
        itemId = request.args.get("itemId")
        listId = request.args.get("listId")
        deleteListItem(type, itemId, listId)
        return jsonify({"msg": "Success"}), 200
    return jsonify({"msg": "Something went wrong"}), 401


@api.route("/login", methods=["POST"])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    if checkLogin(username, password):
        ret = {
            "username": username,
            "access_token": create_access_token(identity=username, expires_delta=datetime.timedelta(days=14))
        }
        return jsonify(ret), 200
    else:
        return jsonify({"msg": "Incorrect username or password"}), 401


@api.route("/change_pw", methods=["POST"])
def change_password():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    new_password = request.json.get('new_password', None)

    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400
    if not new_password:
        return jsonify({"msg": "Missing new password parameter"}), 400

    if changePassword(username, password, new_password):
        return jsonify({"msg": "Password changed succesfully"}), 200
    else:
        return jsonify({"msg": "Incorrect username or password"}), 401


@api.route("/refresh", methods=["POST"])
@jwt_required
def refresh():
    username = get_jwt_identity()
    ret = {
        "username": username,
        "access_token": create_access_token(identity=username, expires_delta=datetime.timedelta(days=14))
    }
    return jsonify(ret), 200


@api.route("/register", methods=["POST"])
def register():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    if createUser(username, password):
        return jsonify({"msg": "Success"}), 200
    else:
        return jsonify({"msg": "User already exists"}), 401


@api.route("/jwttest", methods=['GET'])
@jwt_required
def jwttest():
    return jsonify(["Bravo! You're in."])
