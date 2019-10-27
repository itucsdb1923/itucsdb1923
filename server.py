
import sys
from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route("/api")
def api():
    return jsonify(["API goes here lol"])


@app.route("/", defaults={"route": None})
@app.route("/<route>")
def home_page(route):
    return render_template("main.html")
    

if __name__ == "__main__":
    app.run(debug=len(sys.argv) == 2 and sys.argv[1] == "--debug")
