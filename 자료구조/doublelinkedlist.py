#이중 연결 리스트의 개별 요소를 나타내는 노드 클래스
#데이터와 이전 노드(prev), 다음 노드(next) 포인터를 가짐
############################
class Node:

    def __init__(self, data):
        self.data = data  # 노드가 저장할 실제 데이터
        self.prev = None  # 이전 노드를 가리키는 포인터
        self.next = None  # 다음 노드를 가리키는 포인터

############################
#이중 연결 리스트 전체를 관리하는 클래스
# 리스트의 시작점(head)과 끝점(tail)을 가짐
class DoublyLinkedList:

    def __init__(self):
        self.head = None  # 리스트의 시작 노드
        self.tail = None  # 리스트의 끝 노드 (탐색 효율성을 위해 추가)

    def is_empty(self): #리스트가 비어있는지 확인
        return self.head is None

    def insert_at_beginning(self, data): #리스트의 맨 앞에 새로운 노드를 추가
        new_node = Node(data)
        
        if self.is_empty():
            # 리스트가 비어있으면 head와 tail 모두 새 노드를 가리킴
            self.head = new_node
            self.tail = new_node
        else:
            # 새 노드 설정
            new_node.next = self.head  # 새 노드의 next는 기존 head
            
            # 기존 head 설정
            self.head.prev = new_node  # 기존 head의 prev는 새 노드
            
            # head 업데이트
            self.head = new_node        # 새 노드를 새로운 head로 설정
        
        print(f"-> {data}를 리스트 맨 앞에 추가했습니다.")


    def insert_at_end(self, data):  #리스트의 맨 끝에 새로운 노드를 추가합니다. (tail 덕분에 O(1)에 가능)
        new_node = Node(data)
        
        if self.is_empty():
            # 리스트가 비어있으면 head와 tail 모두 새 노드를 가리킴
            self.head = new_node
            self.tail = new_node
        else:
            # 새 노드 설정
            new_node.prev = self.tail  # 새 노드의 prev는 기존 tail
            
            # 기존 tail 설정
            self.tail.next = new_node  # 기존 tail의 next는 새 노드
            
            # tail 업데이트
            self.tail = new_node       # 새 노드를 새로운 tail로 설정
            
        print(f"-> {data}를 리스트 맨 끝에 추가했습니다.")

    def display_forward(self): #리스트에 있는 모든 노드의 데이터를 앞에서부터 순서대로 출력
        if self.is_empty():
            print("이중 연결 리스트가 비어있습니다.")
            return

        print("\n[정방향 리스트 구조]:")
        current = self.head
        elements = []
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        
        print(" <-> ".join(elements))
        print("--------------------------")
        
    def display_backward(self): #리스트에 있는 모든 노드의 데이터를 뒤에서부터 역순으로 출력(tail 덕분에 가능)
        if self.is_empty():
            print("이중 연결 리스트가 비어있습니다.")
            return

        print("\n[역방향 리스트 구조]:")
        current = self.tail
        elements = []
        while current is not None:
            elements.append(str(current.data))
            current = current.prev
        
        print(" <-> ".join(elements))
        print("--------------------------")


################################
#이중 연결 리스트 사용 예시 ---
################################
# 1. 이중 연결 리스트 객체 생성
my_dll = DoublyLinkedList()

# 2. 노드 추가
my_dll.insert_at_beginning(10) # head=10, tail=10
my_dll.insert_at_end(30)       # head=10, tail=30
my_dll.insert_at_beginning(5)  # head=5,  tail=30
my_dll.insert_at_end(40)       # head=5,  tail=40
my_dll.insert_at_beginning(1)  # head=1,  tail=40

# 3. 리스트 출력 (정방향)
my_dll.display_forward() 
# 예상 출력: 1 <-> 5 <-> 10 <-> 30 <-> 40

# 4. 리스트 출력 (역방향)
my_dll.display_backward()
# 예상 출력: 40 <-> 30 <-> 10 <-> 5 <-> 1


