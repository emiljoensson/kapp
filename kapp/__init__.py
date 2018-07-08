from flask import Flask
from flask_restful import Api

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.config['MONGO_URI'] = 'mongodb://user:password@127.0.0.1:27017/database'

    api = Api(app)

    # MongoDB
    from . import database

    # RESTful routes (and resources)
    from . import routes
    routes.init_resources(api)

    # Error handler. This is useful for debugging the live application,
    # however, you should disable the output of the exception for production
    # applications.
    @app.errorhandler(500)
    def server_error(e):
        return """
        An internal error occurred: <pre>{}</pre>
        See logs for full stacktrace.
        """.format(e), 500

    return app
