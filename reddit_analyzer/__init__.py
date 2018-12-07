import os

from flask import Flask

def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from reddit_analyzer import analyze
    app.register_blueprint(analyze.bp)
    app.add_url_rule('/', endpoint='index')

    @app.after_request
    def add_header(response):
        response.headers['Pragma'] = 'no-cache'
        response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response.headers['Expires'] = '0'
        return response

    return app