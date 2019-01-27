import time
import pigpio
pi = pigpio.pi()

RedPin = 17
GreenPin = 22
BluePin = 24


print("tesing for red")

pi.set_PWM_dutycycle(RedPin, 255)
time.sleep(2)

pi.set_PWM_dutycycle(RedPin, 0)
time.sleep(1)

print("testing for green")

pi.set_PWM_dutycycle(GreenPin, 255)
time.sleep(2)

pi.set_PWM_dutycycle(GreenPin, 0)
time.sleep(1)

print("testing for blue")

pi.set_PWM_dutycycle(BluePin, 255)
time.sleep(2)

pi.set_PWM_dutycycle(BluePin, 0)
time.sleep(1)

pi.stop()
