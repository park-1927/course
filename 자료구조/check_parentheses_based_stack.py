def f():
   name = "철수"
   score = 95
   subject = "수학"
   print(f"학생 이름: {name}, {subject} 점수: {score}점입니다.")
   # 출력: 학생 이름: 철수, 수학 점수: 95점입니다.

f()

def check_parentheses(expression):

    # 스택을 사용하여 주어진 문자열의 괄호 짝이 맞는지 검사

    stack = []
    # 괄호 종류와 짝을 정의하는 딕셔너리
    mapping = {")": "(", "}": "{", "]": "["} 
    
    # 닫는 괄호만 모아놓은 집합 (효율적인 검사를 위함)
    closing_parentheses = set(mapping.keys())
    
    for char in expression:
        # 1. 여는 괄호인 경우 (Push)
        # 닫는 괄호의 값(Value)에 현재 문자가 있다면, 즉 여는 괄호라면
        if char in mapping.values():
            stack.append(char)
            
        # 2. 닫는 괄호인 경우 (Pop 및 짝 검사)
        elif char in closing_parentheses:
            # A. 스택이 비어있다면, 짝이 없는 닫는 괄호가 먼저 나왔다는 의미
            if not stack:
                return False 
            
            # B. 스택의 Top 항목을 Pop하고 짝이 맞는지 확인
            top_element = stack.pop()
            
            # 닫는 괄호(char)의 짝(mapping[char])과 꺼낸 괄호(top_element)가 일치하는지 확인
            if mapping[char] != top_element:
                return False
                
    # 3. 모든 문자를 처리한 후, 스택이 비어있어야 모든 괄호가 짝을 이룬 것입니다.
    return not stack 

# --- 테스트 예시 ---
# 여는 괄호( (, {, [ ) --> 문자열을 순서대로 읽다가 여는 괄호를 만나면, 무조건 스택에 Push하여 저장
# 닫는 괄호(  ), }, ] ) --> 닫는 괄호를 만나면, 현재 닫는 괄호의 짝이 될 여는 괄호가 스택의 Top에 있는지 확인
#                                스택이 비어 있다면 (if not stack) : 짝지어줄 여는 괄호가 없으므로 False를 즉시 반환(예: )로 시작하는 경우)
#                                Pop 후 짝 검사 : 스택에서 가장 위에 있는 여는 괄호를 Pop으로 꺼냄,
#                                                        꺼낸 괄호가 현재 닫는 괄호의 정확한 짝(mapping 확인)이 아니라면 False를 반환





# 1. 올바른 괄호
print(f"'{[()]}': {check_parentheses('{[()]}')}") 
# 출력: True

# 2. 닫는 괄호가 먼저 나옴
print(f"'([]}}': {check_parentheses('([]}}')}") 
# 출력: False (A. 닫는 괄호 }가 먼저 나와 스택이 비어있는 상태에서 pop 시도)

# 3. 짝이 맞지 않음
print(f"'([)]': {check_parentheses('([)]')}")
# 출력: False (B. [이 꺼내져야 하는데 (가 나와 짝이 맞지 않음)

# 4. 여는 괄호가 남음 (스택이 비어있지 않음)
print(f"'(([]': {check_parentheses('(([]')}")
# 출력: False (3. 최종적으로 스택에 여는 괄호가 남아있음)
