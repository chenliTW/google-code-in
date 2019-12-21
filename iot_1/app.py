from datetime import datetime
import Adafruit_DHT
import pause
import requests
import os

api_key=""

temp_aver=float(0)
hum_aver=float(0)
vaild_data=int(0)

while True:
    h, t = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4)
    if h != None and t != None:
        print(str(datetime.now())+" "+str(t)+" "+str(h))
        temp_aver+=t
        hum_aver+=h
        vaild_data+=1
    if datetime.now().minute==59:
        break
    pause.until(datetime(datetime.now().year,datetime.now().month,datetime.now().day,datetime.now().hour,datetime.now().minute+1))

temp_aver/=vaild_data
hum_aver/=vaild_data

print(temp_aver,hum_aver)
pause.until(datetime(datetime.now().year,datetime.now().month,datetime.now().day,datetime.now().hour+1))
requests.get("https://api.thingspeak.com/update?api_key="+api_key+"&field1="+str(temp_aver)+"&field2="+str(hum_aver))
