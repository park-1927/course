"""

###############################################
## 암호화와 복호화
################################################

 - 암호화(Encryption)와 복호화(Decryption)는 데이터를 보호하기 위해 사용

 - 암호화는 평문(Plaintext)을 알아볼 수 없는 암호문(Ciphertext)으로 변환하고, 복호화는 암호문을 다시 평문으로 되돌리는 과정


#########################################################################
## 파이썬에서는 일반적으로 cryptography 라이브러리를 사용하여 강력한 암호화를 구현
## 여기서는 널리 사용되는 대칭키 암호화 방식인 AES(Advanced Encryption Standard)를 사용
#########################################################################

1. AES 대칭키 암호화 및 복호화 예

  - 대칭키 암호화는 암호화와 복호화에 동일한 비밀 키(Secret Key)를 사용하는 방식

      * cryptography 라이브러리 내의 Fernet 모듈을 사용
      * Fernet은 AES 암호화, HMAC(메시지 인증 코드) 및 기타 보안 기능을 하나의 간편한 패키지로 결합하여 안전한 사용을 보장
"""

#pip install cryptography

from cryptography.fernet import Fernet
import base64
import os

# --- 1. 키 생성 (Key Generation) ---

# Fernet은 32바이트 (256비트)의 키를 사용하며, Base64로 인코딩되어야 함

def generate_fernet_key():

    """안전한 32바이트 Fernet 키를 생성"""

    # os.urandom을 사용하여 안전한 랜덤 바이트 생성
    return base64.urlsafe_b64encode(os.urandom(32))

# --- 2. 암호화 함수 (Encryption) ---

def encrypt_message(message: str, key: bytes) -> bytes:

    """메시지를 주어진 키로 암호화"""

    # Fernet 객체 생성
    f = Fernet(key)
    
    # 문자열을 바이트로 인코딩한 후 암호화
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

# --- 3. 복호화 함수 (Decryption) ---

def decrypt_message(encrypted_message: bytes, key: bytes) -> str:

    """암호문을 주어진 키로 복호화"""

    f = Fernet(key)
    
    try:
        # 암호문을 복호화한 후, 바이트를 다시 문자열로 디코딩
        decrypted_message = f.decrypt(encrypted_message).decode()
        return decrypted_message
    except Exception as e:
        # 키가 잘못되었거나 암호문이 변조된 경우 에러 발생
        return f"복호화 실패: {e}"


# 실행 및 시연

# 1. 암호화/복호화에 사용할 비밀 키 생성

secret_key = generate_fernet_key()
print(" 생성된 비밀 키 (Base64 인코딩):", secret_key.decode())
print("-" * 50)

# 2. 평문 메시지 정의
plaintext = "이것은 기밀로 유지되어야 할 비밀 메시지입니다."
print("평문 (Plaintext):", plaintext)

# 3. 암호화 실행
ciphertext = encrypt_message(plaintext, secret_key)
print("암호문 (Ciphertext):", ciphertext.decode())
print("-" * 50)

# 4. 복호화 실행
decrypted_text = decrypt_message(ciphertext, secret_key)
print("복호화된 평문:", decrypted_text)

# 5. 복호화 검증
print(f"\n복호화 성공 여부: {plaintext == decrypted_text}")