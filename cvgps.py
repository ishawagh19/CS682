import argparse
parser=argparse.ArgumentParser()
parser.add_argument('-u',type=int,required=True)
args = parser.parse_args()
print('Timestep',args.u)

TIMESTEP=args.u
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import json

import time
import datetime;


import numpy as np #   ---------foe array handling
#         ----------------for delay
import RPi.GPIO as GPIO#-----------for rpi gpio pin accsess
import glob#------------------------------for global v1iable declaration

global mes1#---------------mes v1iable loc

import serial
import utm
import pynmea2 
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent='samplecloud33@gmail.com')

port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)# ---define serial port gsm and gps
def parseGPS(s1):
    global mes1
    if s1.find('RMC') > 0:
        mes = pynmea2.parse(s1)
        
        
        latitude_1=int(mes.lat[0:2])
        latitude_2=float(mes.lat[2:9])
        latitude_2=latitude_2/60
        lat=latitude_1+latitude_2
        
        if int(mes.lon[0:1])==int(0):            
            lon1=int(mes.lon[0:3])
            lon2=float(mes.lon[3:11])
            lon2=lon2/60
            lon=lon1+lon2
        else:
            lon1=int(mes.lon[0:2])
            lon2=abs(float(mes.lon[2:10]))
            lon2=lon2/60
        lon=-1*(lon1+lon2)
        #print lat,lon
        v1=("%s,%s" % (lat,lon))  # Message
        print(v1)
        loc = geolocator.reverse(v1)
        mes1=(loc.address)
        mes1=str(mes1)
        
        print (mes1)
        scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
        ]
        credentials = ServiceAccountCredentials.from_json_keyfile_name("totemic-cursor-347317-609cc8849617.json", scopes) #access the json key you downloaded earlier 
        file = gspread.authorize(credentials) # authenticate the JSON key with gspread
        #print(file)
        sheet = file.open("gps")  #open sheet
        sheet = sheet.sheet1  #replace sheet_name with the name that corresponds to yours, e.g, it can be sheet1
        #all_cells = sheet.range('A1:C6')

        sheet.update_acell('F1', mes1)
        sheet.update_acell('C2',v1)
        ct = datetime.datetime.now()
        print("current time:-", ct)
        #ts = ct.timestamp()
        #print("timestamp:-", ts)


        sheet.update_acell('D1', str(ct))
       
mes1=''
from time import time, sleep 
while True:
    sleep(TIMESTEP - time() % TIMESTEP)#pause for 300 second
    try:
        s1 = (port.readline()).decode()
        parseGPS(s1)

        #time.sleep(TIMESTEP - time() % TIMESTEP)#pause for 300 second
    except:
        print('e')

#sheet.update_cell(2, 3, 'Blue') #updates row 2 on column 3

#Reference links for the above code:
#1] https://github.com/bnbe-club/rpi-dashcam-p2-diy-29/blob/master/e29-gps-test.py
#2] https://github.com/modmypi/GPS/blob/master/gps.py
#3] https://data-flair.training/blogs/read-data-from-google-sheets-using-python/
#4] https://www.makeuseof.com/tag/read-write-google-sheets-python/
#5] https://docs.python.org/3/library/argparse.html



