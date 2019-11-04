import time
import paho.mqtt.client as mqtt

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
print("Configuring MQTT Client...")
print("Configuring MQTT Client...")
# mqttClient = mqtt.Client(mqtt_clientIdentifier)
# mqttClient.username_pw_set(mqtt_username, password=mqtt_password)
# mqttClient.on_connect= OnMqttConnect
# mqttClient._on_disconnect= OnMqttDisconnect
# mqttClient.on_message= OnMqttMessage

# # Connect MQTT Client to broker.
# mqttClient.connect(mqtt_brokerAddress, port=mqtt_brokerPort)
# mqttClient.loop_start()
# while not isMqttConnected:
#     time.sleep(0.1) # Blocking but shouldn't be too bad.
# mqttClient.subscribe(mqtt_subscribeTopic)

