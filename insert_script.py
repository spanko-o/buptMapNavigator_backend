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


# 添加数据
# 添加数据
vex_data = [
    {'name': '教一', 'category': '教学楼', 'longitude': 116.35840523256256, 'latitude': 39.96119784480619},
    {'name': '教二', 'category': '教学楼', 'longitude': 116.35809193723807, 'latitude': 39.960490904153794},
    {'name': '教三', 'category': '教学楼', 'longitude': 116.3567692984475, 'latitude': 39.960475447846505},
    {'name': '教四', 'category': '教学楼', 'longitude': 116.3564751101895, 'latitude': 39.96191848662335},
    {'name': '学二', 'category': '宿舍', 'longitude': 116.35668923965758, 'latitude': 39.962485317018285},
    {'name': '学十三', 'category': '宿舍', 'longitude': 116.35522535762183, 'latitude': 39.963971214219754},
    {'name': '瑞幸', 'category': '咖啡厅', 'longitude': 116.35803138097535, 'latitude': 39.96361283073395},
    {'name': '食堂一', 'category': '食堂', 'longitude': 116.35905951553204, 'latitude': 39.963434022680914},
    {'name': '食堂二', 'category': '食堂', 'longitude': 116.35665038188299, 'latitude': 39.96392340071386},
    {'name': '外卖柜', 'category': '其他', 'longitude': 116.35679745678053, 'latitude': 39.96491016630655},
    {'name': '路口一', 'category': '路口', 'longitude': 39.96480343500151, 'latitude': 116.35707744065284},
    {'name': '路口二', 'category': '路口', 'longitude': 39.96378583118574, 'latitude': 116.35716327133665},
    {'name': '路口三', 'category': '路口', 'longitude': 39.96328083857512, 'latitude': 116.35871601504614},
    {'name': '路口四', 'category': '路口', 'longitude': 39.96229222073221, 'latitude': 116.3572119121912},
    {'name': '路口五', 'category': '路口', 'longitude': 39.96167069048346, 'latitude': 116.3572343821102},
    {'name': '路口六', 'category': '路口', 'longitude': 39.96072712381531, 'latitude': 116.35726068637437},
    {'name': '路口七', 'category': '路口', 'longitude': 39.963139980103776, 'latitude': 116.35544246501304},
    {'name': '路口八', 'category': '路口', 'longitude': 39.96233950143029, 'latitude': 116.35870234881023}
]

# 创建边数据
edges_data = [
    {
        'from_vex_name': '外卖柜',
        'to_vex_name': '路口一',
        'weight': 0.5
    },
    {
        'from_vex_name': '学二',
        'to_vex_name': '路口四',
        'weight': 0.4
    },
    {
        'from_vex_name': '学十三',
        'to_vex_name': '路口七',
        'weight': 0.1
    },
    {
        'from_vex_name': '食堂一',
        'to_vex_name': '路口二',
        'weight': 0.3
    },
    {
        'from_vex_name': '食堂二',
        'to_vex_name': '路口三',
        'weight': 0.3
    },
    {
        'from_vex_name': '教一',
        'to_vex_name': '路口四',
        'weight': 0.3
    },
    {
        'from_vex_name': '教四',
        'to_vex_name': '路口五',
        'weight': 0.3
    },
    {
        'from_vex_name': '教三',
        'to_vex_name': '路口二',
        'weight': 0.2
    },
    {
        'from_vex_name': '教二',
        'to_vex_name': '路口二',
        'weight': 0.3
    },
    {
        'from_vex_name': '路口一',
        'to_vex_name': '路口二',
        'weight': 0.7
    },
    {
        'from_vex_name': '路口二',
        'to_vex_name': '路口三',
        'weight': 1.9
    },
    {
        'from_vex_name': '路口二',
        'to_vex_name': '路口四',
        'weight': 2.2
    },
    {
        'from_vex_name': '路口二',
        'to_vex_name': '路口七',
        'weight': 2.0
    },
    {
        'from_vex_name': '路口七',
        'to_vex_name': '路口四',
        'weight': 2.4
    },
    {
        'from_vex_name': '路口三',
        'to_vex_name': '路口四',
        'weight': 2.7
    },
    {
        'from_vex_name': '路口四',
        'to_vex_name': '路口五',
        'weight': 0.7
    },
    {
        'from_vex_name': '路口五',
        'to_vex_name': '路口六',
        'weight': 1.1
    },
    {
        'from_vex_name': '路口五',
        'to_vex_name': '路口八',
        'weight': 1.2
    },
    {
        'from_vex_name': '路口一',
        'to_vex_name': '外卖柜',
        'weight': 0.5
    },
    {
        'from_vex_name': '路口四',
        'to_vex_name': '学二',
        'weight': 0.4
    },
    {
        'from_vex_name': '路口七',
        'to_vex_name': '学十三',
        'weight': 0.1
    },
    {
        'from_vex_name': '路口二',
        'to_vex_name': '食堂一',
        'weight': 0.3
    },
    {
        'from_vex_name': '路口三',
        'to_vex_name': '食堂二',
        'weight': 0.3
    },
    {
        'from_vex_name': '路口四',
        'to_vex_name': '教一',
        'weight': 0.3
    },
    {
        'from_vex_name': '路口五',
        'to_vex_name': '教四',
        'weight': 0.3
    },
    {
        'from_vex_name': '路口二',
        'to_vex_name': '教三',
        'weight': 0.2
    },
    {
        'from_vex_name': '路口二',
        'to_vex_name': '教二',
        'weight': 0.3
    },
    {
        'from_vex_name': '路口二',
        'to_vex_name': '路口一',
        'weight': 0.7
    },
    {
        'from_vex_name': '路口三',
        'to_vex_name': '路口二',
        'weight': 1.9
    },
    {
        'from_vex_name': '路口四',
        'to_vex_name': '路口二',
        'weight': 2.2
    },
    {
        'from_vex_name': '路口七',
        'to_vex_name': '路口二',
        'weight': 2.0
    },
    {
        'from_vex_name': '路口四',
        'to_vex_name': '路口七',
        'weight': 2.4
    },
    {
        'from_vex_name': '路口四',
        'to_vex_name': '路口三',
        'weight': 2.7
    },
    {
        'from_vex_name': '路口五',
        'to_vex_name': '路口四',
        'weight': 0.7
    },
    {
        'from_vex_name': '路口六',
        'to_vex_name': '路口五',
        'weight': 1.1
    },
    {
        'from_vex_name': '路口八',
        'to_vex_name': '路口五',
        'weight': 1.2
    },
    {
        'from_vex_name': '路口六',
        'to_vex_name': '路口八',
        'weight': 2.3
    },
    {
        'from_vex_name': '路口八',
        'to_vex_name': '路口六',
        'weight': 2.3
    },
    {
        'from_vex_name': '路口八',
        'to_vex_name': '路口三',
        'weight': 1.7
    },
    {
        'from_vex_name': '路口三',
        'to_vex_name': '路口八',
        'weight': 1.7
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
