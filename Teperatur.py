#Show Temperatur
import machine 
import utime
from machine import ADC #Mainboard Sensor
from machine import Pin
import time, random


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

#Pause
#Zeile 1 v L n R
#  led1.value(1)          led2.value(1)          led3.value(1)          led4.value(1)          led5.value(1)
#Zeile 2 v L n R
#  led6.value(1)          led7.value(1)          led8.value(1)          led9.value(1)          led10.value(1)
#Zeile 3 v L n R
#  led11.value(1)         led12.value(1)         led13.value(1)         led14.value(1)         led15.value(1)
#Zeile 4 v L n R
#   led16.value(1)        led17.value(1)         led18.value(1)         led19.value(1)         led20.value(1)
#Zeile 5 v L n R
#   led21.value(1)        led22.value(1)         led23.value(1)         led24.value(1)         led25.value(1)


# Setup Temperaturmessung und Konvertierung
sensor_temp = machine.ADC(4) 
conversion_factor = 3.3 / (65535) 


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

        loop = 0
        while loop <= 2:
            h = 0
            o = 0
            reading = sensor_temp.read_u16() * conversion_factor
            temperature = round(27 - (reading - 0.706) / 0.001721)
            tempa=temperature
            print("TEMPERATUR")
            print (tempa)
            #print("  " + "{:.0f}".format(temperature) + "." + "c", 10, 30, 0, 7)
            utime.sleep(3)
        
#LED zeigen Temperaturbereiche an    
            if tempa == 0:
                led1.value(1)    
            
            if tempa == 1:
                led1.value(1)
                led2.value(1)
            
            if tempa == 2:
                led1.value(1)
                led2.value(1)
                led3.value(1)

            if tempa == 3:
                led1.value(1)
                led2.value(1)
                led3.value(1)
                led4.value(1)
           
            if tempa == 4:
                led1.value(1)
                led2.value(1)
                led3.value(1)
                led4.value(1)
                led5.value(1)
          
            if tempa == 5:
                led1.value(1)
                led2.value(1)
                led3.value(1)
                led4.value(1)
                led5.value(1)
                led6.value(1)
                
            if tempa == 6:
                led1.value(1)
                led2.value(1)
                led3.value(1)
                led4.value(1)
                led5.value(1)
                led6.value(1)
                led7.value(1)  
          
            if tempa == 7:
                led1.value(1)
                led2.value(1)
                led3.value(1)
                led4.value(1)
                led5.value(1)
                led6.value(1)
                led7.value(1)
                led8.value(1)
          
            if tempa == 8:
                led1.value(1)
                led2.value(1)
                led3.value(1)
                led4.value(1)
                led5.value(1)
                led6.value(1)
                led7.value(1)
                led8.value(1)
                led9.value(1)
 
            if tempa == 9:
                led1.value(1)
                led2.value(1)
                led3.value(1)
                led4.value(1)
                led5.value(1)
                led6.value(1)
                led7.value(1)
                led8.value(1)
                led9.value(1)
                led10.value(1)
          
            if tempa == 10:
                led1.value(1)
                led2.value(1)
                led3.value(1)
                led4.value(1)
                led5.value(1)
                led6.value(1)
                led7.value(1)
                led8.value(1)
                led9.value(1)
                led10.value(1)
                led11.value(1)
###          
            if tempa == 11:
                led00.value(1)
                led04.value(1)
          
            if tempa == 12:
                led01.value(1)
                led04.value(1)
          
            if tempa == 13:
                led00.value(1)
                led01.value(1)
                led04.value(1)

            if tempa == 14:
                led02.value(1)
                led04.value(1)
          
            if tempa == 15:
                led00.value(1)
                led02.value(1)
                led04.value(1)
          
            if tempa == 16:
                led01.value(1)
                led02.value(1)
                led04.value(1)
          
            if tempa == 17:
                led00.value(1)
                led01.value(1)
                led02.value(1)
                led04.value(1)

            if tempa == 18:
                led03.value(1)
                led04.value(1)
          
            if tempa == 19:
                led00.value(1)
                led03.value(1)
                led04.value(1)
          
            if tempa == 20:
                led05.value(1)
          
            if tempa == 21:
                led00.value(1)
                led05.value(1)
          
            if tempa == 22:
                led01.value(1)
                led05.value(1)
          
            if tempa == 23:
                led00.value(1)
                led01.value(1)
                led05.value(1)

            if tempa == 24:
                led02.value(1)
                led05.value(1)
          
            if tempa == 25:
                led00.value(1)
                led02.value(1)
                led05.value(1)
          
 
          
            if ((tempa>= 25) and (tempa<= 50)):
                led23.value(0)
 
            utime.sleep(5)

            #Reset
            led00.value(0)
            led01.value(0)
            led02.value(0)
            led03.value(0)
            led04.value(0)
            led05.value(0)
            led06.value(0)
            led07.value(0)
            led08.value(0)
            led09.value(0)
            led10.value(0)
            led11.value(0)
            led12.value(0)
            led13.value(0)
            led14.value(0)
            led16.value(0)
            led17.value(0)
            led18.value(0)
            led19.value(0)
            led20.value(0)
            led21.value(0)
            led22.value(0)
            
            loop = loop + 1
            
        if loop >= 3:
            break
        continue 
        #    exec(open('change.py').read())

