from flask import Blueprint, request, jsonify
from contract_model import db, Contract

contract_api = Blueprint('api', __name__)

@contract_api.route('/contracts', methods=['GET'])
def get_contracts():
    contracts = Contract.query.all()
    return jsonify([contract.to_dict() for contract in contracts])

@contract_api.route('/contracts', methods=['POST'])
def add_contract():
    print("called add")
    data = request.json
    new_contract = Contract(name=data['name'], cost=data['cost'], duration=data['duration'], cycle = data['cycle'])
    db.session.add(new_contract)
    db.session.commit()
    return jsonify(new_contract.to_dict()), 201

def initialize_contracts():
    # Check if the database is empty
    if not Contract.query.first():
        # Define some sample contracts
        contracts = [
            Contract(id = 1, name="Rent", cost=80, duration=12, cycle=50),
            Contract(id = 2, name="Electricity", cost=60, duration=12, cycle=10),
            Contract(id = 3, name="Water Supply", cost=50, duration=12, cycle=10),
            Contract(id = 4, name="Internet", cost=30, duration=12, cycle=10)
        ]
        # Add them to the session and commit
        db.session.bulk_save_objects(contracts)
        db.session.commit()
        print("Initialized the database with sample contracts.")

# From the react frontend:
"""
    contracts: [
        { id: 1, name: 'Rent', cost: 80, duration: 12, cycle: 50 },
        { id: 2, name: 'Electricity', cost: 60, duration: 12, cycle: 10 },
        { id: 3, name: 'Water Supply', cost: 50, duration: 12, cycle: 10 },
        { id: 4, name: 'Internet', cost: 30, duration: 12, cycle: 10 },
    ],
"""


# before first request 
@contract_api.before_app_first_request
def before_first_request():
    initialize_contracts()

@contract_api.route('/contracts/<int:id>', methods=['PUT'])
def update_contract(id):
    print("called put")
    contract = Contract.query.get_or_404(id)
    data = request.json
    contract.name = data['name']
    contract.cost = data['cost']
    contract.duration = data['duration']
    contract.cycle = data['cycle']
    db.session.commit()
    return jsonify(contract.to_dict())

@contract_api.route('/contracts/<int:id>', methods=['DELETE'])
def delete_contract(id):
    contract = Contract.query.get_or_404(id)
    db.session.delete(contract)
    db.session.commit()
    return jsonify({"message": "Deleted Contract"}), 200