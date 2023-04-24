from flask import Blueprint, render_template

user = Blueprint("user", __name__, url_prefix="/users", static_folder="../statics")

USERS = {
    1: "Mike",
    2: "Иван",
    3: "Сергей"
}


@user.route("/")
def user_list():
    return render_template("users/list.html", users=USERS)


@user.route("/<int:pk>")
def get_user(pk: int):
    return render_template("users/detail.html",
                           user_id=pk,
                           users=USERS)
