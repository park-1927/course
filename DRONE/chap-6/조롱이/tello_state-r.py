#tello_state-r.py

import socket
from time import sleep

########################################################
import curses # curses 확장 모듈을 사용하여 텍스트 모드 디스플레이를 제어
#https://python.flowdas.com/howto/curses.html
########################################################

#INTERVAL = 0.2
INTERVAL= 0.05

def report(str):
    stdscr.addstr(0, 0, str) #0번째 줄 0번째 열부터 str라는 문자열을 출력하라는 의미
    stdscr.refresh() #화면을 갱신하기 위해 창 객체의 refresh() 메서드를 호출

if __name__ == "__main__":
    stdscr = curses.initscr() #curses로 터미널을 제어하려면 먼저 initscr()을 호출하여 터미널 객체 stdscr을 생성해야함
    curses.noecho() #키보드 입력값이 화면에 보이지 않도록 설정

    #응용 프로그램은 또한 일반적으로 Enter 키를 누르지 않아도 즉시 키에 반응해야 함
    #이것을 일반적인 버퍼 입력 모드와 대비하여 cbreak 모드라고 함
    curses.cbreak()

    local_ip = ''
    local_port = 8890
    socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # socket for sending cmd
    socket.bind((local_ip, local_port))

    tello_ip = '192.168.10.1'
    tello_port = 8889
    tello_adderss = (tello_ip, tello_port)

    socket.sendto('command'.encode('utf-8'), tello_adderss)

    try:
        index = 0
        while True:
            index += 1
            #recvfrom() : 클라이언트로부터 데이터 수신(데이터 및 주소 정보 반환)
            response, ip = socket.recvfrom(1024) #좌측에 콤마로 구분된 변수들을 나열하고 우측에 값을 순서대로 나열
            if response == 'ok':
                continue
            out = response.replace(';', ';\n')
            out = 'Tello State:\n' + out
            report(out) #def report(str):
            sleep(INTERVAL)
    except KeyboardInterrupt:
        curses.echo() #키보드 입력값이 화면에 출력되도록 설정
        curses.nocbreak() #cbreak 모드를 해제
        curses.endwin() # endwin() 함수를 호출하여 터미널을 원래 작동 모드로 복원

