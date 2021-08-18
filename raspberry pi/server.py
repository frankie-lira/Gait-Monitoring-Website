#!/usr/bin/env python

# websocket server that sends data from sensor/arduino to client

import asyncio
import time
import websockets
import serial

# plug in sensor/arduino into raspberry pi before running this script
port='/dev/ttyACM0'
arduino = serial.Serial(port, 115200)

# function that sends data from arduino to client via websocket
async def senddata(websocket, path):
    while True:
        # wait for 0.1 sec then send all data collected in that time interval
        time.sleep(0.1)
        data = arduino.read(arduino.inWaiting()).decode("utf-8")

        await websocket.send(data)

# replace <rpi ip> with raspberry pi's ip address
# can change "5678" as long as the server and client scripts have same number
start_server = websockets.serve(senddata, "<rpi ip>", 5678)

# doesn't stop transferring data unless script stops running or websocket connection is lost
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
