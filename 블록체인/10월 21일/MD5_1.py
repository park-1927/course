###############################################################
## 파일 해시 생성 코드
## MD5는 파일의 무결성 검사에도 자주 사용됨
## 큰 파일의 경우 메모리 효율성을 위해 파일을 조각(chunk)으로 읽어 처리함
###############################################################

import hashlib

def generate_md5_for_file(filepath):

    """
    파일 경로를 입력받아 파일 전체의 MD5 해시값을 계산
    
    :param filepath: 해시할 파일의 경로
    :return: 16진수 형태의 MD5 해시값, 또는 에러 메시지
    """

    hasher = hashlib.md5()
    
    try:

        # 파일을 바이너리 읽기 모드 ('rb')로 오픈

        with open(filepath, 'rb') as file:
            # 큰 파일 처리를 위해 64KB 단위로 파일을 읽음

            buffer = file.read(65536) 
            while len(buffer) > 0:
                hasher.update(buffer)
                buffer = file.read(65536)
        
        return hasher.hexdigest()
    
    except FileNotFoundError:
        return "오류: 파일을 찾을 수 없습니다."
    except Exception as e:
        return f"오류 발생: {e}"

# 사용 예시 (실제 파일 경로를 넣어 테스트)

file_path = "file.txt"
file_md5 = generate_md5_for_file(file_path)

print(f"파일 MD5 해시값: {file_md5}")

