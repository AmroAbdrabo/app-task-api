from flask import Flask
from config import Config
from config import db
from sub_routes  import sub_api
from flask_cors import CORS 
from contract_routes import contract_api

def create_app():
    app = Flask(__name__)
    CORS(app) # needed since database is on port 5000 and the redux request comes from port 3000
    app.config.from_object(Config)

    # Initialize db with the app context
    with app.app_context():
        db.init_app(app)
        db.create_all()  # creates all tables
    
    app.register_blueprint(contract_api, url_prefix='/api')
    app.register_blueprint(sub_api, url_prefix='/api')

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)