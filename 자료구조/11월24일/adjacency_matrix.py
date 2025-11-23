def create_undirected_adjacency_matrix(num_vertices, edges):
    """
    무방향 그래프의 인접 행렬을 생성합니다.
    :param num_vertices: 꼭짓점(노드)의 개수
    :param edges: (u, v) 형태의 간선 리스트
    :return: 인접 행렬 (리스트의 리스트 형태)
    """
    # num_vertices x num_vertices 크기의 0으로 채워진 행렬 초기화
    adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    for u, v in edges:
        # 무방향 그래프이므로 (u, v)와 (v, u) 모두 1로 설정
        # (노드 번호가 0부터 시작한다고 가정)
        adj_matrix[u][v] = 1
        adj_matrix[v][u] = 1

    return adj_matrix

# --- 예시 사용 ---
# 4개의 꼭짓점 (0, 1, 2, 3)
num_v = 4
# 간선 리스트: (0-1), (0-2), (1-2), (2-3)
edge_list = [(0, 1), (0, 2), (1, 2), (2, 3)]

adj_matrix_undirected = create_undirected_adjacency_matrix(num_v, edge_list)

print("✅ 무방향 그래프 인접 행렬:")
for row in adj_matrix_undirected:
    print(row)