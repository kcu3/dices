from randomgen import random
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        do = request.form['d']
        if do == "stop":
            return render_template('index.html', content=[3, 8])
    return render_template('index.html', content=random())


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)  # host='0.0.0.0'
