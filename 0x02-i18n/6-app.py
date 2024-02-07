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


def get_user() -> Union[Dict, None]:
    '''
        get_user: function
        @login_as: URL parameter.
        return: Dictionary or None.
    '''
    login_as = request.args.get("login_as")
    if login_as is None:
        return None
    return users.get(int(login_as))


@app.before_request
def before_request() -> None:
    '''
        before_request: function
        return: None
    '''
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    '''
        get_locale: function
        return: The locale of the request.
    '''
    locale = request.args.get("locale")
    if locale is not None and locale in app.config['LANGUAGES']:
        return locale
    user = get_user()
    if user is not None and user.get('locale') in app.config['LANGUAGES']:
        return user.get('locale')
    req_header = request.accept_languages.best_match(app.config['LANGUAGES'])
    if req_header in app.config['LANGUAGES']:
        return req_header
    return app.config['BABEL_DEFAULT_LOCALE']


@app.route('/')
def index_page() -> str:
    '''
        index: function
        return: the main page
    '''
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
