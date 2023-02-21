from flask import Flask, render_template

app = Flask(__name__)



@app.route("/")
def welcome():
    return render_template(
        "wc.html",
        message="**Jinja variable at work here!**"
        )


