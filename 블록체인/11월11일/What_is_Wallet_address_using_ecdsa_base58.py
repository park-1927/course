"""

####################################################
## 비트코인 지갑 주소를 생성
####################################################

# ecdsa와 base58 라이브러리를 사용하여 개인 키, 공개 키, 그리고 비트코인 주소를 생성

   - os.urandom(32)으로 32바이트 개인 키 생성

   - ecdsa 라이브러리로 공개 키 생성

   - 공개 키를 SHA-256 → RIPEMD-160 해시 처리

   - 네트워크 바이트와 체크섬을 붙여 Base58로 인코딩

# 이 코드는 메인넷 비트코인 주소를 생성하며, 테스트넷 주소는 네트워크 바이트를 0x6f로 바꾸면 됨

"""

# 필요한 라이브러리 설치
# pip install ecdsa base58

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
publickey = b'\x04' + vk.to_string()
print("Public Key:", publickey.hex())
print("")

#3. 공개 키를 해시하여 주소 생성
sha256pk = hashlib.sha256(publickey).digest()
ripemd160 = hashlib.new('ripemd160')
ripemd160.update(sha256pk)
hashed_pk = ripemd160.digest()

#4. 네트워크 바이트 추가 (0x00 for mainnet)
networkbyte = b'\x00' + hashed_pk

#5. 체크섬 추가
checksum = hashlib.sha256(hashlib.sha256(networkbyte).digest()).digest()[:4]
addressbytes = networkbyte + checksum

#6. Base58 인코딩
walletaddress = base58.b58encode(addressbytes)
print("Bitcoin Wallet Address:", walletaddress.decode())


