from flask import Flask
from config import Config
from config import db
from contract_model import Contract

# from sub_routes  import sub_api
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

        # Delete existing data
        db.session.query(Contract).delete()
        
        # Initialize database
        contracts = [
            Contract(id = 1, name="Rent", cost=80, duration=12, cycle=50),
            Contract(id = 2, name="Electricity", cost=60, duration=12, cycle=10),
            Contract(id = 3, name="Water Supply", cost=50, duration=12, cycle=10),
            Contract(id = 4, name="Internet", cost=30, duration=12, cycle=10)
        ]
        # Add them to the session and commit
        db.session.bulk_save_objects(contracts)
        db.session.commit()

    app.register_blueprint(contract_api, url_prefix='/api')
    # app.register_blueprint(sub_api, url_prefix='/api')

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)