from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config ['SECRET_KEY'] = 'sdvnweiniwRJ2343234'
    app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 1024 * 10  # accept files with size <10Gb
    app.config['UPLOAD_EXTENSIONS'] = ['.sff']                  # accept only .sff files

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
