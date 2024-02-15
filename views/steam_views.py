import flask

steam_blueprint = flask.Blueprint('steam',__name__, template_folder='templates')

@steam_blueprint.route('/steam')
def SteamHome():
    return flask.render_template('/steam/SteamHome.html')

