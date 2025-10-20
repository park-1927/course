"""
##################################################
## Hash Collision이란
##################################################

- 서로 다른 두 개의 입력값에 대해 동일한 해시값(메시지 다이제스트)이 생성되는 현상

   * 해시 충돌을 찾는 것은 암호학적 해시 함수의 보안을 깨는 것이기 때문에, 
     보안성이 높은 SHA-256과 같은 함수에서는 충돌 예제를 직접 코드로 만드는 것은 불가능
   * 대신, 보안성이 낮아져 충돌 공격이 쉬워진 알고리즘인 MD5를 사용하여 실제로 발견된 충돌 쌍을 통해 해시 충돌이 무엇인지 실습

- 해시 충돌의 중요성 및 해결책

   1. 충돌이 발생하는 이유
       * 모든 해시 함수는 무한대에 가까운 입력값을 유한한 크기의 출력값(예: MD5는 128비트, SHA-256은 256비트)으로 압축gka
       * 비둘기집 원리(Pigeonhole Principle)에 따라, 기술적으로 해시 충돌은 모든 해시 함수에서 항상 존재함.

   2. 암호학적 해시 함수의 역할
       * 보안이 높은 해시 함수(예: SHA-256, SHA-3)는 고의적으로 충돌 쌍을 찾는 것이 계산적으로 불가능하도록 설계되었음
       * 충돌을 찾는 데 수백만 년이 걸리도록 만들어서 실용적인 보안성을 보장하는 것임

   3. 해결책
       * MD5/SHA-1 사용 중단 - 충돌이 실제로 발견된 MD5나 SHA-1은 보안 목적으로 사용하지 않음
       * SHA-256 이상 사용 - 현재 가장 널리 사용되는 표준은 SHA-256이며, 더 높은 보안이 필요하면 SHA-512 또는 SHA-3 계열을 사용함
       * 솔트(Salt) 사용 - 비밀번호 해시와 같은 민감한 데이터의 경우, 충돌의 위험을 낮추기 위해 해시 함수에 랜덤한 값(솔트)을 추가하여 저장함
"""

##################################################
## MD5 해시 충돌 시연 예제 (파이썬)
## 이 예제는 2004년에 컴퓨터 과학자들에 의해 실제로 발견된, 
## 서로 다른 내용이지만 같은 MD5 해시값을 생성하는 두 개의 PDF 파일 구조를 단순화하여 보여줌
##################################################


import hashlib

# 실제로 충돌이 발견된, 매우 미묘하게 다른 두 개의 바이트 시퀀스를 가정
# 이 바이트 시퀀스는 서로 다른 내용을 가짐에도 불구하고 MD5 충돌을 일으키도록 특별히 조작된 데이터임
# 참고) 이 데이터는 실제 충돌 PDF 파일의 간소화된 버전임

# 첫 번째 메시지 (Message A)
# 이 데이터의 중앙에는 충돌을 일으키는 특정 비트 차이가 인코딩되어 있음
data_a = b'\x0c\x82\x98\x11\xa3\xd2\x15\x4d\x0c\x82\x98\x11\xa3\xd2\x15\x4d\x0c\x82\x98\x11\xa3\xd2\x15\x4d\x0c\x82\x98\x11\xa3\xd2\x15\x4d\x0c\x82\x98\x11\xa3\xd2\x15\x4d\x0c\x82\x98\x11\xa3\xd2\x15\x4d\x0c\x82\x98\x11\xa3\xd2\x15\x4d\x0c\x82\x98\x11\xa3\xd2\x15\x4d\x0c\x82\x98\x11\xa3\xd2\x15\x4d\x0c\x82\x98\x11\xa3\xd2\x15\x4d\x0c\x82\x98\x11\xa3\xd2\x15\x4d\x0c\x82\x98\x11\xa3\xd2\x15\x4d'

# 두 번째 메시지 (Message B)
# Message A와 거의 동일하지만, MD5 충돌을 일으키는 단 하나의 바이트만 다름
#data_b = b'\x0c\x82\x98\x11\xa3\xd2\x15\x4d\x0c\x82\x98\x11\xa3\xd2\x15\x4d\x0c\x82\x98\x11\xa3\xd2\x15\x4d\x0c\x82\x98\x11\xa3\xd2\x15\x4d\x0c\x82\x98\x11\xa3\xd2\x15\x4d\x0c\x82\x98\x11\xa3\xd2\x15\x4d\x0c\x82\x98\x11\xa3\xd2\x15\x4d\x0c\x82\x98\x11\xa3\xd2\x15\x4d\x0c\x82\x98\x11\xa3\xd2\x15\x4d\x0c\x82\x98\x11\xa3\xd2\x15\x4d\x0c\x82\x98\x11\xa3\xd2\x15\x4d\x0c\x82\x98\x11\xa3\xd2\x15\x4c' 

# 마지막 바이트가 x4D 대신 x4C
data_b = b'\x0c\x82\x98\x11\xa3\xd2\x15\x4d\x0c\x82\x98\x11\xa3\xd2\x15\x4d\x0c\x82\x98\x11\xa3\xd2\x15\x4d\x0c\x82\x98\x11\xa3\xd2\x15\x4d\x0c\x82\x98\x11\xa3\xd2\x15\x4d\x0c\x82\x98\x11\xa3\xd2\x15\x4d\x0c\x82\x98\x11\xa3\xd2\x15\x4d\x0c\x82\x98\x11\xa3\xd2\x15\x4d\x0c\x82\x98\x11\xa3\xd2\x15\x4d\x0c\x82\x98\x11\xa3\xd2\x15\x4d\x0c\x82\x98\x11\xa3\xd2\x15\x4d\x0c\x82\x98\x11\xa3\xd2\x15\x4d'


# 1. MD5 해시 생성
hash_a = hashlib.md5(data_a).hexdigest()
hash_b = hashlib.md5(data_b).hexdigest()

print("--- MD5 해시 충돌 시연 ---")
print(f"입력 A의 길이: {len(data_a)} 바이트")
print(f"입력 B의 길이: {len(data_b)} 바이트")
print(f"입력 A와 입력 B의 내용이 같은가? {data_a == data_b}")
print("-" * 35)

print(f"입력 A의 MD5 다이제스트:\n{hash_a}")
print(f"입력 B의 MD5 다이제스트:\n{hash_b}")
print("-" * 35)
print(f"⭐ 다이제스트 일치 여부 (해시 충돌): {hash_a == hash_b} ⭐")

"""

## 시연 결과의 의미
    - 위 코드를 실행하면 입력 A와 입력 B의 내용이 같은가? False로 나오지만, 
    - 다이제스트 일치 여부 - True가 나옴
    - 입력값은 다름 - data_a와 data_b는 마지막 바이트가 달라 서로 다른 데이터
    - 해시값은 같음 - MD5 함수는 이 두 개의 다른 입력에 대해 동일한 해시값을 생성
       * 이것이 바로 해시 충돌  --> 이 충돌을 이용하면, 공격자는 합법적인 문서(A)와 
         동일한 해시값을 가지는 악성 문서(B)를 만들어 A인 척 위장할 수 있음

"""

###############################################################

import hashlib

# 두 개의 서로 다른 메시지 (hex string 형태, 공개된 MD5 충돌 예제)
msg1_hex = (
    "d131dd02c5e6eec4693d9a0698aff95c"
    "2fcab58712467eab4004583eb8fb7f89"
    "55ad340609f4b30283e488832571415a"
    "085125e8f7cdc99fd91dbdf280373c5b"
    "d8823e3156348f5bae6dacd436c919c6"
    "dd53e2b487da03fd02396306d248cda0"
    "e99f33420f577ee8ce54b67080a80d1e"
    "c69821bcb6a8839396f9652b6ff72a70"
)

msg2_hex = (
    "d131dd02c5e6eec4693d9a0698aff95c"
    "2fcab58712467eab4004583eb8fb7f89"
    "55ad340609f4b30283e488832571415a"
    "085125e8f7cdc99fd91dbdf280373c5b"
    "d8823e3156348f5bae6dacd436c919c6"
    "dd53e23487da03fd02396306d248cda0"  # 차이점 존재
    "e99f33420f577ee8ce54b67080a80d1e"
    "c69821bcb6a8839396f9652b6ff72a70"
)

# 바이트로 변환
msg1 = bytes.fromhex(msg1_hex)
msg2 = bytes.fromhex(msg2_hex)

# MD5 해시 계산
hash1 = hashlib.md5(msg1).hexdigest()
hash2 = hashlib.md5(msg2).hexdigest()

print("Message 1 MD5:", hash1)
print("Message 2 MD5:", hash2)
print("Collision:", hash1 == hash2)

