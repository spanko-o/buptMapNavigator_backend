import heapq


class Vex:
    def __init__(self, id, name, desc, longitude, latitude):
        self.id = id
        self.name = name
        self.desc = desc
        self.longitude = longitude
        self.latitude = latitude

    def get_address(self):
        return self.longitude, self.latitude


class Edge:
    def __init__(self, vex1, vex2, weight):
        self.vex1 = vex1
        self.vex2 = vex2
        self.weight = weight


class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.vex_num = 0
        self.vex_list = []

    def insert_vex(self, vex):
        self.adjacency_list[vex.id] = []
        self.vex_list.append(vex)
        self.vex_num += 1

    def insert_edge(self, edge):
        if edge.from_vex.id not in self.adjacency_list:
            self.adjacency_list[edge.from_vex.id] = []
        if edge.to_vex.id not in self.adjacency_list:
            self.adjacency_list[edge.to_vex.id] = []

        self.adjacency_list[edge.from_vex.id].append((edge.to_vex.id, edge.weight))
        self.adjacency_list[edge.to_vex.id].append((edge.from_vex.id, edge.weight))

    def find_vex_by_name(self, name):
        for vex in self.vex_list:
            if vex.name == name:
                return vex.get_address()
        return "景点名称未找到。"

    def tarjan_scc(self):
        index = [0]  # Index sequence number
        stack = []
        lowlink = {}
        index_dict = {}
        on_stack = {v: False for v in self.adjacency_list}
        scc_result = []

        def strongconnect(v):
            index_dict[v] = index[0]
            lowlink[v] = index[0]
            index[0] += 1
            stack.append(v)
            on_stack[v] = True

            for (w, _) in self.adjacency_list[v]:
                if w not in index_dict:
                    strongconnect(w)
                    lowlink[v] = min(lowlink[v], lowlink[w])
                elif on_stack[w]:
                    lowlink[v] = min(lowlink[v], index_dict[w])

            # If v is a root node, pop the stack and generate an SCC
            if lowlink[v] == index_dict[v]:
                scc = []
                while True:
                    w = stack.pop()
                    on_stack[w] = False
                    vex = self.vex_list[w - 1]
                    scc.append(vex.get_address())
                    if w == v:
                        break
                scc_result.append(scc)

        for v in self.adjacency_list:
            if v not in index_dict:
                strongconnect(v)

        return scc_result

    def greedy_vertex_cover(self):
        covered_edges = set()
        vertex_cover = set()
        # 创建边的集合，保证每条边只被统计一次
        edges = set(frozenset({u, v}) for u in self.adjacency_list for v, _ in self.adjacency_list[u] if u < v)

        id_to_vex = {vex.id: vex for vex in self.vex_list}

        while covered_edges != edges:
            max_degree_vertex = None
            max_degree = -1

            # 计算每个顶点的“未覆盖边”度
            for vertex in self.adjacency_list:
                current_degree = len({frozenset({vertex, v}) for v, _ in self.adjacency_list[vertex] if
                                      frozenset({vertex, v}) not in covered_edges})
                if current_degree > max_degree:
                    max_degree = current_degree
                    max_degree_vertex = vertex

            # 如果没有找到合适的顶点，即图中没有更多边需要覆盖
            if max_degree_vertex is None:
                break

            vertex_coords = id_to_vex[max_degree_vertex].get_address()
            vertex_cover.add((vertex_coords['longitude'], vertex_coords['latitude']))
            # 更新已覆盖的边集
            covered_edges.update({frozenset({max_degree_vertex, v}) for v, _ in self.adjacency_list[max_degree_vertex]})

        return vertex_cover


class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, root1, root2):
        root1_root = self.find(root1)
        root2_root = self.find(root2)
        if root1_root != root2_root:
            if self.rank[root1_root] > self.rank[root2_root]:
                self.parent[root2_root] = root1_root
            elif self.rank[root1_root] < self.rank[root2_root]:
                self.parent[root1_root] = root2_root
            else:
                self.parent[root2_root] = root1_root
                self.rank[root1_root] += 1


def kruskal_mst(graph):
    # 创建一个并查集实例
    ds = DisjointSet([v.id for v in graph.vex_list])

    # 初始化最小生成树结果列表
    mst = []
    total_weight = 0

    # 获取所有边，并按权重排序
    edges = []
    for u in graph.adjacency_list:
        for v, weight in graph.adjacency_list[u]:
            if u < v:  # 避免重复添加无向图的边
                edges.append((weight, u, v))
    edges.sort()

    # 遍历排序后的边集，使用并查集确保无环
    for weight, u, v in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            u_coords = graph.vex_list[u - 1].get_address()
            v_coords = graph.vex_list[v - 1].get_address()
            mst.append([
                 u_coords,
                 v_coords
            ])
            total_weight += weight

    return mst, total_weight


def dijkstra(graph, start_id, end_id):
    distance = {vex.id: float('inf') for vex in graph.vex_list}
    distance[start_id] = 0
    previous = {vex.id: None for vex in graph.vex_list}
    heap = [(0, start_id)]
    visited = set()

    while heap:
        current_dist, current_vex_id = heapq.heappop(heap)
        if current_vex_id in visited:
            continue
        visited.add(current_vex_id)

        for neighbor, weight in graph.adjacency_list[current_vex_id]:
            if neighbor in visited:
                continue
            new_dist = current_dist + weight
            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                previous[neighbor] = current_vex_id
                heapq.heappush(heap, (new_dist, neighbor))

    path = []
    step = end_id
    if previous[step] is None:
        return float('inf'), []

    while step is not None:
        vertex = next(v for v in graph.vex_list if v.id == step)
        path.append(vertex.get_address())
        step = previous[step]
    path.reverse()

    return distance[end_id], path


def hamiltonian_path(graph, start, visited, path):
    if len(path) == len(graph.adjacency_list):
        return path
    for neighbor, _ in graph.adjacency_list[start]:
        if not visited[neighbor]:
            visited[neighbor] = True
            path.append(neighbor)
            result_path = hamiltonian_path(graph, neighbor, visited, path)
            if result_path:
                return result_path
            visited[neighbor] = False
            path.pop()
    return None


def find_hamiltonian_path(graph):
    for start_vertex in graph.adjacency_list.keys():
        visited = {vex: False for vex in graph.adjacency_list}
        path = [start_vertex]
        visited[start_vertex] = True
        hamiltonian = hamiltonian_path(graph, start_vertex, visited, path)
        if hamiltonian:
            return hamiltonian
    return None
