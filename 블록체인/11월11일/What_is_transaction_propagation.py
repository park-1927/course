#########################################
##블록체인 노드들 사이에 트랜잭션을 전파
#########################################

########################################################################################################
## 본질적으로 P2P(Peer-to-Peer) 네트워크 통신과 데이터 직렬화/역직렬화를 필요로 함
## 실제 블록체인 환경은 복잡하지만, 여기서는 핵심 원리인 트랜잭션 객체를 생성하고, 이를 다른 노드에게 브로드캐스트하는 파이썬 예제
## 간단한 HTTP 통신 라이브러리인 requests를 사용하고, 각 노드는 Flask 웹 서버로 가정
#########################################################################################################

# (1) 기본 트랜잭션 및 노드 모델
#      - 트랜잭션과 블록체인 노드를 나타내는 기본 파이썬 클래스


import time
import hashlib
import json
import requests
from urllib.parse import urlparse

class Transaction:
    def __init__(self, sender, recipient, amount):
        # 트랜잭션의 기본 정보
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.timestamp = time.time()
        
    def to_dict(self):
        """트랜잭션 객체를 직렬화 가능한 딕셔너리로 변환"""
        return {
            'sender': self.sender,
            'recipient': self.recipient,
            'amount': self.amount,
            'timestamp': self.timestamp,
        }

class BlockchainNode:
    def __init__(self, node_address):
        # 이 노드의 주소 (예: 'http://127.0.0.1:5000')
        self.address = node_address
        # 이 노드가 알고 있는 다른 노드들의 집합 (중복 방지를 위해 set 사용)
        self.peers = set()
        # 아직 블록에 포함되지 않은 트랜잭션 목록 (MemPool 역할)
        self.pending_transactions = []

    def register_peer(self, address):
        """네트워크에 새로운 노드를 추가"""
        parsed_url = urlparse(address)
        self.peers.add(parsed_url.netloc)
        print(f"새로운 피어 등록: {parsed_url.netloc}")

    def add_transaction(self, tx_data):
        """새 트랜잭션을 pending_transactions에 추가"""
        try:
            # tx_data는 이미 딕셔너리 형태라고 가정
            tx = Transaction(**tx_data)
            self.pending_transactions.append(tx.to_dict())
            return True
        except Exception as e:
            print(f"트랜잭션 추가 오류: {e}")
            return False

# (2) 트랜잭션 전파 (Propagation) 코드
#      - 노드가 새로운 트랜잭션을 수신했을 때, 자신이 알고 있는 모든 피어(peers)에게 이 트랜잭션을 HTTP POST 요청을 통해 전달


# BlockchainNode 클래스에 추가할 메소드

    def broadcast_transaction(self, transaction):
        """
        새로운 트랜잭션을 모든 피어 노드에게 전파(브로드캐스트)
        :param transaction: 전파할 트랜잭션 딕셔너리
        """
        success_count = 0
        
        # 자신이 알고 있는 모든 피어에게 전송
        for peer in self.peers:
            url = f'http://{peer}/transactions/new'
            try:
                # HTTP POST 요청을 통해 트랜잭션 데이터를 전송
                response = requests.post(
                    url, 
                    json=transaction,
                    timeout=5 # 응답을 기다리는 최대 시간
                )
                
                if response.status_code == 200:
                    print(f"✅ {peer}에게 트랜잭션 성공적으로 전파")
                    success_count += 1
                else:
                    print(f"❌ {peer}에게 트랜잭션 전파 실패 (상태 코드: {response.status_code})")
                    
            except requests.exceptions.RequestException as e:
                print(f"⚠️ {peer}와 통신 오류: {e}")
                
        return success_count

# (3) Flask를 사용한 노드 시뮬레이션
#     - 실제 네트워크 통신을 시뮬레이션하기 위해 Flask를 사용하여 노드를 구축
# pip install flask
# flask - 파이썬으로 만든 경량 웹 프레임워크, 웹사이트, API 서버, 간단한 웹 애플리케이션을 빠르고 쉽게 만들 수 있게 도와주는 도구

#Node Server (Node_A.py)

from flask import Flask, request, jsonify
# 위에서 정의한 클래스들 임포트 (실제로는 같은 파일에 있다고 가정)
# from transaction_model import Transaction, BlockchainNode 

# --- 노드 초기화 (예: A 노드, 포트 5000) ---
app = Flask(__name__)
node = BlockchainNode(node_address='127.0.0.1:5000')

# 예시 피어 노드 등록 (실제 환경에서는 동적으로 이루어짐)
# B 노드 (5001), C 노드 (5002)를 알고 있다고 가정
node.register_peer('http://127.0.0.1:5001')
node.register_peer('http://127.0.0.1:5002')


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    """
    1. 외부(다른 노드 또는 사용자)로부터 새로운 트랜잭션을 수신합니다.
    2. 로컬 MemPool에 추가합니다.
    3. 다른 모든 피어에게 이 트랜잭션을 전파합니다.
    """

    tx_data = request.get_json()
    required_fields = ['sender', 'recipient', 'amount']
    
    if not all(field in tx_data for field in required_fields):
        return '필수 필드가 누락되었습니다.', 400

    # 1. 트랜잭션 유효성 검사 및 로컬 MemPool에 추가 (간단화)
    index = node.add_transaction(tx_data)
    
    # 2. 다른 노드들에게 트랜잭션 전파 (재귀적 전파 방지를 위한 플래그는 생략)
    # 실제 시스템에서는 이미 받은 트랜잭션을 다시 전파하지 않도록 처리해야 함 (Bloom Filter 또는 Set 사용)
    success_count = node.broadcast_transaction(tx_data)

    response = {
        'message': '트랜잭션이 추가되고 {}개의 피어에게 전파되었습니다.'.format(success_count),
        'pending_transactions': node.pending_transactions
    }
    return jsonify(response), 200

@app.route('/peers', methods=['GET'])
def get_peers():
    """노드가 알고 있는 피어 목록을 반환"""
    return jsonify(list(node.peers)), 200

# 서버 실행 (다른 포트에서 여러 개를 실행해야 시뮬레이션 가능)
if __name__ == '__main__':
    # Flask 서버를 5000번 포트로 실행
    # Node_B는 5001, Node_C는 5002 등으로 실행하여 테스트 가능
    app.run(host='0.0.0.0', port=5000)

#############################
# 테스트 방법 (터미널에서 실행)
#############################
# Node_A, Node_B, Node_C 실행 : Node_A.py 파일을 복사하여 포트만 다르게(예: 5000, 5001, 5002) 설정하여 세 개의 터미널에서 실행
# 새 트랜잭션 전송 - Node_A(5000)로 새 트랜잭션을 전송하면, Node_A가 이를 받아 Node_B(5001)와 Node_C(5002)에게 전파하는 것을 볼 수 있음

# 터미널에서 Node_A(5000)로 HTTP 요청을 보냄
# Node_A는 이 트랜잭션을 받고, 등록된 피어(5001, 5002)에게 전파함


#curl 같은 명령어를 그대로 파이썬 코드에 붙여넣은 경우
#(-d '{...}' 는 쉘 명령어 형식이라 파이썬에서는 오류 발생)

"""curl -X POST \
  http://127.0.0.1:5000/transactions/new \
  -H 'Content-Type: application/json' \
  -d '{
    "sender": "Alice",
    "recipient": "Bob",
    "amount": 10.5 }'
"""

import requests

url = "http://127.0.0.1:5000/transactions/new"
payload = {
    "sender": "Alice",
    "recipient": "Bob",
    "amount": 10.5 }

res = requests.post(url, json=payload)
print(res.text)



# 이 코드는 실제 블록체인 네트워크의 Gossip Protocol의 핵심 메커니즘을 시뮬레이션함
# 트랜잭션은 하나의 노드에서 시작하여 네트워크 전체로 퍼져나가 채굴자 노드의 멤풀(Mempool)에 들어가게 됨