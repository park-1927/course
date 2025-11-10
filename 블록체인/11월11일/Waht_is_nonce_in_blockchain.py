#########################################################################################
##블록체인에서 Nonce(논스)란
## Proof-of-Work(작업증명) 과정에서 특정 조건을 만족하는 해시값을 찾기 위해 반복적으로 변경되는 임의의 숫자
## 이 숫자를 찾는 과정을 채굴(Mining)이라고 함
#########################################################################################

## 파이썬을 사용하여 논스(nonce)를 포함하고, 특정 난이도 조건을 만족하는 해시를 찾는 (간단한) 블록 마이닝의 예시 코드
## Block 클래스를 정의하고, mine_block 메소드를 통해 논스를 찾아 해시가 '0000'으로 시작하는 조건을 만족하게 함(난이도 설정)

import hashlib
import time

# 블록 클래스 정의
class Block:
    def __init__(self, index, timestamp, data, previous_hash=''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0 # Nonce 초기값 설정
        self.hash = self.calculate_hash()

    # 블록의 해시를 계산하는 함수
    def calculate_hash(self):
        # 블록의 모든 정보를 문자열로 합치고 SHA256으로 해시 계산
        block_string = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(block_string.encode()).hexdigest()

    # 작업 증명 (Proof-of-Work)을 통해 논스를 찾는 함수 (마이닝)
    def mine_block(self, difficulty):
        # 난이도 조건: 해시가 '0' * difficulty 로 시작해야 함
        target_prefix = '0' * difficulty
        
        # 해시가 난이도 조건을 만족할 때까지 논스 증가
        while not self.hash.startswith(target_prefix):
            self.nonce += 1
            self.hash = self.calculate_hash()
        
        print(f"블록 채굴 완료! 논스: {self.nonce}, 해시: {self.hash}")

# 블록 생성 및 마이닝 예시

# 난이도 설정 (예: 해시가 4개의 0으로 시작해야 함)
DIFFICULTY = 4

# 첫 번째 블록 (제네시스 블록) 생성 및 마이닝
genesis_block = Block(0, time.time(), "Genesis Block")
print("=== 제네시스 블록 채굴 시작 ===")
genesis_block.mine_block(DIFFICULTY)
print("-" * 30)


# 두 번째 블록 생성 및 마이닝
data_block = Block(1, time.time(), "Transaction Data Example", genesis_block.hash)
print("=== 두 번째 블록 채굴 시작 ===")
data_block.mine_block(DIFFICULTY)
print("-" * 30)

# 결과 출력
print("첫 번째 블록 해시:", genesis_block.hash)
print("두 번째 블록 해시:", data_block.hash)


"""
# 코드 설명
   * Block 클래스
         * __init__ : 블록의 속성(index, timestamp, data, previous_hash, nonce)을 초기화, nonce는 0에서 시작
         * calculate_hash : 블록의 모든 속성(특히 nonce 값)을 문자열로 결합하고 SHA256 해시 함수를 사용하여 해시값을 계산

   * mine_block(difficulty) (핵심)
     * difficulty는 요구되는 난이도(해시가 시작해야 하는 '0'의 개수)를 정의
     * while 루프를 사용하여 생성된 해시가 난이도 조건(target_prefix)을 만족하는지 확인
     * 조건을 만족하지 않으면 self.nonce를 1씩 증가시키고 (self.nonce += 1), 새로운 논스 값을 포함하여 calculate_hash()를 다시 호출하여 새로운 해시를 생성
     * 요구되는 해시 조건을 찾을 때까지 이 과정을 반복 --> 이것이 바로 '작업 증명'의 핵심이며, 블록체인의 보안을 유지하는 방식
"""
