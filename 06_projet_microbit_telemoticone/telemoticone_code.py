import radio
from microbit import *

radio.on()

images = [Image.HEART,Image.HAPPY,Image.SMILE,Image.SAD,Image.CONFUSED,Image.ANGRY,Image.ASLEEP,Image.SURPRISED]

index = 0
display.show(images[0])

while True:
    if button_a.was_pressed():
        index += 1
        if index == len(images):
            index = 0
        display.show(images[index])


    if button_b.is_pressed():
        radio.send(str(index))

    incoming = radio.receive()
    if incoming:
        display.show(images[int(incoming)])
        sleep(500)
    display.show(images[index])

