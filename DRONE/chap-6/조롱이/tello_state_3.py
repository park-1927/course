#-*- coding: utf-8 -*-  #한글 인코딩 옵션 

#tello_control_test_1.py  - 현재 텔로 드론과 연결 상태 정보 출력
#드론과 와이파이 연결



#소켓 통신을 하기 위해 socket이라는 모듈을 import
import socket 

#time 라이브러리의 sleep 함수를 사용하면 일정 시간동안 프로세스를 일시정지 
from time import sleep 

#__name__ 변수는 현재 모듈의 이름을 담고 있는 내장 변수
#모듈이 직접 실행되었는지(import 되었는지 아닌지) 판단할 때 __name__ 변수의 값을 사용
#일반적으로, 모듈은 직접 실행되거나 다른 모듈에서 import 되어 사용됨
#만약 모듈이 직접 실행되면, __name__ 변수는 문자열"__main__"이 할당됨
#반대로, 모듈이 import 되어 사용될 때는,__name__변수는 해당 모듈의 이름(파일명)이 할당됨
#따라서, __name__ 변수의 값을"__main__"과 비교하면 현재 모듈이 직접 실행되는지(import 되는지)를 판단할 수 있음
#따라서 코드를 if __name__ == "__main__"로 감싸면, 해당 파일이 모듈로 사용될 때는 실행되지 않고, 직접 실행될 때만 실행됨

if __name__ == "__main__":
    local_ip = ''
    local_port = 8890  # 입력 포트 저장

    #파이썬에서 비연결성 UDP 소켓을 생성
    #socket.AF_INET - IPv4 주소를 의미 
    #socket.SOCK_DGRAM - 비연결성 소켓 유형 
    #socket 모듈 - BSD 소켓 인터페이스에 대한 액세스를 제공 
    #socket() 함수 - 소켓 객체를 반환하고, 이 소켓 객체의 메서드는 다양한 소켓 시스템 호출을 구현 

    socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # socket for sending cmd
    socket.bind((local_ip, local_port)) #소켓 주소 정보 할당

    tello_ip = '192.168.10.1' # Tello는 AP(Access Point)이며 주소는 ip 192.168.10.1을 사용

    #Send Command & Receive Response
    #명령어는 UDP Port 8889를 통하여 보내줄 수 있으며 첫번째는 'command' 명령을 보내어 SDK 모드가 되도록 함
    tello_port = 8889 # port 출력(저장)
    tello_adderss = (tello_ip, tello_port)
    socket.sendto('command'.encode('utf-8'), tello_adderss) # SDK Mode 진입

    try:
        index = 0
        while True:
            outStr=""
            response, ip = socket.recvfrom(1024) #클라이언트로부터 데이터 수신(데이터 및 주소 정보 반환)
            if response == 'ok':
                continue
            outStr = 'Tello State:' + str(response)
            print(outStr)
            sleep(0.2)
    except KeyboardInterrupt:
        pass  # "아무것도 하지 않는" 명령어, 마치 # 코멘트 처리되어 있는 라인과 같은 효과를 가짐