#!/usr/bin/env python3
""" app main """
from typing import Text
from flask_babel import Babel, gettext
from flask import Flask, render_template, request


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ class config """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """get locale """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def basic_app() -> Text:
    """ this is a basic app """
    return render_template(
            '3-index.html',
            home_title=gettext(u'home_title'),
            home_header=gettext(u'home_header')
        )


if __name__ == '__main__':
    app.run(debug=True)
