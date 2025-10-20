"""

#########################################
## 랜섬웨어
########################################

 - 파일 시스템에 실제 손상을 주지 않으면서 랜섬웨어의 핵심적인 동작 원리인 '파일 암호화'와 '랜섬 노트 생성'을 
   모방한 가상의 시뮬레이션 코드

 - 핵심 원리 요약 - 랜섬웨어 공격은 일반적으로 다음 두 단계로 구성

 	ㄱ) 파일 암호화 (Encryption)

		* 대칭 키 암호화 알고리즘(예: AES)을 사용하여 사용자 파일을 빠르게 암호화
		* 이때 사용한 암호화 키는 다시 공개 키 암호화(비대칭 키)를 사용하여 공격자만 해독할 수 있는 키로 한 번 더 암호화됨

	ㄴ) 랜섬 노트 생성 (Ransom Note)
		* 암호화된 파일이 있는 디렉터리마다 READ_ME.txt와 같은 파일을 남겨놓고, 몸값 지불 방법과 복구 방법을 안내함

#########################################################
"""

# 1. 테스트 환경 설정

# 시뮬레이션을 위한 테스트 파일을 생성

# test_file.txt 생성

with open("test_file.txt", "w", encoding="utf-8") as f:
    f.write("이것은 중요한 파일의 내용입니다. 암호화되기 전 원본 텍스트.")

# 2. 시뮬레이션 코드 (ransom_simulator.py)

# test_file.txt를 찾아 내용을 변경하고 랜섬 노트를 생성

import os

# --- 설정 ---

TARGET_FILE = "test_file.txt"
RANSOM_NOTE_FILE = "READ_ME_NOW.txt"
ENCRYPTED_CONTENT = "AES-256-ENCRYPTED-DATA-BLOCK" # 실제 암호화된 것처럼 보이는 가짜 데이터

def simulate_encryption():

    """실제 파일 대신 가상의 암호화된 내용으로 파일을 덮어씀"""

    try:
        # 1. 파일 확인
        if not os.path.exists(TARGET_FILE):
            print(f"ERROR: 대상 파일 '{TARGET_FILE}'을 찾을 수 없습니다.")
            return

        # 2. 파일 덮어쓰기 (암호화 모방)
        with open(TARGET_FILE, "w", encoding="utf-8") as f:
            f.write(ENCRYPTED_CONTENT)

        print(f"[SUCCESS] '{TARGET_FILE}' 파일이 암호화된 것처럼 변경되었습니다.")

    except Exception as e:
        print(f"파일 처리 중 오류 발생: {e}")

def create_ransom_note():

    """몸값 요구 파일을 생성"""

    note_content = (

        "*** 당신의 파일은 암호화되었습니다! ***\n"
        "당신의 중요한 데이터는 해독할 수 없는 상태로 변경되었습니다.\n"
        "파일을 복구하려면 0.1 BTC를 다음 주소로 보내십시오.\n"
        "복호화 키를 받기 위한 이메일 주소: restore-data@anon.com\n"
        "절대 파일을 삭제하거나 내용을 변경하지 마십시오!"
    )

    with open(RANSOM_NOTE_FILE, "w", encoding="utf-8") as f:
        f.write(note_content)

    print(f"[SUCCESS] '{RANSOM_NOTE_FILE}' 파일이 생성되었습니다.")


# --- 실행 ---

if __name__ == "__main__":
    print("--- 랜섬웨어 시뮬레이션 시작 ---")
    simulate_encryption()
    create_ransom_note()
    print("--- 시뮬레이션 완료 ---")

# 3. 시뮬레이션 결과

# 위 코드를 실행한 후 파일 시스템을 확인하면 다음과 같은 결과를 볼 수 있음

# test_file.txt 파일의 내용이 AES-256-ENCRYPTED-DATA-BLOCK으로 바뀌어 복구할 수 없는 것처럼 보임(실제 랜섬웨어는 파일 내용을 암호화 키로 잠금)

# READ_ME_NOW.txt라는 랜섬 노트 파일이 생성되어 몸값 지불을 요구하는 메시지가 적혀 있음

