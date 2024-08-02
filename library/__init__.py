from flask import Flask
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.app_context().push()

    from library.auth import auth_bp
    from library.authors import authors_bp
    from library.books import books_bp
    from library.borrows import borrows_bp
    from library.copies import copies_bp

    app.register_blueprint(auth_bp, url_prefix=(
            config_class.URL_PREFIX + '/auth') if config_class.URL_PREFIX else '/api/v1/auth')
    app.register_blueprint(authors_bp, url_prefix=config_class.URL_PREFIX if config_class.URL_PREFIX else '/api/v1')
    app.register_blueprint(books_bp, url_prefix=config_class.URL_PREFIX if config_class.URL_PREFIX else '/api/v1')
    app.register_blueprint(borrows_bp, url_prefix=config_class.URL_PREFIX if config_class.URL_PREFIX else '/api/v1')
    app.register_blueprint(copies_bp, url_prefix=config_class.URL_PREFIX if config_class.URL_PREFIX else '/api/v1')

    return app
