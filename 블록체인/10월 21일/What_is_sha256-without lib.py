import math

# 1. 초기 해시값 (H0~H7)과 라운드 상수 (K) 정의
# 이 값들은 소수의 제곱근의 소수부에서 얻어짐

h_init = [
    0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
    0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
]

k_const = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
]

# 2. SHA-256 비트 연산 함수 정의
# 32비트 워드 기반의 비트 연산을 수행

def _rotr(x, n): return (x >> n) | (x << (32 - n)) & 0xFFFFFFFF
def _shr(x, n): return (x >> n)
def _ch(x, y, z): return (x & y) ^ (~x & z)
def _maj(x, y, z): return (x & y) ^ (x & z) ^ (y & z)
def _sigma0(x): return _rotr(x, 2) ^ _rotr(x, 13) ^ _rotr(x, 22)
def _sigma1(x): return _rotr(x, 6) ^ _rotr(x, 11) ^ _rotr(x, 25)
def _capsigma0(x): return _rotr(x, 7) ^ _rotr(x, 18) ^ _shr(x, 3)
def _capsigma1(x): return _rotr(x, 17) ^ _rotr(x, 19) ^ _shr(x, 10)

def sha256_custom(message):

    # 3. 메시지 전처리 및 패딩
    # 메시지를 바이트로 변환하고 1을 추가, 512비트의 배수로 만듬

    message_bytes = message.encode('utf-8')
    ml = len(message_bytes) * 8
    message_bytes += b'\x80'
    while (len(message_bytes) * 8) % 512 != 448:
        message_bytes += b'\x00'
    message_bytes += ml.to_bytes(8, 'big')

    # 4. 해시 계산
    h = list(h_init)
    for i in range(0, len(message_bytes), 64):
        chunk = message_bytes[i:i+64]
        words = list(int.from_bytes(chunk[j:j+4], 'big') for j in range(0, 64, 4))
        
        # 64개의 워드 배열 확장
        for t in range(16, 64):
            s0 = _capsigma0(words[t-15])
            s1 = _capsigma1(words[t-2])
            words.append((words[t-16] + s0 + words[t-7] + s1) & 0xFFFFFFFF)

        a, b, c, d, e, f, g, hh = h[:] # 현재 해시값을 임시 변수에 복사

        # 64라운드 압축 함수 실행
        for t in range(64):
            t1 = (hh + _sigma1(e) + _ch(e, f, g) + k_const[t] + words[t]) & 0xFFFFFFFF
            t2 = (_sigma0(a) + _maj(a, b, c)) & 0xFFFFFFFF
            hh, g, f, e, d, c, b, a = g, f, e, (d + t1) & 0xFFFFFFFF, c, b, a, (t1 + t2) & 0xFFFFFFFF
        
        # 라운드 결과값 누적
        h = [(h[j] + [a, b, c, d, e, f, g, hh][j]) & 0xFFFFFFFF for j in range(8)]

    # 5. 최종 해시값 생성
    return ''.join(f'{x:08x}' for x in h)


# 예제 사용
message = "Hello, World!"
hashed_message = sha256_custom(message)
print(f"원본 데이터: {message}")
print(f"SHA-256 해시값: {hashed_message}")