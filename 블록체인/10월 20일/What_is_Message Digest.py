"""

#######################################################
##메시지 다이제스트(Message Digest, MD)란?
#######################################################

- 데이터의 무결성을 확인하기 위해 사용되는 해시 함수의 출력값

    * 메시지 다이제스트는 임의 길이의 입력 데이터(메시지)를 고정된 길이의 출력값으로 변환
    * 입력 메시지가 조금이라도 바뀌면 다이제스트가 완전히 달라지기 때문에, 데이터가 위변조되지 않았음을 확인하는 데 유용

- 파이썬에서는 기본적으로 제공되는 hashlib 모듈을 사용하여 다양한 해시 알고리즘(MD5, SHA-256 등)을 구현할 수 있음

"""

###########################################################################################################
##SHA-256 다이제스트 생성 예제 (권장) - 가장 널리 사용되며 보안성이 높은 해시 함수인 SHA-256 (Secure Hash Algorithm 256-bit)을 사용
###########################################################################################################

import hashlib

def generate_sha256_digest(message: str) -> str:

    """
    주어진 문자열 메시지에 대한 SHA-256 다이제스트를 생성하고 
    16진수 문자열로 반환
    """

    # 1. hashlib 객체 생성 (SHA-256 사용)
    hasher = hashlib.sha256()

    # 2. 메시지를 바이트(bytes) 형태로 인코딩하여 업데이트
    # 해시 함수는 문자열이 아닌 바이트 데이터를 처리
    hasher.update(message.encode('utf-8'))

    # 3. 다이제스트를 16진수 문자열로 추출하여 반환
    return hasher.hexdigest()

# 예제 사용
message1 = "Hello, world! This is a test message."
digest1 = generate_sha256_digest(message1)

message2 = "Hello, world! This is a test message" # 끝에 마침표만 제거
digest2 = generate_sha256_digest(message2)

print(f"메시지 1: '{message1}'")
print(f"다이제스트 1 (SHA-256): {digest1}")
print("-" * 50)
print(f"메시지 2: '{message2}'")
print(f"다이제스트 2 (SHA-256): {digest2}")
print("-" * 50)

# 중요) 입력의 작은 변화가 다이제스트에 큰 변화를 줌
print(f"다이제스트 일치 여부: {digest1 == digest2}")
print("-" * 50)

###############################################################################
## MD5 다이제스트 생성 예제 (보안상 비권장)
## MD5는 역사적으로 많이 사용되었으나, 현재는 보안 취약점 (충돌 공격 가능성)이 발견되어 
## 데이터 무결성 확인 용도로만 제한적으로 사용되며, 보안이 중요한 목적으로는 권장되지 않음
###############################################################################

import hashlib

def generate_md5_digest(message: str) -> str:

    """
    주어진 문자열 메시지에 대한 MD5 다이제스트를 생성
    (보안이 중요한 상황에서는 SHA-256 이상을 사용!!!)
    """

    hasher = hashlib.md5()
    hasher.update(message.encode('utf-8'))
    return hasher.hexdigest()

message = "This is a simple MD5 test."
md5_digest = generate_md5_digest(message)

print(f"MD5 다이제스트: {md5_digest}")
# MD5는 출력이 128비트(16진수 32자리)로 고정ehla
print("-" * 50)


###########################################################################
## 파일 무결성 확인 예제
## 메시지 다이제스트는 파일이 다운로드 중 손상되지 않았는지 확인하는 데 가장 흔하게 사용됨
###########################################################################

import hashlib
import os

def generate_file_sha256_digest(filepath: str) -> str:

    """
    대용량 파일에 대한 SHA-256 다이제스트를 블록 단위로 생성
    """

    if not os.path.exists(filepath):
        return "파일 없음"
        
    hasher = hashlib.sha256()
    # 파일을 한 번에 읽지 않고 블록 단위로 읽어 메모리 과부하를 방지
    blocksize = 65536 

    with open(filepath, 'rb') as f:
        while True:
            buffer = f.read(blocksize)
            if not buffer:
                break
            hasher.update(buffer)
            
    return hasher.hexdigest()

# 사용 예시 : (실제 경로를 지정해야 함)
file_path = "example_file.txt"
file_digest = generate_file_sha256_digest(file_path)
print(f"'{file_path}'의 다이제스트: {file_digest}")
