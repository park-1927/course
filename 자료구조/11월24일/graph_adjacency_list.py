"""
그래프 구조 구현 (인접 리스트 방식)
인접 리스트 방식은 딕셔너리(dict)를 사용하여 구현하는 것이 가장 효율적la
딕셔너리의 키(Key)는 노드(정점)가 되고, 값(Value)은 해당 노드와 연결된 다른 노드들의 리스트가 됨
"""

class Graph:
    """인접 리스트를 사용하는 그래프 클래스"""
    def __init__(self):
        # 그래프를 저장할 딕셔너리: {노드: [연결된 노드 리스트]}
        self.adjacency_list = {}

    def add_node(self, node):
        """그래프에 노드를 추가합니다."""
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []

    def add_edge(self, node1, node2, directed=False):
        """
        두 노드 사이에 간선(edge)을 추가합니다.
        
        :param node1: 간선의 시작 노드
        :param node2: 간선의 끝 노드
        :param directed: 방향성 그래프(True)인지 무방향성 그래프(False)인지 지정
        """
        self.add_node(node1)
        self.add_node(node2)
        
        # node1 -> node2 방향으로 간선 추가
        self.adjacency_list[node1].append(node2)
        
        # 무방향성(undirected) 그래프일 경우, 역방향 간선도 추가
        if not directed:
            self.adjacency_list[node2].append(node1)

################################################
# 그래프 출력 (Display)

    def __str__(self):
        """print() 함수로 객체를 출력할 때 호출됩니다."""
        output = "Graph (Adjacency List):\n"
        for node, neighbors in self.adjacency_list.items():
        # 각 노드와 그 노드에 연결된 이웃 리스트를 출력
            output += f"  {node}: {neighbors}\n"
        return output


######################################
# 그래프 사용 예시 (무방향 그래프)

# 그래프 인스턴스 생성
g = Graph()

# 노드와 간선 추가
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "E")
g.add_edge("D", "E")
g.add_edge("D", "F")
g.add_node("G") # 연결되지 않은 노드 추가

# 그래프 출력
print("--- 무방향 그래프 출력 결과 ---")
print(g)


##############################
#4. 방향 그래프 (Directed Graph) 예시
#add_edge 메서드의 directed 인수를 True로 설정하여 방향 그래프를 만들 수도 있음

# 방향 그래프 인스턴스 생성
dg = Graph()

# 간선 추가 (방향성: True)
dg.add_edge("X", "Y", directed=True)
dg.add_edge("Y", "Z", directed=True)
dg.add_edge("X", "Z", directed=True)

# 그래프 출력
print("--- 방향 그래프 출력 결과 ---")
print(dg)