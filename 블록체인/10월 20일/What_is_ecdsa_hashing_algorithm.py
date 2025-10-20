"""
#########################################################
## ECDSA (Elliptic Curve Digital Signature Algorithm)이란?
#########################################################

 - 타원곡선 암호학(ECC, Elliptic Curve Cryptography)을 기반으로 한 디지털 서명 알고리즘
 
 - 메시지를 안전하게 서명하고, 그 서명이 진짜인지 검증할 수 있는 방법을 제공하는 암호 기술


##########################################################
## ECDSA (타원 곡선 디지털 서명 알고리즘) 
##
## ECDSA는 트랜잭션이 해당 소유자에 의해 서명되었음을 증명하고, 
## 서명 후 트랜잭션 내용이 변경되지 않았음을 보장하는 데 사용
############################################################

# ecdsa 라이브러리를 설치
# pip install ecdsa

"""

import hashlib
import ecdsa
import binascii

# 1. 개인 키 생성 (서명자)
# 일반적으로 안전한 임의의 숫자 (256비트)를 사용
# 여기서는 간단한 예시를 위해 고정된 값을 사용

private_key_hex = "f9a4e76a917e7d4c8c7c94a5a54b42b9e28f73a3648f8c85c0b7d7f7e7e7e7e7" 
private_key_bytes = binascii.unhexlify(private_key_hex)

# Curve: 비트코인 등에서 흔히 사용하는 secp256k1
signing_key = ecdsa.SigningKey.from_string(
    private_key_bytes, 
    curve=ecdsa.SECP256k1
)

# 2. 공개 키 생성 (서명 검증자)
verifying_key = signing_key.get_verifying_key()
public_key_hex = binascii.hexlify(verifying_key.to_string()).decode('utf-8')

print("개인 키 (서명용):", private_key_hex)
print("공개 키 (검증용):", public_key_hex)
print("-" * 50)


# 3. 서명할 데이터 (트랜잭션 메시지)
# "앨리스가 밥에게 10 코인을 보낸다"는 트랜잭션 메시지
message = "Alice pays Bob 10 coins"
message_bytes = message.encode('utf-8')

# 메시지 해시 생성
message_hash = hashlib.sha256(message_bytes).digest()

print(f"서명할 메시지: '{message}'")


# 4. 디지털 서명 생성 (개인 키 사용)
signature = signing_key.sign(message_hash, hashfunc=hashlib.sha256)
signature_hex = binascii.hexlify(signature).decode('utf-8')

print("생성된 서명:", signature_hex)
print("-" * 50)


# 5. 디지털 서명 검증 (공개 키 사용)

# 검증 성공 사례
try:
    verifying_key.verify(signature, message_hash, hashfunc=hashlib.sha256)
    print("✅ 서명 검증 성공: 메시지가 변경되지 않았고, 개인 키 소유자가 서명했습니다.")
except ecdsa.BadSignatureError:
    print("❌ 서명 검증 실패: 서명이 유효하지 않습니다.")


# 검증 실패 사례 (메시지 변조 시도)
tampered_message = "Alice pays Charlie 10 coins"
tampered_message_bytes = tampered_message.encode('utf-8')
tampered_message_hash = hashlib.sha256(tampered_message_bytes).digest()

print(f"\n변조된 메시지: '{tampered_message}'")

try:
    verifying_key.verify(signature, tampered_message_hash, hashfunc=hashlib.sha256)
    print("❌ 서명 검증 성공 (오류 발생!): 변조된 메시지가 원본 서명으로 검증되었습니다. (이 메시지가 보이면 버그)")
except ecdsa.BadSignatureError:
    print("✅ 서명 검증 실패: 메시지가 변조되었거나 서명이 일치하지 않습니다. (정상 작동)")

"""
# ECDSA 요약

 * 서명 과정
	- 원본 메시지(트랜잭션)를 해시
	- 서명자는 자신의 개인 키를 사용하여 이 해시값에 대한 디지털 서명을 생성
 * 검증 과정

	- 검증자는 수신된 메시지를 다시 해시
	- 공개 키와 수신된 서명을 사용하여 해시값이 유효한지 확인
	- 서명이 유효하면
     * 메시지가 서명 후 변경되지 않았음을 보장
     * 서명을 생성한 것이 해당 개인 키의 소유자임을 보장

"""