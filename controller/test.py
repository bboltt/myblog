from flask import Blueprint, render_template
import db.test

test = Blueprint("test", __name__)


@test.route("/test/search_name_list")
def search_name_list():
    list = db.test.search_name_list()
    return render_template("test.html", list=list)