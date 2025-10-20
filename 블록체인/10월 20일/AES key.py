"""
#################################
## PyCryptodome을 이용한 AES 키 생성
#################################

 - 보안 암호화 작업에는 표준 라이브러리 대신 전문적인 암호화 라이브러리인
   PyCryptodome(pip install pycryptodome 필요)을 사용하는 것이 권장됨

"""

from Crypto.Random import get_random_bytes

# AES는 128, 192, 256비트 키를 사용
# 128비트 = 16바이트
# 192비트 = 24바이트
# 256비트 = 32바이트 (가장 권장됨)

def generate_aes_key(key_size_bytes):

    """
    지정된 크기의 AES 암호화 키를 생성
    key_size_bytes는 16, 24, 또는 32여야 함
    """

    if key_size_bytes not in [16, 24, 32]:
        raise ValueError("AES 키 크기는 16, 24, 32 바이트 중 하나여야 합니다.")
    
    # 강력한 의사 난수 생성기를 사용하여 키 생성
    key = get_random_bytes(key_size_bytes)
    return key

# --- 키 생성 예시 ---

# 1. AES-256 키 생성 (32 바이트)
key_256 = generate_aes_key(32)

# 2. AES-128 키 생성 (16 바이트)
key_128 = generate_aes_key(16)

print(f"AES-256 (32 바이트) 키 생성: {key_256.hex()}")
print(f"길이: {len(key_256)} 바이트")
print("-" * 30)
print(f"AES-128 (16 바이트) 키 생성: {key_128.hex()}")
print(f"길이: {len(key_128)} 바이트")