
import sys
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("main.html")
    

if __name__ == "__main__":
    app.run(debug=len(sys.argv) == 2 and sys.argv[1] == "--debug")
