# from app.models.gift import Gift
from app.view_models.book import BookViewModel
from . import web
from flask import render_template


# from flask_login import login_required, current_user


@web.route('/')
def index():
    pass


@web.route('/personal')
# @login_required
def personal_center():
    pass
