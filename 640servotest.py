import time
from darkwater_640.darkwater_640 import dw_Controller, dw_Servo, dw_Motor

dw = dw_Controller( addr=0x60 )
s1 = dw.getServo(1)
s2 = dw.getServo(2)

s1.off()
s2.off()
time.sleep(1)

print "Set 2000uS - "
print "Servo 1"
s1.setPWMuS(2000)
time.sleep(1)
print "Servo 2"
s2.setPWMuS(2000)
time.sleep(1)
print "Set 1500uS - "
print "Servo 1"
s1.setPWMuS(1500)
time.sleep(1)
print "Servo 2"
s2.setPWMuS(1500)
time.sleep(1)
print "Set 1000uS - "
print "Servo 1"
s1.setPWMuS(1000)
time.sleep(1)
print "Servo 2"
s2.setPWMuS(1000)
time.sleep(1)
print "All off"
s1.off()
s2.off()
