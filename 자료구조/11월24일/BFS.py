from collections import deque

def bfs(graph, start_node):
    """
    너비 우선 탐색(BFS)을 수행하는 함수입니다.
    
    :param graph: 딕셔너리 형태의 인접 리스트 (예: {노드: [이웃 노드 목록]})
    :param start_node: 탐색을 시작할 노드
    :return: 탐색된 노드의 순서 리스트
    """
    # 1. 방문 여부를 체크하는 집합(Set) 초기화
    visited = set()
    
    # 2. 탐색을 위한 큐(Queue) 초기화 (deque 사용)
    queue = deque([start_node])
    
    # 3. 탐색 순서를 저장할 리스트
    traversal_order = []

    # 시작 노드를 방문했음으로 표시
    visited.add(start_node)

    while queue:
        # 큐에서 노드를 하나 꺼냅니다 (FIFO)
        current_node = queue.popleft()
        
        # 탐색 순서에 추가
        traversal_order.append(current_node)

        # 현재 노드와 연결된 모든 이웃 노드를 확인
        for neighbor in graph.get(current_node, []):
            # 이웃 노드가 아직 방문되지 않았다면
            if neighbor not in visited:
                # 방문했음으로 표시하고
                visited.add(neighbor)
                # 큐에 추가하여 나중에 탐색하도록 예약
                queue.append(neighbor)
                
    return traversal_order

# --- 예시 그래프 정의 (인접 리스트) ---
# 노드 A, B, C, D, E, F, G를 가진 무방향 그래프
graph_example = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'G'],
    'F': ['C'],
    'G': ['E']
}

# --- BFS 실행 ---
start = 'A'
bfs_result = bfs(graph_example, start)

print(f"🔍 시작 노드: {start}")
print(f"➡️ BFS 탐색 순서: {bfs_result}")