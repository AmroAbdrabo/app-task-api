"""
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  # Make sure CORS is handled if needed
import os

app = Flask(__name__)
CORS(app)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'subscriptions.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cost = db.Column(db.Float, nullable=False)
    duration = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "cost": self.cost,
            "duration": self.duration
        }

with app.app_context():
    db.create_all()

@app.route('/api/subscriptions', methods=['GET'])
def get_subscriptions():
    subscriptions = Subscription.query.all()
    return jsonify([sub.to_dict() for sub in subscriptions])

@app.route('/api/subscriptions', methods=['POST'])
def add_subscription():
    print("called")
    data = request.json
    new_subscription = Subscription(name=data['name'], cost=data['cost'], duration=data['duration'])
    db.session.add(new_subscription)
    db.session.commit()
    return jsonify(new_subscription.to_dict()), 201

@app.route('/api/subscriptions/<int:id>', methods=['PUT'])
def update_subscription(id):
    subscription = Subscription.query.get_or_404(id)
    data = request.json
    subscription.name = data['name']
    subscription.cost = data['cost']
    subscription.duration = data['duration']
    db.session.commit()
    return jsonify(subscription.to_dict())

@app.route('/api/subscriptions/<int:id>', methods=['DELETE'])
def delete_subscription(id):
    subscription = Subscription.query.get_or_404(id)
    db.session.delete(subscription)
    db.session.commit()
    return jsonify({"message": "Deleted Subscription"}), 200

if __name__ == '__main__':
    app.run(debug=True)

"""