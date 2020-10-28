import time
import requests
import unicornhat as uh

uh.set_layout(uh.PHAT)
uh.brightness(0.5)
uh.rotation(180)
width,height = uh.get_shape()


rgb_list = []
color = 0

while True:
    try:
        cheer = requests.get("http://api.thingspeak.com/channels/1417/field/2/last.json").json()
    except:
        pass

    cheer = cheer['field2'].strip('#')

    if cheer != color:
        for i in range(0, 5, +2):
            value = int(cheer[i:i + 2], 16)
            rgb_list.append(value)

        for y in range(height):
            for x in range(width):
                uh.set_pixel(x, y, rgb_list[0], rgb_list[1], rgb_list[2])
		uh.show()
		time.sleep(0.05)

        color = cheer
        rgb_list = []

    time.sleep(16)
