#!/usr/bin/env python3
'''
    basic Flask app with a single route of /
'''
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index_page() -> str:
    '''
        index: function
        return: the main page
    '''
    return render_template('0-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
