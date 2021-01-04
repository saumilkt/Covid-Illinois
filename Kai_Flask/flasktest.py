from flask import Flask, redirect, url_for, render_template, request
from os import path, environ
import pathlib
import scatterplot

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods=["POST","GET"])
def search():
    if request.method == "POST":
        day = request.form["day"]
        month = request.form["month"]
        stat = request.form["stat"]

        return redirect(url_for("plot", dy = day, mn = month, st = stat))
    else:
        return render_template("search.html")

@app.route("/<dy>/<mn>/<st>")
def plot(dy, mn, st):
    location = scatterplot.create_scatter(dy, mn, st)
    return render_template("scatter.html", scatter = location)

if __name__ == "__main__":
    app.run()