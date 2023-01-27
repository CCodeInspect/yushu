# from app.models.gift import Gift
from app.view_models.book import BookViewModel
from flask import render_template
from app.web import web


# from flask_login import login_required, current_user


@web.route('/')
def index():
    return "i am index"


@web.route('/personal')
# @login_required
def personal_center():
    pass
