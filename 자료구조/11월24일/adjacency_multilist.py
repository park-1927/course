def create_adjacency_multilist(num_vertices, edges):
    """
    다중 그래프(Multigraph)의 인접 다중 리스트를 생성합니다.
    
    :param num_vertices: 꼭짓점(노드)의 개수 (0부터 시작한다고 가정)
    :param edges: (u, v) 형태의 간선 리스트. 다중 간선이 포함될 수 있습니다.
    :return: 딕셔너리 형태의 인접 다중 리스트
    """
    # 딕셔너리로 초기화: {노드: 연결된 노드 리스트}
    # 각 노드의 연결 리스트는 중복된 노드를 포함할 수 있음
    adj_multilist = {i: [] for i in range(num_vertices)}

    for u, v in edges:
        # 무방향 그래프를 가정하고 양쪽에 모두 추가
        # (만약 방향 그래프라면 u -> v만 추가)
        
        # u의 리스트에 v 추가 (u에서 v로 가는 간선)
        adj_multilist[u].append(v)
        
        # v의 리스트에 u 추가 (v에서 u로 가는 간선)
        adj_multilist[v].append(u)

    return adj_multilist

# --- 예시 사용 ---
# 5개의 꼭짓점 (0, 1, 2, 3, 4)
num_v = 5

# 간선 리스트 (다중 간선 포함): 
# (0-1) 일반 간선
# (1-2) 일반 간선
# (0-2) 다중 간선 1
# (0-2) 다중 간선 2 -> 노드 0과 2 사이에 총 2개의 간선 존재
# (3-3) 자기 순환 (Self-loop) -> 노드 3과 3 사이에 1개의 간선 존재
edge_list_multigraph = [
    (0, 1), 
    (1, 2), 
    (0, 2), 
    (0, 2), 
    (3, 3) 
]

adj_multilist = create_adjacency_multilist(num_v, edge_list_multigraph)

print("✅ 인접 다중 리스트:")
for node, neighbors in adj_multilist.items():
    print(f"노드 {node}: {neighbors}")