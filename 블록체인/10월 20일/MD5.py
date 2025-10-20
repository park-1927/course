####################################################################
## MD5 해시 함수를 사용하는 가장 간단하고 표준적인 방법은 내장 모듈인 hashlib를 이용
####################################################################

###########################################
## 텍스트 문자열에 대한 MD5 해시값을 계산
###########################################

import hashlib

def generate_md5_hash(data_string):
    """
    주어진 문자열에 대한 MD5 해시값을 생성
    
    :param data_string: 해시할 문자열
    :return: 16진수 형태의 MD5 해시값 (32자리)
    """

    # 1. hashlib.md5() 객체를 생성
    md5_hash = hashlib.md5()
    
    # 2. 문자열을 바이트 형태로 인코딩하여 해시 객체에 업데이트
    #    해시 함수는 문자열이 아닌 바이트(bytes) 입력을 받음
    md5_hash.update(data_string.encode('utf-8'))
    
    # 3. 최종 해시값을 16진수 문자열로 반환
    return md5_hash.hexdigest()

# 예시 사용
text_to_hash = "안녕하세요, MD5 해시를 테스트합니다!"
md5_result = generate_md5_hash(text_to_hash)

print(f"원본 문자열: {text_to_hash}")
print(f"MD5 해시값: {md5_result}")
print(f"해시 길이: {len(md5_result)} 자리") 
# MD5는 128비트 해시를 생성하며, 16진수로 표현하면 32자리