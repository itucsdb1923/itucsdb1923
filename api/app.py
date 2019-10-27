from flask import jsonify, Blueprint

api = Blueprint("api", __name__, url_prefix="/api")


@api.route("/")
def main():
    return jsonify(["API goes here"])
