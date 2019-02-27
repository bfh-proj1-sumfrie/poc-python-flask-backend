import datetime
import decimal

from flask import Flask, json, make_response
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from sqlchain.database import engine

def create_app(test_config=None):
    application = Flask(__name__)
    application.config['DEBUG'] = False
    application.config.from_object(__name__)
    application.config.update(dict(
        JSONIFY_PRETTYPRINT_REGULAR=False
    ))
    application.config.from_envvar('FLASK_SERVER_SETTINGS', silent=True)


    @application.route('/query/<query>')
    def query_controller(query):

        #print query
        sql = text(query)
        try:
            users = engine.execute(sql)
        except SQLAlchemyError as err:
            return json.jsonify({"error": str(err)})

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
    return application
