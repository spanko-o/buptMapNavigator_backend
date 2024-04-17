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
                    scc.append(w)
                    if w == v:
                        break
                scc_result.append(scc)

        for v in self.adjacency_list:
            if v not in index_dict:
                strongconnect(v)

        return scc_result


def dijkstra(graph, start, end):
    distance = {vex: float('inf') for vex in graph.adjacency_list}
    distance[start] = 0
    previous = {vex: None for vex in graph.adjacency_list}
    heap = [(0, start)]
    visited = set()

    while heap:
        current_dist, current_vex = heapq.heappop(heap)
        visited.add(current_vex)

        for neighbor, weight in graph.adjacency_list[current_vex]:
            if neighbor not in visited:
                new_dist = current_dist + weight
                if new_dist < distance[neighbor]:
                    distance[neighbor] = new_dist
                    previous[neighbor] = current_vex
                    heapq.heappush(heap, (new_dist, neighbor))

    path = []
    step = end
    if previous[step] is None:
        return float('inf'), []
    while step is not None:
        path.append(step)
        step = previous[step]
    path.reverse()

    return distance[end], path


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
