#-*- coding: utf-8 -*- 

#tello_test(3_7).py - #자동 이착륙 코드

# 반드시 드론을 멀리 떨어져서 실행할 것
# 두 개의 파일 -  폴더 Single_Tello_Test에 있는 stats와 tello를 같은 폴더에 위치하고 실행할 것
# command 파일 작성할 것

#드론과 와이파이 연결

from tello import Tello
from datetime import datetime
import time  #time 모듈은 Python에서 시간 관련 작업을 수행하기 위한 표준 라이브러리

start_time = str(datetime.now())
file_name ="command.txt"
f = open(file_name, "r")
commands = f.readlines()  # readlines() : 파일 내 텍스트에서 각 줄을 element로 하는 리스트로 반환
tello = Tello()

for command in commands:
    if command != '' and command != '\n':
        command = command.rstrip()  #인자로 전달된 문자를 String의 오른쪽에서 제거
        if command.find('delay') != -1:
            sec = float(command.partition('delay')[2])
            print('delay %s' % sec)
            time.sleep(sec)
            pass
        else:
            tello.send_command(command)

log = tello.get_log()  #get_log method is used to get the log for a given log type
outFile = open('log.txt', 'w+') 
for stat in log:
    stat.print_stats()
    str = stat.return_stats()
    outFile.write(str)


#command.txt의 내용
#takeoff
#delay 5
#land
