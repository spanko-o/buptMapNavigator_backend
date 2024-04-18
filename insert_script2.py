""" 此页面作为单独的脚本运行"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:twrmax1234@localhost:5432/buptGraphicGuide'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Vex(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)

    edges_starting_here = db.relationship('Edge', backref='from_vex', lazy='dynamic', foreign_keys='Edge.from_vex_id')
    edges_ending_here = db.relationship('Edge', backref='to_vex', lazy='dynamic', foreign_keys='Edge.to_vex_id')


class Edge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    from_vex_id = db.Column(db.Integer, db.ForeignKey('vex.id'), nullable=False)
    to_vex_id = db.Column(db.Integer, db.ForeignKey('vex.id'), nullable=False)
    weight = db.Column(db.Float, nullable=False)


vex_data = [
    {'name': '主楼', 'category': '教学楼', 'longitude': 116.35840523256256, 'latitude': 39.96119784480619},
    {'name': '教二', 'category': '教学楼', 'longitude': 116.35809193723807, 'latitude': 39.960490904153794},
    {'name': '教三', 'category': '教学楼', 'longitude': 116.3567692984475, 'latitude': 39.960475447846505},
    {'name': '教四', 'category': '教学楼', 'longitude': 116.3564751101895, 'latitude': 39.96191848662335},
    {'name': '学二', 'category': '宿舍', 'longitude': 116.35668923965758, 'latitude': 39.962485317018285},
    {'name': '瑞幸', 'category': '咖啡厅', 'longitude': 116.35803138097535, 'latitude': 39.96361283073395},
    {'name': '食堂一', 'category': '食堂', 'longitude': 116.35905951553204, 'latitude': 39.963434022680914},
    {'name': '食堂二', 'category': '食堂', 'longitude': 116.35665038188299, 'latitude': 39.96392340071386},
    {'name': '外卖柜', 'category': '其他', 'longitude': 116.35679745678053, 'latitude': 39.96491016630655},
    {'name': '路口一', 'category': '路口', 'longitude': 116.357316, 'latitude': 39.960427},
    {'name': '路口二', 'category': '路口', 'longitude': 116.357278, 'latitude': 39.961194},
    {'name': '路口三', 'category': '路口', 'longitude': 116.357228, 'latitude': 39.962273},
    {'name': '路口四', 'category': '路口', 'longitude': 116.357173, 'latitude': 39.963754},
    {'name': '路口五', 'category': '路口', 'longitude': 116.358623, 'latitude': 39.963862},
    {'name': '路口六', 'category': '路口', 'longitude': 116.358688, 'latitude': 39.963305},
    {'name': '路口七', 'category': '路口', 'longitude': 116.358778, 'latitude': 39.961195},
    {'name': '路口八', 'category': '路口', 'longitude': 116.358640, 'latitude': 39.960466},
    {'name': '路口九', 'category': '路口', 'longitude': 116.357072, 'latitude': 39.964884},
    {'name': '路口十', 'category': '路口', 'longitude': 116.357179, 'latitude': 39.96327},
    {'name': '路口十一', 'category': '路口', 'longitude': 116.358729, 'latitude': 39.962336},
]

edges_data = [
    {
        'from_vex_name': '路口一',
        'to_vex_name': '教三',
        'weight': 74
    },
    {
        'from_vex_name': '路口一',
        'to_vex_name': '教二',
        'weight': 66
    },
    {
        'from_vex_name': '路口一',
        'to_vex_name': '路口二',
        'weight': 53
    },
    {
        'from_vex_name': '路口三',
        'to_vex_name': '路口二',
        'weight': 113
    },
    {
        'from_vex_name': '路口四',
        'to_vex_name': '路口三',
        'weight': 167
    },
    {
        'from_vex_name': '路口五',
        'to_vex_name': '路口四',
        'weight': 125
    },
    {
        'from_vex_name': '路口六',
        'to_vex_name': '路口五',
        'weight': 171
    },
    {
        'from_vex_name': '路口三',
        'to_vex_name': '路口六',
        'weight': 127
    },
    {
        'from_vex_name': '路口七',
        'to_vex_name': '路口六',
        'weight': 119
    },
    {
        'from_vex_name': '路口八',
        'to_vex_name': '路口七',
        'weight': 83
    },
    {
        'from_vex_name': '路口八',
        'to_vex_name': '教二',
        'weight': 4
    },
    {
        'from_vex_name': '路口二',
        'to_vex_name': '主楼',
        'weight': 95
    },
    {
        'from_vex_name': '路口七',
        'to_vex_name': '主楼',
        'weight': 30
    },
    {
        'from_vex_name': '路口三',
        'to_vex_name': '教四',
        'weight': 80
    },
    {
        'from_vex_name': '路口三',
        'to_vex_name': '学二',
        'weight': 49
    },
    {
        'from_vex_name': '路口四',
        'to_vex_name': '食堂二',
        'weight': 44
    },
    {
        'from_vex_name': '路口九',
        'to_vex_name': '外卖柜',
        'weight': 33
    },
    {
        'from_vex_name': '路口四',
        'to_vex_name': '瑞幸',
        'weight': 87
    },
    {
        'from_vex_name': '路口五',
        'to_vex_name': '瑞幸',
        'weight': 44
    },
    {
        'from_vex_name': '路口五',
        'to_vex_name': '食堂一',
        'weight': 36
    },
    {
        'from_vex_name': '路口六',
        'to_vex_name': '食堂一',
        'weight': 29
    },
    {
        'from_vex_name': '路口四',
        'to_vex_name': '路口九',
        'weight': 119
    },

    {
        'from_vex_name': '教三',
        'to_vex_name': '路口一',
        'weight': 74
    },
    {
        'from_vex_name': '教二',
        'to_vex_name': '路口一',
        'weight': 66
    },
    {
        'from_vex_name': '路口二',
        'to_vex_name': '路口一',
        'weight': 53
    },
    {
        'from_vex_name': '路口二',
        'to_vex_name': '路口三',
        'weight': 113
    },
    {
        'from_vex_name': '路口三',
        'to_vex_name': '路口四',
        'weight': 167
    },
    {
        'from_vex_name': '路口四',
        'to_vex_name': '路口五',
        'weight': 125
    },
    {
        'from_vex_name': '路口五',
        'to_vex_name': '路口六',
        'weight': 171
    },
    {
        'from_vex_name': '路口六',
        'to_vex_name': '路口三',
        'weight': 127
    },
    {
        'from_vex_name': '路口六',
        'to_vex_name': '路口七',
        'weight': 119
    },
    {
        'from_vex_name': '路口七',
        'to_vex_name': '路口八',
        'weight': 83
    },
    {
        'from_vex_name': '教二',
        'to_vex_name': '路口八',
        'weight': 4
    },
    {
        'from_vex_name': '主楼',
        'to_vex_name': '路口二',
        'weight': 95
    },
    {
        'from_vex_name': '主楼',
        'to_vex_name': '路口七',
        'weight': 30
    },
    {
        'from_vex_name': '教四',
        'to_vex_name': '路口三',
        'weight': 80
    },
    {
        'from_vex_name': '学二',
        'to_vex_name': '路口三',
        'weight': 49
    },
    {
        'from_vex_name': '食堂二',
        'to_vex_name': '路口四',
        'weight': 44
    },
    {
        'from_vex_name': '外卖柜',
        'to_vex_name': '路口九',
        'weight': 33
    },
    {
        'from_vex_name': '瑞幸',
        'to_vex_name': '路口四',
        'weight': 87
    },
    {
        'from_vex_name': '瑞幸',
        'to_vex_name': '路口五',
        'weight': 44
    },
    {
        'from_vex_name': '食堂一',
        'to_vex_name': '路口五',
        'weight': 36
    },
    {
        'from_vex_name': '食堂一',
        'to_vex_name': '路口六',
        'weight': 29
    },
    {
        'from_vex_name': '路口九',
        'to_vex_name': '路口四',
        'weight': 119
    },
    {
        'from_vex_name': '路口十',
        'to_vex_name': '路口三',
        'weight': 112
    },
    {
        'from_vex_name': '路口十',
        'to_vex_name': '路口四',
        'weight': 58
    },
    {
        'from_vex_name': '路口十',
        'to_vex_name': '路口六',
        'weight': 129
    },
    {
        'from_vex_name': '路口十一',
        'to_vex_name': '路口六',
        'weight': 108
    },
    {
        'from_vex_name': '路口十一',
        'to_vex_name': '路口七',
        'weight': 117
    },
    {
        'from_vex_name': '路口十一',
        'to_vex_name': '路口三',
        'weight': 127
    },
    {
        'from_vex_name': '路口三',
        'to_vex_name': '路口十',
        'weight': 112
    },
    {
        'from_vex_name': '路口四',
        'to_vex_name': '路口十',
        'weight': 58
    },
    {
        'from_vex_name': '路口六',
        'to_vex_name': '路口十',
        'weight': 129
    },
    {
        'from_vex_name': '路口六',
        'to_vex_name': '路口十一',
        'weight': 108
    },
    {
        'from_vex_name': '路口七',
        'to_vex_name': '路口十一',
        'weight': 117
    },
    {
        'from_vex_name': '路口三',
        'to_vex_name': '路口十一',
        'weight': 127
    }

]

with app.app_context():
    for data in vex_data:
        vex = Vex(name=data['name'], category=data['category'], longitude=data['longitude'], latitude=data['latitude'])
        db.session.add(vex)
    for data in edges_data:
        from_vex = Vex.query.filter_by(name=data['from_vex_name']).first()
        to_vex = Vex.query.filter_by(name=data['to_vex_name']).first()
        if from_vex and to_vex:
            edge = Edge(from_vex=from_vex, to_vex=to_vex, weight=data['weight'])
            db.session.add(edge)

    db.session.commit()
