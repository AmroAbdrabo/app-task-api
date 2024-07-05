from flask_sqlalchemy import SQLAlchemy
from config import db

class Contract(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cost = db.Column(db.Float, nullable=False)
    duration = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "cost": self.cost,
            "duration": self.duration
        }