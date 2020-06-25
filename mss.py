from ppadb.client import Client
import time
import mss
from PIL import Image
import numpy as np

#stage clear coords {"top": 420, "left": -1100, "width": 70, "height": 90} ok
#confirm {"top": 1020, "left": -490, "width": 190, "height": 70} ok
#try again monitor = {"top": 1020, "left": -450, "width": 155, "height": 75} ok
#start {"top": 1020, "left": -500, "width": 210, "height": 60} ok

client = Client(host="127.0.0.1", port=5037)
devices = client.devices()
if len(devices) == 0:
    print("No Devices Connected")

device = devices[0]

monitor = {"top": 1020, "left": -450, "width": 155, "height": 75}
with mss.mss() as sct:
    image = sct.grab(monitor)
    output = "temp.png".format(**monitor)
    mss.tools.to_png(image.rgb, image.size, output=output)


    image = Image.open("temp.png")
    image = np.array(image, dtype=np.uint8)

    tryagain = Image.open("tryagain.png")
    tryagain = np.array(tryagain, dtype=np.uint8)

    print((image==tryagain).all())

    

    