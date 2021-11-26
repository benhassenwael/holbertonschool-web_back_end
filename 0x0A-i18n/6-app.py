#!/usr/bin/env python3
""" I18N
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """ Set Flask config variables
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.before_request
def before_request():
    """Login user
    """
    g.user = get_user(request.args.get('login_as'))


@app.route("/")
def index():
    """ Index route
    """
    return render_template('6-index.html')


@babel.localeselector
def get_locale():
    """ Determine the best match with our supported languages
    """
    supported = app.config['LANGUAGES']

    if request.args.get('locale') in supported:
        return request.args.get('locale')

    if g.user and g.user.get('locale') in supported:
        return g.user.get('locale')

    if request.headers.get('locale') \
       and request.headers.get('locale') in supported:
        return request.headers.get('locale')

    return request.accept_languages.best_match(supported)


def get_user(user_id: int) -> dict:
    """ Get user by id
    """
    if user_id:
        try:
            user_id = int(user_id)
        except ValueError:
            pass

    return users.get(user_id)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
