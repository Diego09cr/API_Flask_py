from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Aqui deixamos preparado para MySQL
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:L!and#443@localhost/flask_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .routes import bp
    app.register_blueprint(bp)

    return app
