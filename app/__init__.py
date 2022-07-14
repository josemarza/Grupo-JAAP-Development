from flask import Flask


def create_app():
    app = Flask(__name__)
    from app.controller import (main)
    app.register_blueprint(main.bp)
    return app



