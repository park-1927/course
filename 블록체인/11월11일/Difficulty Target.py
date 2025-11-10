#####################################################
## nBits 값을 지수(Exponent)와 계수(Coefficient)로 분리한 후, 
## 공식에 따라 text{256-bit}의 실제 목표 값을 계산
#####################################################

#####################################################
## 비트 이동 연산을 사용하는 주된 이유는 크게 세 가지
## 곱셈/나눗셈보다 빠르고 효율적인 연산을 수행하고, 
## 특정 비트나 데이터 영역을 빠르게 추출하거나 설정하며, 
## 데이터를 효율적으로 저장하기 위함
#################################################### 

###################################################
## 데이터 인코딩 및 디코딩 (Data Manipulation)
## 비트 이동은 데이터를 효율적으로 압축하거나 해제할 때 필수적으로 사용
## 비트코인의 난이도 목표(nBits)처럼, 여러 정보를 하나의 정수형 변수에 담거나(인코딩) 그 정보를 다시 분리해 낼 때(디코딩) 유용
## 데이터 추출 (Extraction) - 저장된 데이터에서 원하는 특정 부분만 잘라내거나 읽어낼 때 비트 이동과 비트 마스크(AND) 연산을 함께 사용
## 예) 4-byte text{nBits}에서 가장 왼쪽 text{1 byte}를 지수(Exponent)로 추출하기 위해 오른쪽으로 24비트 이동하는 것이 대표적인 예
##################################################

#######################################
##  데이터 인코딩 (압축) 예시: 상태 플래그 합치기
#######################################

# 여러 개의 작은 정보를 정의합니다.
IS_ADMIN = 1       # 1번 비트 사용
IS_ACTIVE = 1      # 2번 비트 사용
ACCESS_LEVEL = 5   # 최대 7 (3비트)

# 32비트 정수 변수에 이 정보를 인코딩합니다.
packed_data = 0

# 1. IS_ADMIN을 0번째 위치에 저장 (1비트)
# 1을 왼쪽으로 0칸 이동 (<< 0)하여 0번 비트에 1을 설정합니다.
packed_data |= (IS_ADMIN << 0)

# 2. IS_ACTIVE를 1번째 위치에 저장 (1비트)
# 1을 왼쪽으로 1칸 이동 (<< 1)하여 1번 비트에 1을 설정합니다.
packed_data |= (IS_ACTIVE << 1)

# 3. ACCESS_LEVEL (5)을 2번째 위치부터 저장 (3비트)
# 5 (101 in binary)를 왼쪽으로 2칸 이동 (<< 2)하여 2, 3, 4번 비트에 저장합니다.
packed_data |= (ACCESS_LEVEL << 2)

print("--- 데이터 인코딩 (합치기) ---")
print(f"인코딩된 데이터 (10진수): {packed_data}")
print(f"인코딩된 데이터 (2진수): {bin(packed_data)} ({32-len(bin(packed_data)[2:]):02d}개의 0 패딩)")
# 0b10111 (23)
################################################################################

###########################################################
## 데이터 디코딩 (추출) 예시: 압축된 정보 분리
## 위에서 인코딩된 packed_data에서 원래의 개별 정보를 다시 추출하는 경우
## 이 과정에는 비트 이동(≫)과 비트 마스크(&) 연산이 모두 사용
###########################################################

# 3비트(0b111) 마스크를 사용하여 ACCESS_LEVEL을 추출합니다.
ACCESS_MASK = 0b111 # 7

# 1. IS_ADMIN 추출 (0번째 위치)
# 0칸 오른쪽 이동 (>> 0) 후 1 (& 0b1)로 마스킹하여 0번 비트만 추출합니다.
extracted_admin = (packed_data >> 0) & 1

# 2. IS_ACTIVE 추출 (1번째 위치)
# 1칸 오른쪽 이동 (>> 1) 후 1 (& 0b1)로 마스킹하여 1번 비트만 추출합니다.
extracted_active = (packed_data >> 1) & 1

# 3. ACCESS_LEVEL 추출 (2번째 위치)
# 2칸 오른쪽 이동 (>> 2)하여 시작 위치(2번 비트)까지 데이터를 옮깁니다.
# 그 후 3비트 마스크 (7)를 적용하여 3비트 값만 추출합니다.
extracted_access = (packed_data >> 2) & ACCESS_MASK

print("\n--- 데이터 디코딩 (분리) ---")
print(f"1. IS_ADMIN 추출: {extracted_admin}")
print(f"2. IS_ACTIVE 추출: {extracted_active}")
print(f"3. ACCESS_LEVEL 추출: {extracted_access}")
#################################################


import math

# 예시 nBits 값 (Genesis Block의 난이도 1에 해당하는 값)
# 0x1d00ffff는 4-byte(32-bit)로 저장됩니다.
nBits_hex = "1d00ffff" 
nBits_decimal = int(nBits_hex, 16)

def calculate_target(nBits):
    """
    nBits (Packed Bits Format) 값을 입력받아 256-bit Target 값을 계산합니다.
    Target = Coefficient * 2^(8 * (Exponent - 3))
    """


   # 1. 지수(Exponent) 추출: nBits의 가장 왼쪽 1바이트 (8비트)
    # 비트코인에서 nBits는 Little Endian으로 저장되지만, 계산을 위해 Big Endian으로 간주합니다.
    exponent = nBits >> 24  # 32비트 중 상위 8비트 추출 (오른쪽으로 24비트 이동)
    
    # 2. 계수(Coefficient) 추출: nBits의 나머지 3바이트 (24비트)
    # 0x00ffffff는 나머지 24비트(하위 3바이트)만 마스킹(AND)하여 추출합니다.
    coefficient = nBits & 0x00ffffff
    
    print(f"--- nBits ({hex(nBits)}) 분석 ---")
    print(f"1. 지수 (Exponent): {hex(exponent)} (십진수: {exponent})")
    print(f"2. 계수 (Coefficient): {hex(coefficient)} (십진수: {coefficient})")
    
    # 3. Target 값 계산
    # Python에서 매우 큰 정수 연산을 수행합니다.
    
    # Target = Coefficient * (2 ^ (8 * (Exponent - 3)))
    # shift_bits는 Coefficient에 붙여야 할 0의 총 비트 수입니다.
    shift_bits = 8 * (exponent - 3)
    
    # Target = Coefficient를 shift_bits만큼 왼쪽으로 비트 이동 (0 붙이기)
    target = coefficient << shift_bits
    
    # Target은 256-bit 숫자로 표현됩니다.
    
    print("-" * 30)
    print(f"3. 비트 이동 수: {shift_bits} bits")
    print(f"4. 계산된 Target (십진수): {target}")
    print(f"5. 계산된 Target (256-bit 16진수): {target:064x}") # 64자리(256비트)로 패딩
    print("-" * 30)
    
    return target

# 함수 실행
target_value = calculate_target(nBits_decimal)


