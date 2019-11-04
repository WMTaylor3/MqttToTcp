import time
import paho.mqtt.client as mqtt # https://github.com/eclipse/paho.mqtt.python

# OnMqttConnect function.
#   mqttClient - The client created below.  
#   userData - Ignore the userData parameter, you can read more about it in the docs but for this use I don't think we need it...
#   flags - Response flags sent by the MQTT broker. Don't really need them here...
#   rc - The MQTT connection result. Pretty generic MQTT stuff. 0 = Success etc.
def OnMqttConnect(mqttClient, userData, flags, rc):
    if rc == 0:
        mqttClient.subscribe(mqtt_subscribeTopic)
        print("Connection to MQTT broker successful")
        global isMqttConnected
        isMqttConnected = True
    else:
        print("Connection to MQTT broker unsuccessful")

# OnMqttDisconnect function.
#   mqttClient - The client created below.  
#   userData - Ignore the userData parameter, you can read more about it in the docs but for this use I don't think we need it...
#   rc - The MQTT connection result. Pretty generic MQTT stuff. 0 = Success etc.
def OnMqttDisconnect(mqttClient, userData, rc):
    if rc != 0:
        print("Unexpected disconnection from the MQTT broker.")
        global isMqttConnected
        isMqttConnected = False

# OnMqttMessage callback function.
# Parameters:
#   mqttClient - The client created below.  
#   userData - Ignore the userData parameter, you can read more about it in the docs but for this use I don't think we need it...
#   message - The message returned from the MQTT broker. Object of class MQTTMessage, also listed in the docs but follows the below structure:
#       topic : String/bytes. topic that the message was published on.
#       payload : String/bytes the message payload. NOTE: This is not a string, this is a Bytes. Hence the decode (UTF-8 assumed here but change if it doesn't work.)
#       qos : Integer. The message Quality of Service 0, 1 or 2.
#       retain : Boolean. If true, the message is a retained message and not fresh.
#       mid : Integer. The message id.
def OnMqttMessage(mqttClient, userData, message):
    print("Recieved message.")
    print("Topic: " + message.topic)
    print("Payload: " + message.payload.decode("utf-8"))
    ### Handle TCP here by calling some other method yet to be implemented.

# MQTT connection status.
isMqttConnected = False             # Boolean

# MQTT configuration variables.
mqtt_brokerAddress = "10.11.12.12"  # String
mqtt_brokerPort = 1883              # Number
mqtt_username = "william"           # String
mqtt_password = "william"           # String
mqtt_clientIdentifier = "IRBlaster" # String
mqtt_subscribeTopic = "ir/blaster"  # String

# Initial MQTT client setup.
print("Configuring MQTT client...")
mqttClient = mqtt.Client(mqtt_clientIdentifier)
mqttClient.username_pw_set(mqtt_username, password=mqtt_password)
mqttClient.on_connect= OnMqttConnect
mqttClient._on_disconnect= OnMqttDisconnect
mqttClient.on_message= OnMqttMessage
print("Configuration Complete.")

# Connect MQTT Client to broker.
print("Establishing initial connection to MQTT broker...")
mqttClient.connect(mqtt_brokerAddress, port=mqtt_brokerPort)
mqttClient.loop_start()
while not isMqttConnected:
    print("Connecting ...")
    time.sleep(0.1) # Blocking but shouldn't be too bad.
print("Connection Complete.")

# Main program.
# Not much to it as any new message gets handled automatically but the OnMqttMessage callback function.
# End with Ctrl + C.
try:
    while True:
        time.sleep(1)
        while not isMqttConnected:
            print("Reconnecting ...")
            time.sleep(0.1) # Blocking but shouldn't be too bad.

except KeyboardInterrupt:
    print("Interupt detected. Ending script")
    mqttClient.disconnect()
    mqttClient.loop_stop()

