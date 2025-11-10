"""
############################
## 하드코딩 (Hardcoding)
############################

 - 하드코딩은 데이터나 설정 값을 코드 본문(Source Code) 내부에 고정된 상수로 직접 삽입하는 방식
 - 값이 변경될 때마다 코드를 직접 수정하고 재배포해야 하는 단점이 있음.

# 아래 코드는 할인율 0.1과 배송비 3000원을 코드 안에 고정했음

# 하드코딩된 값 : 할인율 0.1 (10%), 배송비 3000

"""

DISCOUNT_RATE = 0.1
SHIPPING_FEE = 3000

def calculate_final_price(item_price, quantity):
    """
    할인율과 배송비를 코드 내 상수 값으로 직접 계산
    """
    
    subtotal = item_price * quantity
    
    # ❗️ 할인율(0.1)이 코드 내에 직접 사용됨
    discounted_price = subtotal * (1 - DISCOUNT_RATE) 
    
    # ❗️ 배송비(3000)가 코드 내에 직접 사용됨
    final_price = discounted_price + SHIPPING_FEE
    
    return final_price

# 예시 실행
price = calculate_final_price(10000, 3)
print(f"하드코딩된 최종 가격: {price} 원")
print()

# 만약 할인율을 0.2로 변경하려면, 코드 파일을 열어 수정해야 함

"""
###########################
## 소프트코딩 (Softcoding)
###########################

 - 소프트코딩은 변경될 가능성이 있는 데이터나 설정 값을 코드 본문 외부(예: 설정 파일, 데이터베이스, 환경 변수 등)에 분리하여 저장하고, 
   프로그램이 실행될 때 읽어와서 사용하는 방식
 - 값이 변경되어도 코드 자체는 수정할 필요가 없음


# 아래 코드는 설정 값을 외부 INI 파일에서 읽어와 적용함

################################
##1. 외부 설정 파일 (config.ini) 준비
###############################

#[Pricing]
# 할인율 20%로 변경
discount_rate = 0.2
# 배송비 5000원으로 변경
shipping_fee = 5000

#################################
## 2. 파이썬 코드 (설정 값을 읽어와 사용)
#################################

import configparser

# 설정 파일에서 값을 읽어오는 함수

def load_config(filename='config.ini'):
    config = configparser.ConfigParser()
    config.read(filename)
    
    # 설정 파일에서 값을 읽어와 반환
    discount = config.getfloat('Pricing', 'discount_rate')
    shipping = config.getint('Pricing', 'shipping_fee')
    
    return discount, shipping

def calculate_final_price_softcoded(item_price, quantity):

    # 설정 파일에서 읽어온 값으로 계산
    
    # 1. 설정 값을 외부에서 가져옴 (소프트코딩)
    discount_rate, shipping_fee = load_config()
    
    print(f"\n[소프트코딩] 현재 설정: 할인율 {DISCOUNT_RATE}, 배송비 {SHIPPING_FEE} 원")
    
    subtotal = item_price * quantity
    
    # 설정 파일에서 가져온 변수 값을 사용
    discounted_price = subtotal * (1 - discount_rate) 
    final_price = discounted_price + shipping_fee
    
    return final_price

# 예시 실행
price_softcoded = calculate_final_price_softcoded(10000, 3)
print(f"소프트코딩된 최종 가격: {price_softcoded} 원")

# 만약 할인율을 0.3으로 변경하려면, config.ini 파일만 수정하면 됨 
# 코드를 수정하거나 재배포할 필요가 없음

"""

################################################

def load_password():
    """외부 파일에서 비밀번호를 읽어오는 함수"""
    try:
        # 코드 외부에 있는 config.txt 파일을 읽음

        with open('config.txt', 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        return ""

def attempt_login_softcoded(input_password):
    CORRECT_PASSWORD = load_password()
    
    if not CORRECT_PASSWORD:
        print("오류: 비밀번호 설정 파일을 찾을 수 없습니다.")
        return False

    if input_password == CORRECT_PASSWORD:
        print("로그인 성공! (소프트코딩)")
        return True
    else:
        print("로그인 실패. 비밀번호를 확인하세요.")
        return False

attempt_login_softcoded('MySecretPassword123')

# softcoded_login.py를 실행하고 올바른 초기 비밀번호를 입력!!!!

# 비밀번호를 'NewSecurePass'로 바꾸고 싶으면,
# config.txt 파일 내용만 'NewSecurePass'로 수정하면 됨