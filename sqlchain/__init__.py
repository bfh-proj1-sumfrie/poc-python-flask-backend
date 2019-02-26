from flask import Flask, json, make_response
from sqlchain.database import engine
from sqlalchemy import text
import decimal, datetime

application = Flask(__name__)

application.config.from_object(__name__)
application.config.update(dict(
    JSONIFY_PRETTYPRINT_REGULAR=False
))
application.config.from_envvar('FLASK_SERVER_SETTINGS', silent=True)


@application.route('/query/<query>')
def query_controller(query):
    print query
    sql = text(query)
    users = engine.execute(sql)
    data = json.dumps([dict(r) for r in users], default=alchemy_encoder)
    r = make_response(data)
    r.mimetype = 'application/json'
    return r


# JSON encoder function for SQLAlchemy special classes
def alchemy_encoder(obj):
    if isinstance(obj, datetime.date):
        return obj.isoformat()
    elif isinstance(obj, decimal.Decimal):
        return float(obj)
