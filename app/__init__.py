from flask import Flask
from .models import Base, engine

def create_app():
    app = Flask(__name__)

    from .controllers import init_routes
    init_routes(app)

    Base.metadata.create_all(engine)

    return app