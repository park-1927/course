# 1. 스택 초기화
stack = []
print(f"1. 초기 스택: {stack}")
# 출력: 1. 초기 스택: []

# 2. Push (데이터 삽입)
print("\n2. [Push] 동작: 데이터를 순서대로 쌓습니다.")
stack.append("A") # 첫 번째로 삽입
stack.append("B") # 두 번째로 삽입
stack.append("C") # 세 번째로 삽입 (Top)
print(f"   현재 스택: {stack}") 
# 출력: 현재 스택: ['A', 'B', 'C']

# 3. Peek (가장 위의 항목 확인)
if stack:
    top_item = stack[-1]
    print(f"\n3. [Peek] 동작: 가장 위에 있는 항목: {top_item}")
    print(f"   (Peek 후 스택은 변함 없음): {stack}")
# 출력: 3. [Peek] 동작: 가장 위에 있는 항목: C

# 4. Pop (데이터 삭제 및 반환)
print("\n4. [Pop] 동작: LIFO 원칙에 따라 가장 나중에 들어온 항목이 먼저 나갑니다.")
item1 = stack.pop()
print(f"   Poped (나감): {item1}") # 'C'가 나감
print(f"   현재 스택: {stack}")
# 출력: Poped (나감): C / 현재 스택: ['A', 'B']

item2 = stack.pop()
print(f"   Poped (나감): {item2}") # 'B'가 나감
print(f"   현재 스택: {stack}")
# 출력: Poped (나감): B / 현재 스택: ['A']

# 5. isEmpty (스택 비어있는지 확인)
print(f"\n5. [isEmpty] 동작: 스택이 비었는가? -> {len(stack) == 0}")
# 출력: 5. [isEmpty] 동작: 스택이 비었는가? -> False

# 6. 마지막 항목 Pop
item3 = stack.pop()
print(f"   Poped (나감): {item3}") # 'A'가 나감

# 7. 스택 최종 확인
print(f"   현재 스택: {stack}")
print(f"   스택이 비었는가? -> {len(stack) == 0}")
# 출력: 현재 스택: [] / 스택이 비었는가? -> True