"""arquivo"""
from flask import Flask

APP = Flask(__name__)


@APP.route('/')
def index():
    """funcao index"""
    return 'Index Page'


if __name__ == '__main__':
    APP.run()
