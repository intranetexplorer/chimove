#!/usr/bin/env python2
#42.057562,-88.041430 - 1600 mcconnor pkwy schaumburg
#41.872293,-87.633294  - 170 W Polk Chicago
# https://maps.googleapis.com/maps/api/distancematrix/json?origins=42.057562,-88.041430&destinations=41.872293,-87.633294&departure_time=now&units=imperial&key=AIzaSyCVvUXJuWMS5ap0XC8oQK0XNaKFq3XtFXw
# https://maps.googleapis.com/maps/api/distancematrix/json?origins=41.872293,-87.633294&destinations=42.057562,-88.041430&departure_time=now&units=imperial&key=AIzaSyCVvUXJuWMS5ap0XC8oQK0XNaKFq3XtFXw

# While loop
# Reset variables
# make api call
# Parse Json to get time in traffic
# Set date, Day, Time, Route (S2C,C2S), time in traffic
# Write to file - Append
# Save file
# wait 5 mins - 300 sec

import sys;
import datetime;
import time;
import json;
import requests;


#t=datetime.datetime.now()
#print(str(t)+','+ "\n")
req=requests.get('https://maps.googleapis.com/maps/api/distancematrix/json?origins=41.872293,-87.633294&destinations=42.057562,-88.041430&departure_time=now&units=imperial&key=AIzaSyCVvUXJuWMS5ap0XC8oQK0XNaKFq3XtFXw')
resp=req.json()
duration_text=resp['rows'][0]['elements'][0]['duration_in_traffic']['text']
duration_secs=resp['rows'][0]['elements'][0]['duration_in_traffic']['value']
C2S=str(datetime.datetime.now())+'|'+'CHI2SCH'+'|'+str(duration_text)+ '|' + str(duration_secs)
#print C2S
req2=requests.get('https://maps.googleapis.com/maps/api/distancematrix/json?origins=42.057562,-88.041430&destinations=41.872293,-87.633294&departure_time=now&units=imperial&key=AIzaSyCVvUXJuWMS5ap0XC8oQK0XNaKFq3XtFXw')
resp2=req2.json()
duration_text2=resp2['rows'][0]['elements'][0]['duration_in_traffic']['text']
duration_secs2=resp2['rows'][0]['elements'][0]['duration_in_traffic']['value']
S2C=str(datetime.datetime.now())+'|'+'SCH2CHI'+'|'+str(duration_text2)+ '|' + str(duration_secs2)
#print S2C
f = open("/home/pavan01/chimove/traveltime", "a")
f.write(C2S+'\n'+S2C +'\n')
f.close()



