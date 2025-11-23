# 힙 트리(Heap Tree)

#  - 완전 이진 트리(Complete Binary Tree)의 한 종류로
#  - 배열(리스트)을 사용하여 구현하는 것이 일반적이며
#  - 힙 속성(Heap Property)을 만족해야 함

#  - 최대 힙 (Max Heap) - 부모 노드의 값이 항상 자식 노드의 값보다 크거나 같음
#                                   (최댓값이 항상 루트에 위치)

#  - 최소 힙 (Min Heap) - 부모 노드의 값이 항상 자식 노드의 값보다 작거나 같음
#                                   (최솟값이 항상 루트에 위치)

# 힙 트리(Heap Tree)의 주된 용도

#   - 우선순위 큐(Priority Queue)를 구현하고 힙 정렬(Heap Sort) 알고리즘을 효율적으로 수행하는 것
#   - 데이터 구조에서 최대값 또는 최소값을 빠르게 찾고 관리하는 데 최적화되어 있기 때문임

# 파이썬에서는 일반적으로 heapq 모듈을 사용하여 최소 힙을 구현
# 직접 클래스를 만들어 최대 힙을 구현할 수도 있음

# heapq 모듈을 사용한 최소 힙 
# 파이썬의 표준 라이브러리인 heapq는 내부적으로 리스트를 사용하여 최소 힙을 구현함


import heapq

# 빈 최소 힙 생성
min_heap = [] 

# 1. 삽입 (heappush)
# O(log N) 복잡도

heapq.heappush(min_heap, 10)
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 7)
heapq.heappush(min_heap, 1)

print(f"삽입 후 최소 힙: {min_heap}") # 최솟값(1)이 리스트의 첫 번째 요소에 위치
print()


# 2. 최솟값 삭제 및 반환 (heappop)
# O(log N) 복잡도

min_value = heapq.heappop(min_heap)
print(f"제거된 최솟값: {min_value}") 
print()

print(f"삭제 후 최소 힙: {min_heap}") 
print()

# 3. 최솟값 확인 (인덱스 0 접근)
# O(1) 복잡도

if min_heap:
    peek_value = min_heap[0]
    print(f"현재 힙의 최솟값 (peek): {peek_value}")
print()

# 사용자 정의 클래스를 사용한 최대 힙 (Max Heap)
# heapq는 최소 힙만 지원하므로, 최대 힙을 구현하려면 사용자 정의 클래스를 만들거나, 
# 값을 삽입/삭제할 때 부호를 반전시키는 트릭을 사용해야 함

# 최대 힙 속성을 유지하는 핵심 연산인 insert와 heaping을 구현한 예시
# 배열(리스트) 인덱스 규칙을 사용
#      - 부모 인덱스 : (i - 1) / 2
#      - 왼쪽 자식 인덱스 : 2 i + 1
#      - 오른쪽 자식 인덱스 : 2 i + 2

# 최대 힙 클래스 구현

class MaxHeap:
    def __init__(self):
        self.heap = []

    def _swap(self, i, j):
        """두 인덱스의 요소를 교환"""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _heapify_up(self, index):
        """새로 삽입된 노드를 부모와 비교하여 위로 올리는(up-heap) 과정"""
        if index == 0:
            return

        parent_index = (index - 1) // 2   # //는 정수 나눗셈(Floor Division) 연산자

        # 자식 노드가 부모보다 크면 교환하고 재귀 호출
        if self.heap[index] > self.heap[parent_index]:
            self._swap(index, parent_index)
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        """루트에서 제거된 후, 새로운 루트를 자식과 비교하여 아래로 내리는(down-heap) 과정"""
        max_index = index
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        
        n = len(self.heap)

        # 왼쪽 자식과 비교
        if left_child_index < n and self.heap[left_child_index] > self.heap[max_index]:
            max_index = left_child_index

        # 오른쪽 자식과 비교
        if right_child_index < n and self.heap[right_child_index] > self.heap[max_index]:
            max_index = right_child_index

        # 부모 노드가 가장 큰 값이 아니면 교환 후 재귀 호출
        if max_index != index:
            self._swap(index, max_index)
            self._heapify_down(max_index)

    def insert(self, item):
        """최대 힙에 요소를 삽입"""
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        """최댓값(루트)을 제거하고 반환"""
        if not self.heap:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()

        # 루트와 마지막 요소를 교환
        self._swap(0, len(self.heap) - 1)
        max_item = self.heap.pop()
        
        # 새로운 루트에 대해 힙 속성을 복원
        self._heapify_down(0)
        
        return max_item

# --- 사용 예시 ---
max_heap = MaxHeap()
max_heap.insert(10)
max_heap.insert(3)
max_heap.insert(7)
max_heap.insert(1)
max_heap.insert(15)

print(f"삽입 후 최대 힙 (내부 리스트): {max_heap.heap}")
print()

max_value = max_heap.extract_max()
print(f"제거된 최댓값: {max_value}")
print()

print(f"삭제 후 최대 힙 (내부 리스트): {max_heap.heap}")