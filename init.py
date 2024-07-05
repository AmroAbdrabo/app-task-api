
from flask import Flask
from .config import Config
from contract_model import db
from sub_routes  import api as api_sub
from contract_routes import api as api_contract

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    
    app.register_blueprint(api, url_prefix='/api')
    
    return app