"""
#########################################################
##########암호화폐 지갑 주소를 생성##########
#########################################################

- 암호화폐 지갑 주소를 생성하는 것은 단순히 무작위 문자열을 만드는 것이 아니라, 
- 개인 키(Private Key)를 생성한 후 특정 암호화 알고리즘(예: ECDSA)과 해싱 과정을 거쳐 
- 공개 키(Public Key)를 도출하고, 이 공개 키에서 최종적으로 지갑 주소(Address)를 생성

#########################################################
#이더리움 (Ethereum) 지갑 주소 생성
#########################################################
- web3.py 라이브러리의 일부인 eth-account 모듈을 사용하여 쉽게 이더리움 계정(개인 키와 주소)을 생성할 수 있음

#먼저 라이브러리 설치 
#pip install eth-account
"""

import secrets
from eth_account import Account

# 1. 강력한 무작위 개인 키 생성
# secrets.token_bytes(32)는 32바이트(256비트)의 무작위 데이터를 생성
private_key_bytes = secrets.token_bytes(32)

# 2. 개인 키에서 계정 객체 생성
# 이더리움 주소는 개인 키를 기반으로 생성
acct = Account.from_key(private_key_bytes)

# 3. 결과 출력
print("--- 이더리움 지갑 정보 ---")
print("개인 키 (Hex):", acct.key.hex())
# 개인 키는 절대 외부에 노출해서는 안 됨  --> 지갑에 접근하는 비밀번호와 같음
print("지갑 주소 (Address):", acct.address)
# 지갑 주소는 이더리움을 주고받기 위해 사용하는 공개 주소
print("=================================================")

########################################################################
### 비트코인 지갑 주소 생성(1)
########################################################################

#먼저 라이브러리 설치 
#pip install ecdsa hashlib base58

import os
import hashlib
import base58
from ecdsa import SECP256k1, SigningKey

# 개인 키 생성
def generate_private_key():
    return os.urandom(32)  # 32 바이트의 랜덤한 개인 키 생성

# 개인 키로 공개 키 생성
def private_key_to_public_key(private_key):
    # ECDSA 서명 키 생성
    sk = SigningKey.from_string(private_key, curve=SECP256k1)
    vk = sk.get_verifying_key()
    
    # 공개 키 (압축되지 않은 형태)
    public_key = b'\x04' + vk.to_string()  # 압축되지 않은 공개 키는 0x04 바이트로 시작
    return public_key

# 공개 키로 비트코인 주소 생성
def public_key_to_bitcoin_address(public_key):
    # SHA256 해시
    sha256_public_key = hashlib.sha256(public_key).digest()

    # RIPEMD160 해시
    ripemd160 = hashlib.new('ripemd160', sha256_public_key).digest()

    # 비트코인 주소 생성
    # 버전 바이트 (0x00은 비트코인 메인넷 주소)
    versioned_payload = b'\x00' + ripemd160

    # 체크섬 계산 (double SHA256 해시)
    checksum = hashlib.sha256(hashlib.sha256(versioned_payload).digest()).digest()[:4]

    # 주소 생성
    address = base58.b58encode(versioned_payload + checksum)
    return address.decode('utf-8')

# 비트코인 주소 생성 과정
def generate_bitcoin_address():
    private_key = generate_private_key()  # 개인 키 생성
    public_key = private_key_to_public_key(private_key)  # 공개 키 생성
    bitcoin_address = public_key_to_bitcoin_address(public_key)  # 비트코인 주소 생성
    
    return private_key.hex(), bitcoin_address

# 비트코인 주소 생성
private_key, bitcoin_address = generate_bitcoin_address()
print(f"Private Key: {private_key}")
print(f"Bitcoin Address: {bitcoin_address}")
print("=================================================")

"""
########################################################################
### 비트코인 지갑 주소 생성 흐름(2)
########################################################################
- 비트코인 지갑 주소를 생성하는 파이썬 코드는 암호화, 해시, Base58 인코딩 등의 과정을 포함
1. 개인 키 생성 (랜덤 256비트 숫자)
2. 공개 키 생성 (개인 키로부터)
3. 공개 키 해시 (SHA-256 → RIPEMD-160)
4. 주소 생성 (Base58Check 인코딩)
"""

import os
import hashlib
import base58
from ecdsa import SigningKey, SECP256k1

#1. 개인 키 생성
private_key = os.urandom(32)
print("Private Key:", private_key.hex())

#2. 공개 키 생성
sk = SigningKey.from_string(private_key, curve=SECP256k1)
vk = sk.verifying_key
public_key = b'\x04' + vk.to_string()
print("Public Key:", public_key.hex())

#3. 공개 키 해시 (SHA-256 → RIPEMD-160)
sha256_pk = hashlib.sha256(public_key).digest()
ripemd160 = hashlib.new('ripemd160')
ripemd160.update(sha256_pk)
hashed_pk = ripemd160.digest()

#4. 주소 생성 (Base58Check 인코딩)
versioned_payload = b'\x00' + hashed_pk  # \x00은 메인넷 주소용
checksum = hashlib.sha256(hashlib.sha256(versioned_payload).digest()).digest()[:4]
full_payload = versioned_payload + checksum
address = base58.b58encode(full_payload)
print("Bitcoin Address:", address.decode())
print("=================================================")