import time
import network
import socket
from machine import Pin

led = Pin("LED", Pin.OUT)
led.value(0)  # LED Off initially

ssid = 'ShadowVPN'
password = '123Sd456!'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

# Function to test a TCP connection
def test_tcp_connection(ip, port=22):
    print(f"Attempting to connect to {ip} on port {port}...")
    led.value(1)  # LED On
    time.sleep(0.1)
    led.value(0)  # LED Off
    time.sleep(0.1)
    
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((ip, port))
        s.close()
        print(f"Connected to {ip} on port {port}!")
        return True
    except:
        print(f"Failed to connect to {ip} on port {port}.")
        return False

# Wait for connect or fail
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('Waiting for connection...')
    time.sleep(1)

# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('Network connection failed')
else:
    print('Connected to ' + ssid)
    status = wlan.ifconfig()
    print('Device IP: ' + status[0])
    
    # Blink LED 3 times to indicate WiFi connection
    for _ in range(3):
        led.value(1)
        time.sleep(0.2)
        led.value(0)
        time.sleep(0.2)

    # Main loop
    while True:
        time.sleep(120)  # Sleep for 2 minutes
        
        # Test connections for 1 minute
        end_time = time.time() + 60
        while time.time() < end_time:
            test_tcp_connection('server_ip1')
            test_tcp_connection('server_ip2')
