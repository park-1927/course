##################################################################################################
## 클래스를 사용한 스택 구현 (더 객체지향적인 방식)
## 실제 소프트웨어 개발에서는 메서드 이름을 push, pop, peek 등으로 명시하여 스택의 역할을 더 명확히 하는 클래스 방식을 선호
###################################################################################################


class Stack:
    def __init__(self):
        # 파이썬 리스트를 내부 저장소로 사용
        # self._items : 스택 클래스 내부에서 실제 데이터(항목들)를 저장하는 파이썬 리스트(list) 객체를 참조
        self._items = []

    def is_empty(self):
        """스택이 비어있는지 확인"""

        # 빈 상태일 때 : 리스트에 항목이 없으면 ([]), 이는 거짓(False) 값으로 간주(Falsy Value)
        # 항목이 있을 때 : 리스트에 항목이 하나라도 있으면 ([10, 20]), 이는 참(True) 값으로 간주(Truthy Value)
  
        return not self._items

    def push(self, item):
        """항목을 스택의 Top에 추가"""
        self._items.append(item)

    def pop(self):
        """스택의 Top 항목을 제거하고 반환"""
        if self.is_empty():
            # 빈 스택에서 pop을 시도하면 IndexError 발생
            raise IndexError("Cannot pop from an empty stack")
        return self._items.pop()

    def peek(self):
        """스택의 Top 항목을 확인 (제거하지 않음)"""
        if self.is_empty():
            raise IndexError("Cannot peek at an empty stack")
        return self._items[-1]

# 클래스 사용 예시
my_stack = Stack()
my_stack.push(10)
my_stack.push(20)

print(f"Top 항목 확인 (Peek): {my_stack.peek()}") 
# 출력: Top 항목 확인 (Peek): 20

print(f"첫 번째 Pop: {my_stack.pop()}")
# 출력: 첫 번째 Pop: 20

print(f"두 번째 Pop: {my_stack.pop()}")
# 출력: 두 번째 Pop: 10

print(f"스택이 비었는가?: {my_stack.is_empty()}")
# 출력: 스택이 비었는가?: True