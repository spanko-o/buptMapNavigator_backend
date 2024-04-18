from flask import request, jsonify
from app.graph import *
from . import main
from app.models import Vex, Edge
from flask import current_app
import re


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


@main.route('/vexes', methods=['GET'])
def get_all_vexes():
    vexes = Vex.query.all()
    return jsonify([vex.to_dict() for vex in vexes]), 200


@main.route('/shortest_path', methods=['POST'])
def get_shortest_path():
    data = request.get_json()
    start_id = data.get('start')
    end_id = data.get('end')
    if not start_id or not end_id:
        return jsonify('Missing required vexes'), 400
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
        return jsonify('Missing keyword'), 400
    vexes = Vex.query.all()
    results = []
    for vex in vexes:
        if keyword in vex.name or keyword in vex.category:
            result = f"{vex.name}[{vex.category}]"
            results.append(result)
    return jsonify({
        'vexes': results
    }), 200


@main.route('/vex_info', methods=['POST'])
def get_vex_info():
    data = request.get_json()
    keyword = data.get('keyword')
    if not keyword:
        return jsonify('Missing keyword'), 400
    vexes = Vex.query.all()
    legal_vexes = []
    if "[" in keyword:
        parts = re.split(r'[\[\]]+', keyword)
        parts = [part for part in parts if part]
        name_part = parts[0]
        category_part = parts[1]
        matched_vexes = [vex for vex in vexes if vex.name == name_part and vex.category == category_part]
        legal_vexes.extend(matched_vexes)
    else:
        for vex in vexes:
            if keyword in vex.name or keyword in vex.category:
                legal_vexes.append(vex)
    return jsonify([vex.to_dict() for vex in legal_vexes]), 200


@main.route('/scc', methods=['GET'])
def scc():
    graph = build_graph()
    scc_results = graph.tarjan_scc()
    return jsonify({
        'SCC': scc_results
    }), 200


@main.route('/mst', methods=['GET'])
def mst():
    graph = build_graph()
    mst, total_weight = kruskal_mst(graph)
    total_weight = round(total_weight, 1)
    return jsonify({
        "minimum spanning tree": mst
    })


@main.route('/vex_cover', methods=['GET'])
def vex_cover():
    graph = build_graph()
    vertex_cover = graph.greedy_vertex_cover()
    vertex_cover_list = list(vertex_cover)
    converted_vex_cover = [{"longitude": lon, "latitude": lat} for lon, lat in vertex_cover_list]
    return jsonify({
        "vex_cover": converted_vex_cover
    }), 200
