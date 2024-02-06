#!/usr/bin/env python3
'''
    basic Flask app with a single route of /
'''
from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """docstring for Config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index_page() -> str:
    '''
        index: function
        return: the main page
    '''
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
