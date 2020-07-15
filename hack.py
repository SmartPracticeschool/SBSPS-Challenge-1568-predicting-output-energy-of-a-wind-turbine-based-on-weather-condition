import time
import random
import sys
import ibmiotf.application
import ibmiotf.device

#Provide your IBM Watson Device Credentials
organization = "oxp93d" # repalce it with organization ID
deviceType = "Arduino" #replace it with device type
deviceId = "Wind_Speed" #repalce with device id
authMethod = "token"
authToken = "7RVC6DuS8_OaB_ROGH"#repalce with token
            
try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

deviceCli.connect()

while True:
        W=random.randint(1,72);
        #Send Temperature & Humidity to IBM Watson
        data = {'d':{ 'Wind_Speed' : W}}
        #print data
        def myOnPublishCallback():
            print ("Published Wind_speed = %s m/sec" % W,"to IBM Watson ")
        if(W>=40):
            print("The motor is ON")
            Energy=0.5*12470*1.23*(W*W*W)
            print("Energy=",Energy ,'Watts')
        else:
            print("The motor is OFF")

        success = deviceCli.publishEvent("event", "json", data, qos=0, on_publish=myOnPublishCallback)
        if not success:
            print("Not connected to IoTF")
        time.sleep(1)
        
# Disconnect the device and application from the cloud
deviceCli.disconnect()
