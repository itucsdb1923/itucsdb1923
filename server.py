from flask import Flask, render_template, jsonify
from flask_jwt_extended import JWTManager
from api.app import api
from settings import SECRET_KEY
app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = SECRET_KEY
jwt = JWTManager(app)
app.register_blueprint(api)


@app.route("/", defaults={"path": None})
@app.route("/<path:path>")
def home_page(path):
    return app.send_static_file("main.html")


if __name__ == "__main__":
    app.run()
