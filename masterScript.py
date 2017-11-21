import time
import datetime
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

boolean = True

print "MasterScript running"
#see timeplan.txt for "to-do list"
while boolean:

        #TIME
        timevarH = str(datetime.datetime.now())
        #humidity
        hum = str(sense.get_humidity())
        f = open("/home/pi/RHAB/LOG/hum.txt","a+")
        f.write(hum + "\n")
        f.close()
        #temperature
        temp = str(sense.get_temperature())
        f = open("/home/pi/RHAB/LOG/temp.txt","a+")
        f.write(temp + "\n")
        f.close()
        #pressure
        pres = str(sense.get_pressure())
        f = open("/home/pi/RHAB/LOG/pres.txt","a+")
        f.write(pres + "\n")
        f.close()
        #orientaion
        ori = str("p:{pitch},r:{roll},y:{yaw}".format(**sense.get_orientation_degrees()))
        f = open("/home/pi/RHAB/LOG/ori.txt","a+")
        f.write(ori + "\n")
        f.close()
        #compass
        comp = str("x:{x},y:{y},z:{z}".format(**sense.get_compass_raw()))
        f = open("/home/pi/RHAB/LOG/comp.txt","a+")
        f.write(comp + "\n")
        f.close()


        #Combined file
        f= open("/home/pi/RHAB/LOG/combinedData","a+")
        f.write(timevarH + "," + hum + "," + temp + ","+ pres + "," + ori + "," + comp + "\n")
        f.close()
        print("sensor data writen to file")
        
        time.sleep(10.0)
