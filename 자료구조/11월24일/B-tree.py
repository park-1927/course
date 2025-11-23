# B-트리

# 디스크 접근이 잦은 대규모 데이터베이스나 파일 시스템에서 효율적인 탐색, 삽입, 삭제를 위해 설계된 다차(multi-way) 트리임
# B-트리의 구현은 이진 트리나 AVL 트리에 비해 훨씬 복잡한 노드 분할(Split) 및 노드 병합(Merge) 로직을 포함함


# B-트리의 기본 구조와 핵심 연산인 탐색 및 삽입(노드 분할 포함)을 이해하기 위한 코드

# B-트리 구현 개요 (최소 차수 t=3 기준)
# B-트리는 최소 차수(t, minimum degree)에 의해 그 구조가 결정됨
# 최소 차수 t는 각 노드의 키와 자식의 개수에 영향을 미침
# 노드당 키의 개수 - 최소 t-1개, 최대 2t-1개
# 노드당 자식의 개수 - 최소 t개, 최대 2t개

# 코드에서는 최소 차수 t=3을 가정(노드당 키 : 최소 2개, 최대 5개)


# B-트리 노드 클래스 (BTreeNode)
# B-트리의 각 노드는 키 리스트, 자식 포인터 리스트, 그리고 리프 여부를 가짐

class BTreeNode:
    def __init__(self, t, leaf):
        self.t = t          # B-트리의 최소 차수
        self.leaf = leaf    # 노드가 리프 노드인지 여부 (True/False)
        self.keys = []      # 키(데이터)를 저장하는 리스트 (정렬된 상태)
        self.children = []  # 자식 노드를 저장하는 리스트

# B-트리 클래스 (BTree)
# 트리 전체를 관리하며, 삽입/탐색 연산을 시작하는 클래스

class BTree:
   def __init__(self, t):
        self.t = t  # 최소 차수
        self.root = BTreeNode(t, True)
    
    # --- 탐색 (Search) ---
    
   def search(self, k):
        """트리에서 키 k를 탐색"""
        return self._search_recursive(self.root, k)

   def _search_recursive(self, x, k):
        """재귀적으로 탐색을 수행 (x: 현재 노드, k: 탐색 키)"""
        i = 0
        # 1. 현재 노드에서 k가 들어갈 위치나 k 자체를 찾기 위해 키들을 순회
        while i < len(x.keys) and k > x.keys[i]:
            i += 1
        
        # 2. 키를 찾은 경우
        if i < len(x.keys) and k == x.keys[i]:
            return (x, i) # 노드와 인덱스 반환
        
        # 3. 리프 노드에 도달했지만 키를 못 찾은 경우
        if x.leaf:
            return None
        
        # 4. 자식 노드로 내려가서 탐색을 재귀적으로 계속
        return self._search_recursive(x.children[i], k)
        
    # --- 삽입 (Insertion) ---
    
   def insert(self, k):
        """트리에 키 k를 삽입"""
        root = self.root
        
        # 루트 노드가 가득 찼다면 (키가 2t-1개), 트리가 성장해야 함
        if len(root.keys) == (2 * self.t) - 1:
            new_root = BTreeNode(self.t, False)
            new_root.children.append(root)
            self.root = new_root
            # 가득 찬 루트를 분할하고 새로운 루트에 중간 키를 승격
            self._split_child(new_root, 0, root)

            # 새로운 루트에서 삽입을 시작
            self._insert_non_full(new_root, k)
        else:
            # 루트가 가득 차지 않은 경우 바로 삽입 시작
            self._insert_non_full(root, k)

   def _insert_non_full(self, x, k):
        """노드 x가 가득 차지 않았다고 가정하고 키 k를 삽입합니다."""
        i = len(x.keys) - 1 # 리스트의 끝부터 시작
        
        if x.leaf:
            # 1. 리프 노드인 경우, 키가 들어갈 위치를 찾아 삽입
            x.keys.append(0) # 공간 확보
            while i >= 0 and k < x.keys[i]:
                x.keys[i+1] = x.keys[i]
                i -= 1
            x.keys[i+1] = k
        else:
            # 2. 내부 노드인 경우, 키가 들어갈 자식 노드를 찾음
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            
            # 자식 노드가 가득 찼는지 확인
            if len(x.children[i].keys) == (2 * self.t) - 1:
                # 가득 찼다면 분할 (Split)
                self._split_child(x, i, x.children[i])
                
                # 분할 후 중간 키와 비교하여 삽입할 경로 다시 결정
                if k > x.keys[i]:
                    i += 1
            
            # 분할 후 혹은 가득 차지 않았다면, 해당 자식 노드로 재귀 호출
            self._insert_non_full(x.children[i], k)

   def _split_child(self, x, i, y):
    # 1. 새 노드 z 생성 및 중앙값(median_key) 추출
        z = BTreeNode(self.t, y.leaf)
    
    # *** 🔑 중앙값을 먼저 추출합니다. (y는 2t-1개의 키를 가집니다.) ***
    # 중앙값 인덱스: t - 1
        median_key = y.keys[self.t - 1] 

    # 2. y의 키 절반(오른쪽 t-1개)을 z로 이동
        z.keys = y.keys[self.t:]
    
    # 3. y는 왼쪽 t-1개 키만 남기고 중앙값과 오른쪽 키를 제거
        y.keys = y.keys[:self.t - 1]
    
    # 4. y가 내부 노드라면, 자식 포인터도 절반(오른쪽 t개)을 z로 이동
        if not y.leaf:
            z.children = y.children[self.t:]
            y.children = y.children[:self.t]
        
    # 5. y의 중간 키를 부모 노드 x로 승격 (i번째 위치)
        x.keys.insert(i, median_key)
    
    # 6. 새 노드 z에 대한 포인터를 부모 노드 x에 추가 (i+1 위치)
        x.children.insert(i + 1, z)


# 테스트 및 시각화 (중위 순회)

def print_btree(node, level=0):
    """트리 구조를 시각적으로 출력하는 함수"""
    if node:
        print("  " * level, f"레벨 {level} 키: {node.keys}, 리프: {node.leaf}")
        for child in node.children:
            print_btree(child, level + 1)

            
# --- B-트리 사용 예시 (t=3) ---
t = 3 # 최소 차수 t=3
# 노드당 최대 키 : 5개 (2t-1), 노드당 최소 키 : 2개 (t-1)

btree = BTree(t)
keys = [10, 20, 30, 40, 50, 60, 70, 80, 5, 25, 45, 65]
print("--- 키 삽입 시작 ---")
print()

for k in keys:
    btree.insert(k)
    print(f"키 {k} 삽입 후 트리의 루트 키: {btree.root.keys}")

print()    
print("\n--- 최종 B-트리 구조 (t=3) ---")
print_btree(btree.root)

# --- 탐색 테스트 ---
search_key = 40
result = btree.search(search_key)
print(f"\n키 {search_key} 탐색 결과: {'찾음' if result else '못 찾음'}")

search_key = 99
result = btree.search(search_key)
print(f"키 {search_key} 탐색 결과: {'찾음' if result else '못 찾음'}")