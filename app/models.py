from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Vex(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    desc = db.Column(db.Text, nullable=True)
    longitude = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(255), nullable=True)


class Edge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    from_vex_id = db.Column(db.Integer, db.ForeignKey('vex.id'), nullable=False)
    to_vex_id = db.Column(db.Integer, db.ForeignKey('vex.id'), nullable=False)
    weight = db.Column(db.Float, nullable=False)
    from_vex = db.relationship('Vex', foreign_keys=[from_vex_id],
                               backref=db.backref('edges_starting_here', lazy='dynamic'))
    to_vex = db.relationship('Vex', foreign_keys=[to_vex_id], backref=db.backref('edges_ending_here', lazy='dynamic'))
