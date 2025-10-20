"""

############################
## 키 교환 방식
############################

##################################################
## 비대칭 키 암호화를 이용한 키 교환 방식
##################################################


- Diffie-Hellman(DH) 방식 
	* 통신 당사자들이 공통의 비밀 키를 유도하는 방식 (가장 일반적인 키 교환 방식)
	* TLS 등 실제 보안 통신에서 널리 사용됨
		- 전송 계층 보안(Transport Layer Security) - 인터넷에서 데이터를 안전하게 주고받을 수 있도록 암호화하는 통신 프로토콜

- RSA 방식
	* 한쪽이 생성한 대칭 키를 상대방의 공개 키로 암호화하여 안전하게 전달하는 방식(하이브리드 방식)

##########################################
## Diffie-Hellman 키 교환 파이썬 예제
##########################################

# pip install cryptography


1. 키 교환 코드

"""
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
import os

# ----------------------------------------------------
# 1. 파라미터 생성 (사전 공유)
# ----------------------------------------------------

# DH 키 교환은 두 참여자가 'p' (소수)와 'g' (생성자)라는 공통 파라미터를 사용해야 함

# 실제 환경에서는 표준화된 파라미터 그룹을 사용

parameters = dh.generate_parameters(generator=2, key_size=1024)
# (1024비트 대신 2048비트 이상을 사용해야 안전함, 예제에서는 계산 속도를 위해 1024를 사용)

print("--- Diffie-Hellman 키 교환 시작 ---")
print(f"공통 파라미터 (generator: {parameters.parameter_numbers().g}, key_size: 1024)가 설정됨\n")

# ----------------------------------------------------
# 2. Alice와 Bob이 각각 개인 키/공개 키 생성
# ----------------------------------------------------

# Alice의 키 쌍 생성
alice_private_key = parameters.generate_private_key()
alice_public_key = alice_private_key.public_key()
print("Alice: 개인 키 / 공개 키 쌍 생성 완료")

# Bob의 키 쌍 생성
bob_private_key = parameters.generate_private_key()
bob_public_key = bob_private_key.public_key()
print("Bob: 개인 키 / 공개 키 쌍 생성 완료\n")


# ----------------------------------------------------
# 3. 공개 키 교환 (안전하지 않은 채널을 통해)
# ----------------------------------------------------
print("--- 공개 키 교환 ---")
# Alice는 Bob에게 자신의 공개 키(alice_public_key)를 보냅니다.
# Bob은 Alice에게 자신의 공개 키(bob_public_key)를 보냅니다.
# (도청되어도 안전합니다. 개인 키는 공유되지 않았기 때문입니다.)


# ----------------------------------------------------
# 4. 공통 비밀 키 유도 (Shared Secret Derivation)
# ----------------------------------------------------

# Alice가 Bob의 공개 키를 사용하여 공유 비밀 값 유도
alice_shared_key = alice_private_key.exchange(bob_public_key)
print("Alice: Bob의 공개 키로 공유 비밀 값 유도 완료")

# Bob이 Alice의 공개 키를 사용하여 공유 비밀 값 유도
bob_shared_key = bob_private_key.exchange(alice_public_key)
print("Bob: Alice의 공개 키로 공유 비밀 값 유도 완료\n")


# ----------------------------------------------------
# 5. 최종 대칭 암호화 키 생성 (Key Derivation Function, KDF)
# ----------------------------------------------------
# 공유 비밀 값(shared_key)은 너무 커서 직접 사용하기 어렵고,
# 보안을 위해 HKDF(Hash-based Key Derivation Function)를 사용하여
# AES 암호화에 사용할 최종 대칭 키(32바이트)를 생성

# Alice의 최종 대칭 키
alice_final_key = HKDF(
    algorithm=hashes.SHA256(),
    length=32,
    salt=None,
    info=b'handshake data', # 키 유도에 사용되는 컨텍스트 정보
).derive(alice_shared_key)
print("Alice: 최종 대칭 키 생성 완료 (길이:", len(alice_final_key), "바이트)")

# Bob의 최종 대칭 키
bob_final_key = HKDF(
    algorithm=hashes.SHA256(),
    length=32,
    salt=None,
    info=b'handshake data',
).derive(bob_shared_key)
print("Bob: 최종 대칭 키 생성 완료 (길이:", len(bob_final_key), "바이트)\n")


# ----------------------------------------------------
# 6. 결과 확인
# ----------------------------------------------------
print("--- 최종 확인 ---")
if alice_final_key == bob_final_key:
    print("✅ 성공! Alice와 Bob이 동일한 대칭 비밀 키를 공유합니다.")
    # 이제 이 'final_key'를 사용하여 AES와 같은 대칭 암호화로 통신할 수 있습니다.
    print(f"공유 비밀 키(일부): {alice_final_key[:16].hex()}...")
else:
    print("❌ 오류: 두 키가 일치하지 않습니다.")