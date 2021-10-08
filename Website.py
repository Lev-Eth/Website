from flask import Flask, render_template

Website = Flask(__name__)

@Website.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    Website.run(debug=True)
