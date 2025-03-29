#텔로 자동 이착륙 코드
#pip install djitellopy 설치
#드론과 와이파이 연결
#tello_take_off.py

from djitellopy import Tello
import time
print("Create Tello object")
tello=Tello()

print("Connect to Tello Frone")
tello.connect()

battery_level = tello.get_battery()
print(f"Battery Life Percentage: {battery_level}")

print("Take off!")
tello.takeoff()

print("Sleep for 5 seconds")
time.sleep(5)

print("Landing")
tello.land()

print("touchdown......goodbye")
