from flask import Flask
from app.models.models import DatabaseManager

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')

    db = DatabaseManager(db_path='database/memories.db')
    db.init_db()

    from app.routers.routers import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app