from flask_sqlalchemy import SQLAlchemy
from config import db

class Contract(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cost = db.Column(db.Float, nullable=False)
    duration = db.Column(db.Integer, nullable=False) # duration of the contract in months (for subscriptions, this is usually a month)
    cycle = db.Column(db.Integer, nullable=False) # payment cycle in months (for subscriptions, this is usually equal to a month)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "cost": self.cost,
            "duration": self.duration,
            "cycle": self.cycle
        }