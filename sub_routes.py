from flask import Blueprint, request, jsonify
from sub_model import db, Subscription

sub_api = Blueprint('sub_api', __name__)

@sub_api.route('/subscriptions', methods=['GET'])
def get_subscriptions():
    subscriptions = Subscription.query.all()
    return jsonify([sub.to_dict() for sub in subscriptions])

@sub_api.route('/subscriptions', methods=['POST'])
def add_subscription():
    data = request.json
    new_subscription = Subscription(name=data['name'], cost=data['cost'], duration=data['duration'])
    db.session.add(new_subscription)
    db.session.commit()
    return jsonify(new_subscription.to_dict()), 201

@sub_api.route('/subscriptions/<int:id>', methods=['PUT'])
def update_subscription(id):
    subscription = Subscription.query.get_or_404(id)
    data = request.json
    subscription.name = data['name']
    subscription.cost = data['cost']
    subscription.duration = data['duration']
    db.session.commit()
    return jsonify(subscription.to_dict())

@sub_api.route('/subscriptions/<int:id>', methods=['DELETE'])
def delete_subscription(id):
    subscription = Subscription.query.get_or_404(id)
    db.session.delete(subscription)
    db.session.commit()
    return jsonify({"message": "Deleted Subscription"}), 200