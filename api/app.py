from flask import jsonify, Blueprint, request
from flask_jwt_extended import create_access_token, JWTManager, jwt_required
from operations import createUser, createList, getMovies, getBooks, getMusics, getMovie, getBook, getMusic, getLists, checkLogin


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

@api.route("/musics")
def musics():
    return jsonify(getMusics())

@api.route("/movies/<movie_id>")
def movie(movie_id):
    return jsonify(getMovie(movie_id))

@api.route("/books/<book_id>")
def book(book_id):
    return jsonify(getBook(book_id))

@api.route("/musics/<music_id>")
def music(music_id):
    return jsonify(getMusic(music_id))


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

    if checkLogin(username, password):
        return jsonify({"msg": "Incorrect username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200



@api.route("/jwttest", methods=['GET'])
@jwt_required
def jwttest():
    return jsonify(["Bravo! You're in."])
