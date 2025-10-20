"""

################################
## 빅 엔디언(Big-Endian) 방식
################################

 - 빅 엔디언은 가장 중요한 바이트(최상위 바이트)를 메모리나 바이트 시퀀스의 가장 앞쪽에 저장하는 순서

 - 파이썬에서 정수(Integer)를 바이트(Bytes)로 변환할 때 빅 엔디언(Big-Endian) 방식을 지정하는 
   가장 표준적이고 간단한 방법은 내장 함수인 .to_bytes() 메서드를 사용하는 것임

###############################################
## int.to_bytes() 메서드를 사용한 빅 엔디언 변환
###############################################

 -  파이썬에서 정수와 바이트 간의 변환을 처리하는 가장 권장되는 방식

"""

# 정수 값 (십진수 12345)
integer_value = 12345

# 12345를 4바이트 빅 엔디언으로 변환
# 12345 (10진수) = 0x3039 (16진수)
# 빅 엔디언: 00 00 30 39
big_endian_bytes_4 = integer_value.to_bytes(4, byteorder='big')

# 12345를 2바이트 빅 엔디언으로 변환 (3039)
# 2바이트로 충분하므로 앞의 00은 생략됨
big_endian_bytes_2 = integer_value.to_bytes(2, byteorder='big')

print(f"원본 정수: {integer_value}")
print("-" * 30)
print(f"4바이트 빅 엔디언: {big_endian_bytes_4} (0x00003039)")
print(f"2바이트 빅 엔디언: {big_endian_bytes_2} (0x3039)")


"""
##############################################
## 리틀 엔디언(Little-Endian) 방식
##############################################

 - 리틀 엔디언은 가장 덜 중요한 바이트(최하위 바이트)를 메모리나 바이트 시퀀스의 가장 앞쪽에 저장하는 순서
 - 인텔(Intel) 및 AMD 기반 CPU와 같은 대부분의 현대 컴퓨터 아키텍처에서 사용하는 방식

"""
integer_value = 12345

# 12345 (10진수) = 0x3039 (16진수)
# 리틀 엔디언: 39 30 00 00 (최하위 바이트 39가 앞으로 옴)
little_endian_bytes = integer_value.to_bytes(4, byteorder='little')

# 12345를 2바이트 리틀 엔디언으로 변환 (3039)
# 리틀 엔디언: 39 30
little_endian_bytes_2 = integer_value.to_bytes(2, byteorder='little')

print(f"원본 정수: {integer_value}")
print("-" * 40)
print(f"4바이트 리틀 엔디언: {little_endian_bytes} (0x39300000)")
print(f"2바이트 리틀 엔디언: {little_endian_bytes_2} (0x3930)")