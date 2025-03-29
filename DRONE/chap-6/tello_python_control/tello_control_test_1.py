#현재 텔로 드론과 연결 상태 정보 출력
#텔로 자동 이착륙 코드

#드론과 와이파이 연결
#tello_control_test_1.py

import socket
from time import sleep

if __name__ == "__main__":
    local_ip = ''
    local_port = 8890 ## read port
    socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # socket for sending cmd
    socket.bind((local_ip, local_port))

    tello_ip = '192.168.10.1'
    tello_port = 8889 ## write port
    tello_adderss = (tello_ip, tello_port)

    socket.sendto('command'.encode('utf-8'), tello_adderss) ## Enter SDK Mode

    try:
        index = 0
        while True:
            outStr=""
            response, ip = socket.recvfrom(1024)
            if response == 'ok':
                continue
            outStr = 'Tello State:' + str(response)
            print(outStr)
            sleep(0.2)
    except KeyboardInterrupt:
        pass
