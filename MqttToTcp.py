import time
import paho.mqtt.client as mqtt # https://github.com/eclipse/paho.mqtt.python

# MQTT configuration variables.
mqtt_brokerAddress = "10.11.12.12"  # String
mqtt_brokerPort = 1883              # Number
mqtt_username = "william"           # String
mqtt_password = "william"           # String
mqtt_clientIdentifier = "IRBlaster" # String
mqtt_subscribeTopic = "ir/blaster"  # String

# MQTT connection status.
isMqttConnected = False             # Boolean

# Initial MQTT client setup.
print("Configuring MQTT client...")
mqttClient = mqtt.Client(mqtt_clientIdentifier)
mqttClient.username_pw_set(mqtt_username, password=mqtt_password)
mqttClient.on_connect= OnMqttConnect
mqttClient._on_disconnect= OnMqttDisconnect
mqttClient.on_message= OnMqttMessage

# Connect MQTT Client to broker.
print("Establishing connection to MQTT broker...")
mqttClient.connect(mqtt_brokerAddress, port=mqtt_brokerPort)
mqttClient.loop_start()

while not isMqttConnected:
    print(".", end = '')
    time.sleep(0.1) # Blocking but shouldn't be too bad.

mqttClient.subscribe(mqtt_subscribeTopic)

# OnMqttMessage callback function.
# Parameters:
#   mqttClient - The client created above.  
#   userData - Ignore the userData parameter, you can read more about it in the docs but for this use I don't think we need it...
#   message - The message returned from the MQTT broker. Object of class MQTTMessage, also listed in the docs but follows the below structure:
#       topic : String/bytes. topic that the message was published on.
#       payload : String/bytes the message payload.
#       qos : Integer. The message Quality of Service 0, 1 or 2.
#       retain : Boolean. If true, the message is a retained message and not fresh.
#       mid : Integer. The message id.
def OnMqttMessage(mqttClient, userData, message)

# Main program.
# Not much to it as any new message gets handled automatically but the OnMqttMessage callback function.
# End with any keypress.
try:
    while True:
        time.sleep(1)

except KeyboardInterupt:
    print("Interupt detected. Ending script")
    mqttClient.disconnect()
    mqttClient.loop_stop()

