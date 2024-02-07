#!/usr/bin/env python3
'''
    basic Flask app with a single route of /
'''
from flask import Flask, g, render_template, request
from flask_babel import Babel
from typing import Dict, Union


class Config(object):
    """docstring for Config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(login_as: str) -> Union[Dict, None]:
    '''
        get_user: function
        @login_as: URL parameter.
        return: Dictionary or None.
    '''
    if login_as is None or login_as not in users:
        return None
    return users.get(int(login_as))


@app.before_request
def before_request() -> None:
    '''
        before_request: function
        return: None
    '''
    user = request.args.get("login_as")
    if user is not None:
        g.user = get_user(user)


@babel.localeselector
def get_locale() -> str:
    '''
        get_locale: function
        return: The locale of the request.
    '''
    locale = request.args.get("locale")
    if locale is not None and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index_page() -> str:
    '''
        index: function
        return: the main page
    '''
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
