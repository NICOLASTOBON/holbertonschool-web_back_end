#!/usr/bin/env python3
""" app main """

from flask import Flask, render_template, request
from flask_babel import Babel, gettext


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ class config """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """get locale """
    return request.accept_languages.best_match(['en', 'fr'])


@app.route('/')
def basic_app():
    """ this is a basic app """
    data = {
        'home_title': gettext(u'home_title'),
        'home_header': gettext(u'home_header')
    }
    return render_template('3-index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
