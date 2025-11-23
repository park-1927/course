import heapq

# 1. 빈 우선순위 큐 리스트 생성
priority_queue = []

print("--- 요소 추가 (heappush) ---")
# (우선순위, 값) 형태로 추가합니다.
# 숫자가 작을수록 높은 우선순위를 가집니다.
heapq.heappush(priority_queue, (2, 'Task B - 중간 우선순위'))
heapq.heappush(priority_queue, (1, 'Task A - 최고 우선순위'))
heapq.heappush(priority_queue, (3, 'Task C - 낮은 우선순위'))
heapq.heappush(priority_queue, (1, 'Task D - 최고 우선순위 (1순위가 같음)'))

# 현재 큐의 상태 (힙 구조를 유지하며 저장됨)
print(f"현재 큐: {priority_queue}")

print("\n--- 요소 제거 (heappop) ---")
# 우선순위가 가장 높은 요소(가장 작은 숫자)를 제거하고 반환합니다.
while priority_queue:
    priority, task = heapq.heappop(priority_queue)
    print(f"처리된 작업: {task}, 우선순위: {priority}")

print(f"\n최종 큐 상태: {priority_queue}")