#!/usr/bin/env python3
'''
    basic Flask app with a single route of /
'''
from datetime import datetime
import pytz
from flask import Flask, g, render_template, request
from flask_babel import Babel, format_datetime
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


@babel.timezoneselector
def get_timezone() -> str:
    '''
        get_timezone: function
        return: the timezone of the request.
    '''
    timezone = request.args.get("timezone")
    if timezone is None:
        user = get_user()
        if user:
            timezone = user.get("timezone")
    try:
        return pytz.timezone(timezone)
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def index_page() -> str:
    '''
        index: function
        return: the main page
    '''
    g.time = format_datetime(datetime.now())
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
