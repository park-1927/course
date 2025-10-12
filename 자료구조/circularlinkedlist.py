#환형 연결 리스트는 기본적으로 일반 연결 리스트(단일 또는 이중)와 유사하지만, 
#리스트의 마지막 노드가 첫 번째 노드(head)를 가리켜 리스트의 끝과 시작이 순환 고리를 이루는 구조

#환형 연결 리스트의 주요 특징
#순환 구조 : 리스트의 마지막 노드의 next 포인터가 None 대신 첫 번째 노드를 가리킴
# tail 포인터 사용 : 단일 환형 연결 리스트에서는 head 포인터 대신 tail} 포인터만 관리하는 것이 일반적임
#tail을 통해 리스트의 끝(삽입)과 시작(접근) 모두에 O(1)의 시간 복잡도로 접근할 수 있음(단일 연결 리스트에서는 끝에 삽입 시 O(n)이 필요함)
#순회 (Traversal) 주의 : 리스트를 순회할 때, 무한 루프에 빠지지 않도록 head 노드부터 시작하여 
#다시 head 노드로 돌아올 때 멈추는 조건이 필수(while current != head_node: 또는 while True: ... if current == head_node: break)
#용도 : CPU 스케줄링의 라운드 로빈(Round Robin) 방식, 버퍼 관리 등 지속적인 순환이 필요한 곳에 유용하게 사용


##################################
#환형 연결 리스트의 노드 클래스
#데이터와 다음 노드를 가리키는 포인터(next)를 가짐
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
##################################


#환형 연결 리스트 전체를 관리하는 클래스
#마지막 노드(tail)를 가리키는 포인터를 주로 사용하여,
#head에도 쉽게 접근할 수 있도록 함(self.tail.next가 head이기 때문)

class CircularLinkedList:

    def __init__(self):
        # 마지막 노드를 가리키는 포인터. 
        # 리스트가 비어있으면 None임
        self.tail = None 
        
    def is_empty(self): #리스트가 비어있는지 확인
        return self.tail is None

    def insert_at_beginning(self, data): #리스트의 맨 앞에 새로운 노드를 추가(실제로는 tail.next 위치에 삽입)
        new_node = Node(data)
        
        if self.is_empty():
            # 리스트가 비어있으면, 새 노드가 유일한 노드가 됨
            # 자기 자신을 next로 가리키고, tail이 됨
            new_node.next = new_node
            self.tail = new_node
        else:
            # 새 노드의 next가 현재 head(tail.next)를 가리키게 함
            new_node.next = self.tail.next
            # 기존 tail이 새 노드를 다음으로 가리키게 함
            self.tail.next = new_node
            
        print(f"-> {data}를 리스트 맨 앞(tail.next)에 추가했습니다.")


    def insert_at_end(self, data): # 리스트의 맨 끝에 새로운 노드를 추가 (실제로는 tail 뒤에 삽입하고, 새 노드를 새로운 tail로 만듬)
        new_node = Node(data)
        
        if self.is_empty():
            # 리스트가 비어있으면, insert_at_beginning과 동일
            new_node.next = new_node
            self.tail = new_node
        else:
            # 1. 새 노드가 현재 head(tail.next)를 가리키게 함
            new_node.next = self.tail.next
            # 2. 기존 tail이 새 노드를 다음으로 가리키게 함
            self.tail.next = new_node
            # 3. 새 노드를 새로운 tail로 설정함
            self.tail = new_node
            
        print(f"-> {data}를 리스트 맨 끝(새로운 tail)에 추가했습니다.")

    def display(self): # 리스트의 모든 노드를 순서대로 출력(순환하기 전까지)
        if self.is_empty():
            print("환형 연결 리스트가 비어있습니다.")
            return

        print("\n[현재 환형 연결 리스트 구조]:")
        
        # head (tail.next)부터 시작
        head_node = self.tail.next
        current = head_node
        elements = []
        
        # head부터 시작하여 다시 head로 돌아올 때까지 반복
        while True:
            elements.append(str(current.data))
            current = current.next
            
            if current == head_node:
                break
        
        print(" -> ".join(elements) + " -> (HEAD)")
        print(f"(참고: 현재 Tail 데이터: {self.tail.data})")
        print("--------------------------")


##################################
#환형 연결 리스트 사용 예
##################################

# 1. 환형 연결 리스트 객체 생성
my_cll = CircularLinkedList()
my_cll.display() # 비어있는지 확인

# 2. 노드 추가
my_cll.insert_at_end(20) # tail=20
my_cll.insert_at_beginning(10) # head=10, tail=20
my_cll.insert_at_end(30) # head=10, tail=30
my_cll.insert_at_beginning(5) # head=5, tail=30

# 3. 리스트 출력
my_cll.display() 
# 예상 출력: 5 -> 10 -> 20 -> 30 -> (HEAD)

# 4. Tail과 Head 관계 확인 (디버깅 목적)
if not my_cll.is_empty():
    print(f"\n[연결 관계 확인]:")
    # tail.next는 head를 가리켜야 합니다.
    head_data = my_cll.tail.next.data
    print(f"Tail({my_cll.tail.data})의 다음 노드(Next) 데이터: {head_data} (HEAD)")


