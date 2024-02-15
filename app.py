import flask

from views import steam_views

app = flask.Flask(__name__)


@app.route('/')
def home():
    return flask.render_template('home.html')


if __name__ == '__main__':
    app.register_blueprint(steam_views.steam_blueprint)
    app.run(debug=True)
