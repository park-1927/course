"""
################################################
## 트랜잭션 해시(Transaction Hash)
################################################

 - 블록체인에서 트랜잭션 해시(Transaction Hash)는 트랜잭션의 모든 정보(송신자, 수신자, 금액, Nonce 등)를 
    특정 해시 알고리즘을 통해 압축하여 생성된 고유 식별자

 - 이더리움과 같은 EVM(Ethereum Virtual Machine) 기반 블록체인에서는 
   일반적으로 서명된 트랜잭션 데이터(Raw Transaction)의 Keccak-256 해시를 사용하여 트랜잭션 해시를 계산함



#########################################
## web3.py를 사용한 트랜잭션 해시 계산(이더리움)
#########################################
  
 - 트랜잭션을 생성하고 서명한 다음, 서명된 Raw Transaction 데이터로부터 트랜잭션 해시를 추출하는 과정

"""

# pip install web3 설치


from web3 import Web3
from eth_account import Account
from eth_account.signers.local import LocalAccount
from hexbytes import HexBytes

# 1. Web3 인스턴스 초기화 (노드 연결)

# 실제 블록체인에 연결하지 않고 해시 계산만 하려면 HTTPProvider는 필요 없음
# 하지만 실제 트랜잭션 생성에 필요한 Nonce 등을 가져오려면 노드 연결이 필요
# 여기서는 예시를 위해 더미 연결을 사용
# 실제로는 Infura, Alchemy 등의 노드 URL을 사용해야 함
# w3 = Web3(Web3.HTTPProvider("YOUR_NODE_URL")) 


# 2. 송신자 계정 설정 (실제 개인 키를 사용 금지!!!!)

PRIVATE_KEY = "0xc7f9f2252a1727768b427b500350438686f059e71c696e5730a908d1727a81b3"  # 보안상 절대 공개해서는 안 됨
account: LocalAccount = Account.from_key(PRIVATE_KEY)
sender_address = account.address
receiver_address = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e" # 예시 수신자 주소

# 3. 트랜잭션 객체 생성

# Nonce 값은 해당 주소가 보낸 트랜잭션 수(노드에서 가져와야 함)
# 여기서는 예시를 위해 하드코딩

nonce = 5  
gas_limit = 21000 
gas_price = 1000000000 # 1 Gwei (Wei 단위)
value = Web3.to_wei(0.001, 'ether') # 0.001 ETH (Wei 단위로 변환)
chain_id = 1 # 이더리움 메인넷

transaction = {
    'nonce': nonce,
    'gasPrice': gas_price,
    'gas': gas_limit,
    'to': receiver_address,
    'value': value,
    'data': b'', # 일반적인 ETH 전송에는 빈 값
    'chainId': chain_id
}

# 4. 트랜잭션 서명

# 서명되지 않은 트랜잭션은 해시를 계산할 수 없음
# 서명 과정에서 트랜잭션 데이터에 V, R, S 값이 추가됨

signed_transaction = account.sign_transaction(transaction)

# 5. 트랜잭션 해시 추출

# signed_transaction 객체에는 이미 계산된 트랜잭션 해시가 포함되어 있음
# 이는 서명된 Raw Transaction 데이터의 Keccak-256 해시

tx_hash_bytes: HexBytes = signed_transaction.hash
tx_hash_hex: str = tx_hash_bytes.hex()

print(f"송신자 주소: {sender_address}")
print(f"Nonce: {nonce}")
print(f"생성된 트랜잭션 해시: {tx_hash_hex}")


# Raw Transaction (서명된 RLP 인코딩)
# raw_transaction_hex = signed_transaction.rawTransaction.hex()
# print(f"Raw Transaction: {raw_transaction_hex}")

#####################################
## 일반 해시
#####################################

import json
from Crypto.Hash import SHA256

def calculate_simple_hash(transaction_data):

    """
    단순 텍스트 데이터를 직렬화하여 SHA-256 해시를 계산하는 함수.
    (이더리움의 Keccak-256 해시 방식과는 다름)
    """

    # 1. 트랜잭션 데이터를 JSON 문자열로 직렬화
    # 딕셔너리의 키 순서가 해시에 영향을 미치므로, 반드시 정렬

    transaction_string = json.dumps(transaction_data, sort_keys=True)
    
    # 2. 문자열을 바이트로 인코딩
    encoded_transaction = transaction_string.encode('utf-8')
    
    # 3. SHA-256 해시 계산
    h = SHA256.new()
    h.update(encoded_transaction)
    
    # 4. 16진수 문자열로 반환
    return h.hexdigest()

# 예시 트랜잭션 데이터

tx_data = {
    "from": "Address_A",
    "to": "Address_B",
    "amount": 10.5,
    "timestamp": 1700000000,
    "nonce": 1
}

transaction_hash = calculate_simple_hash(tx_data)
print(f"예시 트랜잭션 데이터: {tx_data}")
print(f"계산된 단순 해시 (SHA-256): {transaction_hash}")
