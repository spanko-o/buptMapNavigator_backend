from flask import request, jsonify
from app.graph import *
from . import main
from app.models import Vex, Edge
from flask import current_app


def build_graph():
    app = current_app
    graph_ = Graph()
    with app.app_context():
        vexes = Vex.query.all()
        for vex in vexes:
            graph_.insert_vex(vex)
        edges = Edge.query.all()
        for edge in edges:
            graph_.insert_edge(edge)
    return graph_


def build_graph_only_roads():
    app = current_app
    graph_ = Graph()
    with app.app_context():
        # 查询所有分类为"路口"的 Vex
        junctions = Vex.query.filter_by(category="路口").all()
        junction_ids = {j.id for j in junctions}  # 创建一个包含所有路口ID的集合

        # 添加顶点到图
        for j in junctions:
            graph_.insert_vex(j)

        # 查询所有两端都是"路口"的边
        edges = Edge.query.filter(Edge.from_vex_id.in_(junction_ids), Edge.to_vex_id.in_(junction_ids)).all()
        for edge in edges:
            graph_.insert_edge(edge)  # 直接添加边到图中

    return graph_


@main.route('/')
def test():
    return None


@main.route('/shortest_path', methods=['POST'])
def get_shortest_path():
    data = request.get_json()
    start_id = data.get('start')
    end_id = data.get('end')
    if not start_id or not end_id:
        return jsonify({'Missing required vexes'}), 400
    graph = build_graph()
    shortest_distance, path = dijkstra(graph, int(start_id), int(end_id))
    return jsonify({
        'shortest_distance': shortest_distance,
        'path': path
    }), 200


@main.route('/hamiltonian_path', methods=['GET'])
def get_hamiltonian_path():
    graph = build_graph_only_roads()
    path = find_hamiltonian_path(graph)
    return jsonify({
        'path': path
    }), 200


@main.route('/vex_prompt', methods=['POST'])
def get_vex_prompt():
    data = request.get_json()
    keyword = data.get('keyword')
    if not keyword:
        return jsonify({'Missing keyword'}), 400
    vexes = Vex.query.all()
    results = []
    for vex in vexes:
        if keyword in vex.name:
            results.append(vex.name)
    return jsonify({
        'vexes': results
    }), 200


@main.route('/vex_info', methods=['POST'])
def get_vex_info():
    data = request.get_json()
    keyword = data.get('keyword')
    if not keyword:
        return jsonify({'Missing keyword'}), 400
    vex = Vex.query.filter_by(name=keyword).first()
    if not vex:
        return jsonify({'This vex does not exist'}), 400
    return jsonify({
        'id': vex.id,
        'name': vex.name,
        'description': vex.desc,
        'longitude': vex.longitude,
        'latitude': vex.latitude,
        'category': vex.category
    }), 200
