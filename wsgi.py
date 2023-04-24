from flask import render_template

from blog.app import create_app

app = create_app()


@app.route("/")
def index():
    return render_template("base.html")


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        debug=True,
        port=8000
    )
