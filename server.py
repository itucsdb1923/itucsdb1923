from flask import Flask, render_template, jsonify
from flask_jwt_extended import JWTManager
from api.app import api

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)
app.register_blueprint(api)


@app.route("/", defaults={"route": None})
@app.route("/<route>")
def home_page(route):
    return render_template("main.html")


if __name__ == "__main__":
    app.run()
