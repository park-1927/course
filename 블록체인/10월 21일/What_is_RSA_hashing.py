"""
##################################
## RSA 공개키 암호 시스템
##################################

 - RSA는 대표적인 공개키 암호 시스템(비대칭키 암호화)
 
 - 암호화에 사용하는 공개키(Public Key)-"우편함 주소"와 복호화에 사용하는 개인키(Private Key)-"우편함 열쇠"가 서로 다름
 
 - RSA의 원리 및 역할
	(ㄱ) RSA는 아주 큰 합성수(1과 자기 자신 이외의 약수를 가지는 자연수)의 소인수분해가 어렵다는 수학적 난제에 기반
              (ㄴ)     용어	                  역할                            특징
                   공개키 (Public Key)	암호화에 사용	모두에게 공개되며, 
                   개인키 (Private Key)	복호화에 사용          암호화된 데이터는 이 키를 만든 개인키로만 풀 수 있음


 - 파이썬에서 RSA를 구현하려면 일반적으로 cryptography 라이브러리 대신 
   좀 더 사용자 친화적이고 파일 기반 키 관리가 쉬운 pycryptodome 라이브러리(기존 pycrypto의 보안 개선 버전)를 사용하는 것이 일반적임


#라이브러리 설치

#pip install pycryptodome

"""

from Crypto.Cipher import AES
#from Cryptodome.PublicKey import RSA
#from Cryptodome.Cipher import PKCS1_OAEP

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

# 1. --- RSA 키 쌍 생성 ---
def generate_rsa_key_pair():

    """개인키와 공개키를 생성"""

    # 2048비트는 현재 권장되는 보안 수준임
    key = RSA.generate(2048)
    
    # 개인키 추출 (비밀로 보관)
    private_key = key.export_key()
    
    # 공개키 추출 (다른 사람에게 배포)
    public_key = key.publickey().export_key()
    
    return public_key, private_key

# 2. --- 암호화 (송신자 역할: 수신자의 공개키 사용) ---
def encrypt_message(message: str, public_key_data: bytes) -> bytes:

    """공개키를 사용하여 메시지를 암호화"""

    # 공개키 로드
    recipient_key = RSA.import_key(public_key_data)
    
    # PKCS1 OAEP 패딩을 적용하여 Cipher 객체 생성 (RSA 표준)
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    
    # 문자열 메시지를 바이트로 인코딩하여 암호화
    ciphertext = cipher_rsa.encrypt(message.encode('utf-8'))
    
    return base64.b64encode(ciphertext) # 전송을 위해 Base64 인코딩하여 반환

# 3. --- 복호화 (수신자 역할: 자신의 개인키 사용) ---
def decrypt_message(ciphertext_b64: bytes, private_key_data: bytes) -> str:

    """개인키를 사용하여 암호문을 복호화"""

    # 개인키 로드
    private_key = RSA.import_key(private_key_data)
    
    # Base64 디코딩
    ciphertext = base64.b64decode(ciphertext_b64)
    
    # PKCS1 OAEP 패딩 객체 생성
    cipher_rsa = PKCS1_OAEP.new(private_key)
    
    try:
        # 복호화 후, 바이트를 문자열로 디코딩하여 반환
        plaintext = cipher_rsa.decrypt(ciphertext).decode('utf-8')
        return plaintext
    except ValueError as e:
        # 키가 잘못되었거나 데이터가 변조된 경우 발생
        return f"⚠️ 복호화 실패 (키 불일치 또는 데이터 변조): {e}"


# 4 실행 

# (1) 키 쌍 생성 (수신자 '밥'의 역할)

public_key_bob, private_key_bob = generate_rsa_key_pair()
print("--- 1. 밥의 키 쌍 생성 완료 ---")
print("🔑 밥의 공개키:\n", public_key_bob.decode()[:100] + "...")
print("🔐 밥의 개인키 (비밀):\n", private_key_bob.decode()[:100] + "...")
print("-" * 50)

# (2) 메시지 암호화 (송신자 '앨리스'의 역할)

plaintext = "RSA는 공개키로 암호화하고 개인키로 복호화합니다. 보안을 유지하세요!"
print("평문:", plaintext)

# 앨리스는 밥의 공개키를 사용하여 암호화

ciphertext_b64 = encrypt_message(plaintext, public_key_bob)
print("암호문 (Base64 인코딩):", ciphertext_b64.decode())
print("-" * 50)

# (3) 메시지 복호화 (수신자 '밥'의 역할)
# 밥은 자신의 개인키를 사용하여 복호화
decrypted_text = decrypt_message(ciphertext_b64, private_key_bob)
print("복호화된 평문:", decrypted_text)

# (4) 검증
is_successful = decrypted_text == plaintext
print(f"\n✅ 복호화 성공 여부: {is_successful}")


