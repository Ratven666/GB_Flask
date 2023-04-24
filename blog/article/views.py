from flask import Blueprint, render_template

from blog.user.views import USERS

article = Blueprint("article", __name__, url_prefix="/articles", static_folder="../statics")

ARTICLES = {
    1: {"authors": [1],
        "title": "Статья 1",
        "abstract": "Abstract_1",
        "text": "Full text 1"
        },
    2: {"authors": [1, 2],
        "title": "Статья 2",
        "abstract": "Abstract_2",
        "text": "Full text 2"
        },
    3: {"authors": [1, 2, 3],
        "title": "Статья 3",
        "abstract": "Abstract_3",
        "text": "Full text 3"
        },
}


@article.route("/")
def articles_list():
    return render_template("articles/list.html",
                           articles=ARTICLES,
                           users=USERS)


@article.route("/<int:pk>")
def get_article(pk: int):
    return render_template("articles/detail.html",
                           article_id=pk,
                           articles=ARTICLES,
                           users=USERS)
