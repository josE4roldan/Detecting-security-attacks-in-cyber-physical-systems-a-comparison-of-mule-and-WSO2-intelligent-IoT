import paho.mqtt.client as mqtt
import pandas as pd
import numpy as np
from time import time
from time import sleep
import json

# Load all the CSV files
df_normal=pd.read_csv("data/MQTT_normal.csv",error_bad_lines=False)
df_normal_pred=pd.read_csv("data/MQTT_normal_pred.csv",error_bad_lines=False)
df_tcp=pd.read_csv("data/TCP_SYN-Events.csv",error_bad_lines=False)
df_udp=pd.read_csv("data/UDP_Port_Scan-Events.csv",error_bad_lines=False)
df_disc=pd.read_csv("data/MQTT_discwave-Events.csv",error_bad_lines=False)
df_disc_pred=pd.read_csv("data/MQTT_discwave_linealreg-Events.csv",error_bad_lines=False)
df_dos=pd.read_csv("data/MQTT_dos-Events.csv",error_bad_lines=False)
df_dos_pred=pd.read_csv("data/MQTT_dos_linealreg-Events.csv",error_bad_lines=False)

#Fill empty (NA) fields
df_normal.fillna("''",inplace=True)
df_tcp.fillna("''",inplace=True)
df_udp.fillna("''",inplace=True)
df_disc.fillna("''",inplace=True)
df_dos.fillna("''",inplace=True)

#Paho connect callback
def on_connect(client, userdata, flags, rc):
	print("Connected with the result code " + str(rc))

#Prepares the packet for sending
def to_dictionary(d):
    newd={}
    for key, value in d.items():
        if key == "delay":
            continue
        else:
            if type(value) is np.int64:
                newd[key]=int(value)
            elif key=="id":
                newd[key]=int(value)
            else:
                newd[key]=value
    return newd
# connect to the broker
client = mqtt.Client()
client.on_connect = on_connect
client.connect("127.0.0.1", 1883, 60) # the ip must be changed!!
print("Connect: "+str(time()))

for i in range(0,df_disc.shape[0]): #if we want send the full discwave attack with prediction
    d=to_dictionary(df_disc.iloc[i])
    client.publish("NetworkPacket", json.dumps(d))
    #sleep(0.0001) # a small delay may be necessary if the prediction packets are ahead of the network packets.
    a=to_dictionary(df_disc_pred.iloc[i])
    client.publish("NetworkPrediction", json.dumps(a))
    sleep(df_normal.iloc[i]['delay']/1000000)
"""
for i in range(0,df_tcp.shape[0]): # if we want to send the complete trace without prediction
    d=to_dictionary(df_tcp.iloc[i])
    client.publish("NetworkPacket", json.dumps(d))
    sleep(df_tcp.iloc[i]['delay']/1000000)
"""