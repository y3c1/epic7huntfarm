from ppadb.client import Client
from PIL import Image
import numpy as np
import time
#try again [828][1252]  [229, 218, 204, 255]
#start [854][1371] [28, 89, 15, 255]
#stage clear [300][645] [235, 209, 140, 255]
#confirm [850][1450] [37, 112, 17, 255]

def checkStatus():
    image = device.screencap()
    with open('screen.png','wb') as f:
        f.write(image)
    image = Image.open('screen.png')
    image = np.array(image, dtype=np.uint8)
    factor = 0.1
    if sum([235, 209, 140, 255]) - factor* sum(list(image[300][645])) <= sum(list(image[300][645])) <= sum([235, 209, 140, 255]) + factor* sum(list(image[300][645])):
        device.shell("input touchscreen tap 645 300")
        time.sleep(1)
        device.shell("input touchscreen tap 645 300")
        print("stage clear")
    elif sum([37, 112, 17, 255]) - factor* sum(list(image[850][1450])) <= sum(list(image[850][1450])) <= sum([37, 112, 17, 255]) + factor* sum(list(image[850][1450])):
        device.shell("input touchscreen tap 1450 850")
        time.sleep(1)
        device.shell("input touchscreen tap 1450 850")
        print("confirm")
    elif sum([229, 218, 204, 255]) - factor* sum(list(image[828][1252])) <= sum(list(image[828][1252])) <= sum([229, 218, 204, 255]) + factor* sum(list(image[828][1252])):
        device.shell("input touchscreen tap 1252 828")
        time.sleep(1)
        device.shell("input touchscreen tap 1252 828")
        print("try again")
    elif sum([20, 75, 15, 255]) - factor* sum(list(image[850][1471])) <= sum(list(image[850][1471])) <= sum([20, 75, 15, 255]) + factor* sum(list(image[850][1471])):
        device.shell("input touchscreen tap 1471 854")
        time.sleep(1)
        device.shell("input touchscreen tap 1471 854")
        print("start")
    elif sum([134, 134, 134, 255]) - factor* sum(list(image[444][740])) <= sum(list(image[444][740])) <= sum([134, 134, 134, 255]) + factor* sum(list(image[444][740])):
        device.shell("input touchscreen tap 740 444")
        time.sleep(1)
        device.shell("input touchscreen tap 239 206")
        time.sleep(1)
        device.shell("input touchscreen tap 1340 214")
        time.sleep(1)
        device.shell("input touchscreen tap 239 206")
        time.sleep(1)
        device.shell("input touchscreen tap 1340 750")
        time.sleep(1)
        device.shell("input touchscreen tap 475 200")
        time.sleep(1)
        device.shell("input touchscreen tap 923 635")
        time.sleep(1)
        device.shell("input touchscreen tap 1530 620")
        time.sleep(1)
        device.shell("input touchscreen tap 1252 828")
        time.sleep(1)
        device.shell("input touchscreen swipe 1100 170 1100 850")
        time.sleep(1)
        device.shell("input touchscreen swipe 1100 170 1100 850")
        time.sleep(1)
        device.shell("input touchscreen tap 1450 828")
    else:
        print("clearing")
        #device.shell("input touchscreen tap 800 450")


client = Client(host="127.0.0.1", port=5037)
devices = client.devices()
if len(devices) == 0:
    print("No Devices Connected")

device = devices[0]

while True:
    checkStatus()
    time.sleep(2)


    