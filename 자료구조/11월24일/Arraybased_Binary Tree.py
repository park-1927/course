# 배열 기반 이진 트리 구현

# 완전 이진 트리(Complete Binary Tree)의 경우, 배열(리스트)을 사용하여 노드를 효율적으로 저장할 수 있음

# 노드의 위치(인덱스)를 통해 부모-자식 관계를 수학적으로 계산함
# 인덱스 규칙 (루트 인덱스 0 기준)특정 노드의 인덱스가 i일 때
#      - 왼쪽 자식 : 2 i + 1
#      - 오른쪽 자식 : 2  i + 2
#      - 부모 노드 : (i - 1) / 2 (단, i > 0)

class ArrayBinaryTree:

    def __init__(self, max_size):
        # 배열을 None으로 초기화
        self.tree = [None] * max_size
        self.max_size = max_size
        self.size = 0  # 현재 노드의 개수

    def insert(self, value, index=0):

        """특정 인덱스에 값을 삽입 (완전 이진 트리를 가정하고 레벨 순서로 삽입하는 것은 별도 로직 필요)"""
        if index >= self.max_size:
            print(f"오류: 인덱스 {index}는 배열 크기를 초과합니다.")
            return

        self.tree[index] = value
        if value is not None:
            self.size = max(self.size, index + 1) # 배열 크기 갱신

    def get_root(self):
        return self.tree[0]

    def get_left_child(self, index):
        left_idx = 2 * index + 1
        if left_idx < self.size:
            return self.tree[left_idx]
        return None

    def get_right_child(self, index):
        right_idx = 2 * index + 2
        if right_idx < self.size:
            return self.tree[right_idx]
        return None

# --- 사용 예시 ---
# A(0) -> B(1), C(2)
# B(1) -> D(3), E(4)

tree_size = 7
abt = ArrayBinaryTree(tree_size)

abt.insert("A", 0)
abt.insert("B", 1)
abt.insert("C", 2)
abt.insert("D", 3)
abt.insert("E", 4)

# 인덱스 5는 None으로 비워두고, 인덱스 6에 F 삽입
abt.insert(None, 5) 
abt.insert("F", 6)

print(f"배열 표현: {abt.tree[:abt.size]}") 
print(f"루트 노드: {abt.get_root()}")
print(f"노드 'B'의 왼쪽 자식 (인덱스 3): {abt.get_left_child(1)}")
print(f"노드 'C'의 오른쪽 자식 (인덱스 6): {abt.get_right_child(2)}")
