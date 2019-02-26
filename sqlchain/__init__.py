from flask import Flask, json
from sqlchain.database import db_session
from sqlchain.database import engine
from sqlchain.models import User
from sqlalchemy import text

application = Flask(__name__)

application.config.from_object(__name__)
application.config.update(dict(
    JSONIFY_PRETTYPRINT_REGULAR=False
))
application.config.from_envvar('FLASK_SERVER_SETTINGS', silent=True)


@application.teardown_appcontext
def shutdown_dbsession(exception=None):
    db_session.remove()


@application.route('/query/<query>')
def query_controller(query):
    print query
    sql = text(query)
    users = engine.execute(sql)
    return json.jsonify([to_dict(user) for user in users])


def to_dict(user):
    return {
        'user_id': user.user_id,
        'username': user.username,
        'password': user.password,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'status': user.status,
        'gender': user.gender,
    }