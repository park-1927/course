# UTXO(Unspent Transaction Output) - 비트코인과 같은 암호화폐 시스템에서 아직 사용되지 않은 거래 잔액을 나타냄

# 실제 UTXO를 다루는 파이썬 코드는 주로 기존 라이브러리(예: bitcoin-cli를 이용한 RPC 호출, python-bitcoin-utils, bitcoinlib 등)를 사용하거나, 
# 매우 복잡한 블록체인 노드 구현이 필요함

# UTXO의 개념과 거래 생성 원리를 이해하기 위한 간단한 파이썬 모의(Mock) 코드 예제

# 실제 네트워크 연결 없이, UTXO의 구조와 거래가 UTXO를 소비(Input)하고 새로운 UTXO를 생성(Output)하는 과정을 시뮬레이션


import hashlib
import time

# 1. UTXO 데이터 구조 정의 (간단화)

class UTXO:

    """
        미사용 거래 출력(Unspent Transaction Output)을 나타내는 클래스
        txid와 output_index로 UTXO를 고유하게 식별(TXID:VOUT 구조)
        amount와 recipient_address는 이 UTXO의 잔액과 소유자 주소를 나타냄
    """

    def __init__(self, txid, output_index, amount, recipient_address):
        self.txid = txid               # UTXO를 생성한 이전 거래의 ID
        self.output_index = output_index # 해당 거래의 몇 번째 출력인지
        self.amount = amount           # 잔액 (사토시 단위로 가정)
        self.recipient_address = recipient_address # 이 잔액을 사용할 수 있는 주소

    def __repr__(self):

        # self.txid가 None일 경우 안전하게 빈 문자열 또는 'N/A'를 사용
        txid_display = self.txid[:8] if self.txid else "N/A"
        return f"UTXO(ID: {txid_display}..., Index: {self.output_index}, Amount: {self.amount})"

# 2. 거래(Transaction) 데이터 구조 정의 (간단화)

class Transaction:

    """
          새로운 거래를 나타내는 클래스
          inputs : 이전 거래의 UTXO(미사용 잔액)를 가리킴 (이 UTXO가 이번 거래에서 소비됨)
          outputs : 새롭게 생성되는 UTXO(새로운 잔액)임
    """

    def __init__(self, inputs, outputs):
        self.timestamp = time.time()
        self.inputs = inputs    # 소비할 UTXO 리스트 (거래의 Input)
        self.outputs = outputs  # 새로운 UTXO 리스트 (거래의 Output)
        self.txid = self.calculate_txid()

    def calculate_txid(self):
        # 거래의 내용을 해시하여 ID 생성 (실제 비트코인 로직과는 다름, 단순화)
        tx_data = str(self.inputs) + str(self.outputs) + str(self.timestamp)
        return hashlib.sha256(tx_data.encode('utf-8')).hexdigest()

# 3. UTXO 집합(UTXO Set) 관리 시뮬레이션
# (현재 네트워크에 존재하는 사용 가능한 UTXO의 전체 목록)

    """
        utxo_set 딕셔너리 :현재 블록체인 상에 사용 가능한 모든 UTXO를 저장하는 데이터베이스의 역할을 모방함
        Key는 TXID:Index 형식임
    """

utxo_set = {}

def get_utxo_key(utxo):

    """ UTXO 고유 키 (TXID:Index) 생성 """

    return f"{utxo.txid}:{utxo.output_index}"

def create_utxo(txid, index, amount, address):

    """ 새로운 UTXO를 생성하고 UTXO Set에 추가 """

    new_utxo = UTXO(txid, index, amount, address)
    key = get_utxo_key(new_utxo)
    utxo_set[key] = new_utxo
    return new_utxo

def process_transaction(tx):

    """
         거래를 처리하고 UTXO Set을 업데이트 (핵심 로직)
         입력(Input) 처리 : 거래에 포함된 모든 input_utxo를 utxo_set에서 찾아서 제거(소비 행위)
         잔액 검증 : 소비된 입력의 총액(total_input)이 새로운 출력의 총액(total_output)보다 크거나 같은지 확인
         출력(Output) 생성 : 거래에 포함된 output_utxo를 utxo_set에 새로운 항목으로 추가 (새로운 잔액 생성)
         수수료 : total_input - total_output의 차액은 자동으로 채굴자 수수료가 됨
    """

    total_input = 0
    
    # 1. Input UTXO 소비 및 잔액 확인
    for input_utxo in tx.inputs:
        key = get_utxo_key(input_utxo)
        if key not in utxo_set:
            raise Exception(f"Error: UTXO {key}는 이미 사용되었거나 존재하지 않습니다.")
            
        # UTXO Set에서 소비된 UTXO 제거
        spent_utxo = utxo_set.pop(key)
        total_input += spent_utxo.amount

    # 2. Output UTXO 검증 및 새로운 UTXO 생성
    total_output = sum(output.amount for output in tx.outputs)
    
    # 입력 총액 >= 출력 총액 확인 (차액은 채굴자 수수료)
    if total_input < total_output:
        raise Exception("Error: 입력 총액이 출력 총액보다 적습니다. 잔액이 부족합니다.")

    # 3. 새로운 UTXO를 UTXO Set에 추가
    for i, output_utxo in enumerate(tx.outputs):
        # 새로운 UTXO의 TXID는 현재 거래의 ID가 됨
        create_utxo(tx.txid, i, output_utxo.amount, output_utxo.recipient_address)

    # 4. 거래 수수료 계산
    fee = total_input - total_output
    print(f"💰 거래 처리 성공. 수수료: {fee}")
    print(f"새로운 거래 ID: {tx.txid}")

# --- 실행 예제 ---

# 초기 상태 : 앨리스(Alice)가 1.0 BTC를 가진다고 가정 (단위는 사토시로 100,000,000으로 가정)

ALICE_ADDRESS = "Alice_PubKeyHash"
BOB_ADDRESS = "Bob_PubKeyHash"

# 1. 'Coinbase' 거래를 모방하여 초기 UTXO 생성 (Tx_A)
# TXID는 임의의 값으로 설정

initial_txid = hashlib.sha256(b"Initial_Block").hexdigest()
initial_utxo = create_utxo(initial_txid, 0, 100000000, ALICE_ADDRESS)

print(f"--- 초기 UTXO Set ---")
print()
print(utxo_set)

# 2. 앨리스가 밥에게 0.3 BTC를 보내는 거래 생성 (Tx_B)

# 앨리스의 인풋 (소비할 UTXO)
input_utxo = initial_utxo

# 앨리스의 아웃풋 (새로운 UTXO)
send_amount = 30000000  # 0.3 BTC
fee = 10000             # 0.0001 BTC 수수료
change_amount = initial_utxo.amount - send_amount - fee # 100M - 30M - 0.01M = 69.99M

# Output 1: 밥에게 보내는 금액
output_to_bob = UTXO(None, 0, send_amount, BOB_ADDRESS)

# Output 2: 앨리스에게 돌아오는 잔액 (Change UTXO)
output_to_alice_change = UTXO(None, 1, change_amount, ALICE_ADDRESS)

# 새로운 거래 객체 생성
tx_B = Transaction(
    inputs=[input_utxo],
    outputs=[output_to_bob, output_to_alice_change]
)

print(f"\n--- 거래(Tx_B) 처리 시작 ---")
process_transaction(tx_B)

print(f"\n--- 최종 UTXO Set ---")
print(utxo_set)

# 결과 : initial_utxo는 사라지고, 밥의 UTXO와 앨리스의 잔액 UTXO가 새로 생성됨




