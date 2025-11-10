"""
####################################
##블록체인에서 트랜잭션 서명 과정
####################################

- 개인 키(Private Key)를 사용하여 트랜잭션 데이터에 대한 디지털 서명을 생성하는 것
   * 이 서명은 트랜잭션의 진위성(Authenticity)과 무결성(Integrity)을 보장하며, 해당 트랜잭션을 승인한 사람이 개인 키 소유자임을 증명함


############################################
##ecdsa 라이브러리를 사용한 트랜잭션 서명 과정
############################################

- 파이썬에서는 일반적으로 ECC(Elliptic Curve Cryptography, 타원 곡선 암호)를 구현한 라이브러리, 특히 ecdsa 또는 cryptography 라이브러리를 사용하여 서명 과정을 구현

# 서명에 필요한 기본 라이브러리 설치
# pip install ecdsa


- 파이썬 서명 코드 예제
   * 키 쌍 생성 : 서명을 위한 개인 키와 검증을 위한 공개 키를 생성
   * 트랜잭션 해시 : 서명할 트랜잭션 데이터의 해시(지문)를 생성
   * 서명 및 검증 : 개인 키로 해시를 서명하고, 공개 키로 서명을 검증
"""

import hashlib
import json
from ecdsa import SigningKey, VerifyingKey, SECP256k1

# 1. 트랜잭션 데이터 정의 (서명할 원본 데이터)
transaction_data = {
    "sender": "Alice",
    "recipient": "Bob",
    "amount": 10.0,
    "fee": 0.001,
    "timestamp": 1678886400.0  # 예시 타임스탬프
}

# 트랜잭션 데이터를 정규화된 JSON 문자열로 변환 (일관된 해시를 위해)
transaction_string = json.dumps(transaction_data, sort_keys=True).encode('utf-8')

# --- 키 생성 및 해시 단계 ---

# (1) 키 쌍 생성 (개인 키와 공개 키)

# SECP256k1은 비트코인 등 많은 블록체인에서 사용하는 타원 곡선
private_key_pem = SigningKey.generate(curve=SECP256k1)
public_key_pem = private_key_pem.verifying_key

# 편의를 위해 키를 16진수 문자열로 변환
PRIVATE_KEY_HEX = private_key_pem.to_string().hex()
PUBLIC_KEY_HEX = public_key_pem.to_string().hex()

print("--- 1단계: 키 쌍 생성 (실제 환경에서는 이미 존재) ---")
print(f"개인 키 (Private Key, 서명 권한): {PRIVATE_KEY_HEX}...")
print(f"공개 키 (Public Key, 검증 권한): {PUBLIC_KEY_HEX}...\n")


# (2) 트랜잭션 해시 생성 (서명할 '지문' 만들기)

# SHA-256을 사용하여 트랜잭션 데이터의 고유한 해시(Digest)를 만듬
transaction_hash = hashlib.sha256(transaction_string).digest()

print("--- 2단계: 트랜잭션 해시 생성 (서명의 대상) ---")
print(f"원본 데이터: {transaction_string.decode('utf-8')}")
print(f"트랜잭션 해시: {transaction_hash.hex()}\n")


# --- 서명 단계 (개인 키 사용) ---
# (3) 개인 키로 해시에 서명

signature = private_key_pem.sign(transaction_hash)

print("--- 3단계: 트랜잭션 서명 (개인 키의 역할) ---")
print(f"생성된 서명 (Signature): {signature.hex()}\n")


# --- 검증 단계 (공개 키 사용) ---

# D. 서명 검증 (다른 노드가 공개 키를 사용)
# 검증을 위해 공개 키 객체를 다시 로드
verifying_key = VerifyingKey.from_string(bytes.fromhex(PUBLIC_KEY_HEX), curve=SECP256k1)

try:
    # 공개 키, 해시, 서명을 사용하여 서명이 유효한지 확인
    is_valid = verifying_key.verify(signature, transaction_hash)
    
    print("--- 4단계: 서명 검증 (네트워크 노드의 역할) ---")
    print(f"검증 결과: {'✅ 서명 유효함' if is_valid else '❌ 서명 무효함'}")
    
    # 참고) 서명 후 트랜잭션 데이터를 조금이라도 변경하면 검증은 실패!!!
    # is_valid_tampered = verifying_key.verify(signature, hashlib.sha256(b"tampered data").digest())
    # print(f"변조된 데이터로 검증 시도: {is_valid_tampered}")

except Exception as e:
    print(f"--- 4단계: 서명 검증 실패 ---")
    print(f"오류: {e}")

