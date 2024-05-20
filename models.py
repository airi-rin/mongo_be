from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Label(db.Model):
    label_id = db.Column(db.Integer, primary_key=True)
    label_name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(255))

    def to_dict(self):
        return {
            'labelId': self.label_id,
            'labelName': self.label_name,
            'description': self.description
        }
