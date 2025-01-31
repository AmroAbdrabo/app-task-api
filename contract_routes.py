from flask import Blueprint, request, jsonify
from contract_model import db, Contract

contract_api = Blueprint('api', __name__)
INIT_QUERIES = False

@contract_api.route('/contracts', methods=['GET'])
def get_contracts():
    contracts = Contract.query.all()
    return jsonify([contract.to_dict() for contract in contracts])

@contract_api.route('/contracts', methods=['POST'])
def add_contract():
    print("called add on")
    data = request.json
    print(data)
    new_contract = Contract(name=data['name'], cost=data['cost'], duration=data['duration'], cycle = data['cycle'])
    db.session.add(new_contract)
    db.session.commit()
    return jsonify(new_contract.to_dict()), 201

@contract_api.route('/contracts/<int:id>', methods=['PUT'])
def update_contract(id):
    print("called put", id)
    contract = Contract.query.get_or_404(id)
    print("contract is", contract)
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