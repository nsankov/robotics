import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(22, GPIO.OUT)

p = GPIO.PWM(22, 50)

p.start(0)
print('ok')
p.ChangeDutyCycle(2.5)
time.sleep(3)
p.ChangeDutyCycle(11.5)
time.sleep(3)
# for x in range(1,13,1):
#     p.ChangeDutyCycle(x)  # turn towards 90 degree
#     print(x)
#     time.sleep(3) # sleep 1 second

p.stop()
GPIO.cleanup()