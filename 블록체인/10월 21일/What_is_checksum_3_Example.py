"""
###########################################
#### 체크섬(Checksum)
###########################################

- 데이터의 무결성(Integrity)을 확인하기 위한 간단한 오류 검출 방법
- 전송 과정이나 저장 과정에서 데이터가 손상되었는지 여부를 확인하는 데 사용


########################################################################
## 파이썬에서 체크섬을 계산하는 가장 일반적이고 권장되는 방법은 내장된 hashlib 모듈을 사용
## 이 모듈은 MD5, SHA-1, SHA-256 등 다양한 암호화 해시 함수를 제공
## 이 해시값(Hash Value)을 데이터의 체크섬으로 사용할 수 있음
#######################################################################

##############################################################################################
## 예제 1) - 문자열에 대한 체크섬 (SHA-256 예제)
## hashlib를 사용하여 문자열의 SHA-256 해시를 계산 - SHA-256은 보안성이 높아 가장 널리 사용되는 체크섬 방법 중 하나
##############################################################################################
"""

import hashlib

# 1. 체크섬을 계산할 문자열

data = "안녕하세요, 체크섬을 계산해봅시다."

# 2. 문자열을 바이트 객체로 변환 (해시 함수는 바이트 데이터를 입력받음)

data_bytes = data.encode('utf-8')

# 3. SHA-256 해시 객체 생성

sha256_hash = hashlib.sha256()

# 4. 바이트 데이터를 해시 객체에 업데이트

sha256_hash.update(data_bytes)

# 5. 해시값(체크섬)을 16진수 문자열로 추출

checksum = sha256_hash.hexdigest()

print(f"원본 데이터: {data}")
print(f"SHA-256 체크섬: {checksum}")
print("")


###########################################################################
## 예제 2) - 파일에 대한 체크섬 (MD5 예제)
## 파일 체크섬은 파일이 전송 중 손상되거나 변조되었는지 확인하는 데 매우 중요
## 대용량 파일을 효율적으로 처리하기 위해 파일을 작은 청크(Chunk)로 나누어 읽는 것이 일반적임
###########################################################################

import hashlib

def get_md5_from_string(input_string):

  """
  주어진 문자열의 MD5 해시 값을 계산하는 함수

  Args:
    input_string: MD5 값을 계산할 문자열임

  Returns:

    계산된 32자리 16진수 MD5 해시 값입니다.

  """

  # MD5 객체를 생성
  hash_md5 = hashlib.md5()

  # 문자열을 바이트 형태로 인코딩하여 MD5 객체에 업데이트
  # UTF-8 인코딩을 사용하는 것이 일반적임
  hash_md5.update(input_string.encode('utf-8'))

  # 16진수 형태의 MD5 해시 값을 반환
  return hash_md5.hexdigest()


def calculate_file_checksum(filepath, hash_algorithm="md5"):

    """
    지정된 파일의 체크섬을 계산
    :param filepath: 파일 경로
    :param hash_algorithm: 사용할 해시 알고리즘 (예: 'md5', 'sha256')
    :return: 16진수 체크섬 문자열
    """
    
    # 1. 선택한 알고리즘에 맞는 해시 객체 생성
    if hash_algorithm == "md5":
        hasher = hashlib.md5()
    elif hash_algorithm == "sha256":
        hasher = hashlib.sha256()
    else:
        raise ValueError("지원하지 않는 해시 알고리즘입니다.")

    try:
        # 2. 파일을 '바이너리 읽기' 모드('rb')로 열기
        with open(filepath, 'rb') as file:
            # 3. 파일을 청크 단위로 읽으며 해시 업데이트
            # 대용량 파일의 메모리 사용을 줄이는 효율적인 방법
            chunk_size = 65536  # 64KB
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                hasher.update(chunk)
                
        # 4. 최종 해시값(체크섬)을 반환
        return hasher.hexdigest()
        
    except FileNotFoundError:
        return f"오류: 파일을 찾을 수 없습니다. ({filepath})"


# 사용 예시:
my_string = "이것은 체크섬을 테스트하기 위한 예제 파일의 내용입니다."
md5_hash = get_md5_from_string(my_string)
print(f"입력 문자열: {my_string}")
print(f"MD5 해시 값: {md5_hash}")

file_path = "example_file.txt"  # 실제 파일 경로로 대체!!!!

# 1) 예제 파일 생성 (실제 테스트를 위해)

try:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write("이것은 체크섬을 테스트하기 위한 예제 파일의 내용입니다.")
except IOError:
    print("예제 파일 생성에 실패했습니다.")


# 2) 파일의 체크섬 계산
md5_checksum = calculate_file_checksum(file_path, "md5")
print(f"파일명: {file_path}")
print(f"MD5 체크섬: {md5_checksum}")
print("")

# 파일 내용이 동일하면 이 값은 항상 동일!!!

###############################################################
## 예제3) - TCP/IP 스타일의 1의 보수 합계 체크섬
## 데이터 통신(특히 TCP/IP 프로토콜의 헤더)에서 사용되는 
## 전통적인 방식은 1의 보수 합계(Ones' Complement Sum)를 이용하는 체크섬
## 이는 매우 간단하지만 오류 검출 능력이 제한적임
###############################################################

def calculate_ones_complement_checksum(data_bytes):

    """
    1의 보수 합계 방식을 사용하여 체크섬을 계산(네트워크 프로토콜에서 사용)
    16비트 워드(Word)를 가정하고 계산
    :param data_bytes: 바이트 객체 (예: b'hello' )
    :return: 16진수 체크섬 (unsigned short)
    """
    
    # 1. 16비트 워드 단위로 합산
    total_sum = 0
    i = 0

    # 2바이트(16비트) 단위로 합산
    while i < len(data_bytes):
        if i + 1 < len(data_bytes):
            # 두 바이트를 합쳐 16비트 워드 생성 (빅 엔디언 가정)
            word = (data_bytes[i] << 8) + data_bytes[i+1]
            total_sum += word
            i += 2
        else:
            # 마지막 홀수 바이트 처리
            total_sum += data_bytes[i] << 8
            i += 1
            
    # 2. 16비트를 초과하는 캐리(Carry) 처리

    # 캐리가 발생하면 다시 더해줌 (1의 보수 합산 규칙)
    while (total_sum >> 16) > 0:
        carry = (total_sum >> 16)
        total_sum = (total_sum & 0xFFFF) + carry
        
    # 3. 최종 합계의 1의 보수를 취함
    checksum = (~total_sum) & 0xFFFF
    
    return hex(checksum)


# 사용 예시

#data = b'ABCDEFGHIJ'
data = b'0'
checksum_value = calculate_ones_complement_checksum(data)

print(f"원본 바이트: {data}")
print(f"1의 보수 체크섬: {checksum_value}")


