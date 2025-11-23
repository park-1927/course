요청하신 **깊이 우선 탐색(Depth-First Search, DFS)**을 위한 파이썬 코드를 두 가지 방식으로 구현해 드립니다. DFS는 시작 정점에서 최대한 깊숙이 내려가 탐색하는 알고리즘이며, 일반적으로 스택(Stack) 자료구조 또는 재귀 함수를 사용하여 구현합니다.

🐍 1. 재귀 함수를 이용한 DFS (권장 방식)
재귀는 DFS의 깊이 우선 탐색 개념을 가장 직관적으로 표현하며, 파이썬에서 가장 흔하게 사용되는 방식입니다.

Python

def dfs_recursive(graph, node, visited):
    """
    재귀 함수를 이용한 DFS 구현입니다.
    
    :param graph: 딕셔너리 형태의 인접 리스트
    :param node: 현재 탐색 중인 노드
    :param visited: 방문된 노드를 저장하는 집합 (Set)
    :return: None (탐색 결과를 출력하거나 리스트에 누적하여 반환)
    """
    # 1. 현재 노드를 방문했음으로 표시하고 출력 (또는 리스트에 추가)
    visited.add(node)
    print(node, end=' -> ')

    # 2. 현재 노드의 모든 이웃을 확인
    for neighbor in graph.get(node, []):
        # 3. 이웃이 아직 방문되지 않았다면, 해당 이웃을 시작으로 DFS 재귀 호출
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

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

print("✅ 재귀를 이용한 DFS 탐색 순서:")
start_node = 'A'
visited_set = set()
dfs_recursive(graph_example, start_node, visited_set)
print("끝")
🐍 2. 스택(Stack)을 이용한 DFS (반복문 방식)
재귀 함수 대신 명시적으로 스택 자료구조를 사용하여 DFS를 구현할 수도 있습니다. 이는 재귀 깊이 제한이 있는 환경에서 유용합니다.

Python

def dfs_iterative(graph, start_node):
    """
    반복문과 스택(Stack)을 이용한 DFS 구현입니다.
    
    :param graph: 딕셔너리 형태의 인접 리스트
    :param start_node: 탐색을 시작할 노드
    :return: 탐색된 노드의 순서 리스트
    """
    # 1. 방문 여부를 체크하는 집합(Set) 초기화
    visited = set()
    
    # 2. 탐색을 위한 스택 초기화 (파이썬 리스트를 스택처럼 사용)
    stack = [start_node]
    
    traversal_order = []

    while stack:
        # 스택에서 노드를 하나 꺼냅니다 (LIFO)
        current_node = stack.pop()
        
        # 이미 방문한 노드라면 건너뜁니다.
        if current_node in visited:
            continue
            
        # 3. 현재 노드를 방문했음으로 표시하고 순서에 추가
        visited.add(current_node)
        traversal_order.append(current_node)

        # 4. 현재 노드의 이웃들을 스택에 넣습니다. 
        # (주의: 깊이 우선 탐색 순서를 맞추기 위해 이웃을 역순으로 처리할 수 있습니다.)
        # 여기서는 기본적으로 리스트 순서대로 스택에 넣습니다.
        for neighbor in reversed(graph.get(current_node, [])):
            if neighbor not in visited:
                stack.append(neighbor)
                
    return traversal_order

# --- DFS 실행 ---
print("\n---")
print("✅ 스택을 이용한 DFS 탐색 순서:")
dfs_result = dfs_iterative(graph_example, 'A')
print(" -> ".join(dfs_result), "-> 끝")