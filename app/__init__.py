from config import Config
from flask import Flask, g

def create_app(config_class=Config):
    
    # Create and configure the app
    app = Flask(__name__)
    app.config.from_object(config_class)

    from app.main import bp as main
    app.register_blueprint(main, url_prefix='/')

    from app.posts import bp as posts
    app.register_blueprint(posts, url_prefix='/posts')

    # Init the DB
    
    from . import db
    db.init_app(app)

    @app.before_request
    def before_request():
        db.get_db()

    @app.after_request
    def after_request(response):
        db.close_db()
        return response

    return app
