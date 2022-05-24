# Raspberry Pi Pico Pin Overview by StSkanta (TechCree) 838375
import machine
from machine import Pin
import utime

#Led Pins laden nach Feldnr. GPIO sortiert
led = Pin(25, Pin.OUT) #mainboard led
# Reihe 1
led1 = Pin(1, Pin.OUT) #GP1
led2 = Pin(2, Pin.OUT) #GP2
led3 = Pin(3, Pin.OUT) #GP3
led4 = Pin(4, Pin.OUT) #GP4
led5 = Pin(5, Pin.OUT) #GP5
# Reihe 2
led6 = Pin(6, Pin.OUT) #GP6
led7 = Pin(7, Pin.OUT) #GP7
led8 = Pin(8, Pin.OUT) #GP8
led9 = Pin(9, Pin.OUT) #GP9
led10 = Pin(10, Pin.OUT) #GP10
# Reihe 3
led11 = Pin(11, Pin.OUT) #GP11
led12 = Pin(12, Pin.OUT) #GP12
led13 = Pin(13, Pin.OUT) #GP13
led14 = Pin(14, Pin.OUT) #GP14
led15 = Pin(15, Pin.OUT) #GP15
# Reihe 4
led16 = Pin(16, Pin.OUT) #GP16
led17 = Pin(17, Pin.OUT) #GP17
led18 = Pin(18, Pin.OUT) #GP18
led19 = Pin(0, Pin.OUT) #GP19
led20 = Pin(20, Pin.OUT) #GP20
# Reihe 5
led21 = Pin(21, Pin.OUT) #GP21
led22 = Pin(22, Pin.OUT) #GP22
led23 = Pin(26, Pin.OUT) #GP26
led24 = Pin(27, Pin.OUT) #GP27
led25 = Pin(28, Pin.OUT) #GP28

while True:
# Alle LED zurücksetzen bzw. ausschalten
      led1.value(0)
      led2.value(0)
      led3.value(0)
      led4.value(0)
      led5.value(0)
      led6.value(0)
      led7.value(0)  
      led8.value(0)
      led9.value(0)
      led10.value(0)
      led11.value(0)
      led12.value(0)
      led13.value(0)
      led14.value(0)
      led15.value(0)
      led16.value(0)
      led17.value(0)
      led18.value(0)
      led19.value(0) 
      led20.value(0)
      led21.value(0)
      led22.value(0)
      led23.value(0)
      led24.value(0)
      led25.value(0)
      
      utime.sleep(1)

      #Zeile 1 v L n R
      led1.value(1)
      led2.value(1)
      led3.value(1)
      led4.value(1)
      led5.value(1)

      #Zeile 2 v L n R
      led6.value(1)
      led7.value(1)  
      led8.value(1)
      led9.value(1)
      led10.value(1)

      #Zeile 3 v L n R
      led11.value(1)
      led12.value(1)
      led13.value(1)
      led14.value(1)
      led15.value(1)

      #Zeile 4 v L n R
      led16.value(1)
      led17.value(1)
      led18.value(1)
      led19.value(1) 
      led20.value(1)

      #Zeile 5 v L n R
      led21.value(1)
      led22.value(1)
      led23.value(1)
      led24.value(1)
      led25.value(1)
      
      utime.sleep(5)
      
      # Alle LED zurücksetzen bzw. ausschalten
      led1.value(0)
      led2.value(0)
      led3.value(0)
      led4.value(0)
      led5.value(0)
      led6.value(0)
      led7.value(0)  
      led8.value(0)
      led9.value(0)
      led10.value(0)
      led11.value(0)
      led12.value(0)
      led13.value(0)
      led14.value(0)
      led15.value(0)
      led16.value(0)
      led17.value(0)
      led18.value(0)
      led19.value(0) 
      led20.value(0)
      led21.value(0)
      led22.value(0)
      led23.value(0)
      led24.value(0)
      led25.value(0)