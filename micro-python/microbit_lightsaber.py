from microbit import *
from neopixel import NeoPixel
# import music
import random

num_pixels = 50
foreground = [0xff, 0x00, 0x00]  # Hex color - red, green and blue
background = [0x10, 0x10, 0x10]
red = 0xf0
green = 0x00
blue = 0x00

ring = NeoPixel(pin2, num_pixels)
ring.clear()
data = []


def build_ranbow():
    #data.clear()
    for i in range(0, num_pixels):
        red, green, blue = 0, 0, 0
        shift = int(((i * 16) / num_pixels))
        if shift == 0:
            red = 0xff
        if shift > 0 and shift < 8:
            red = 0xff >> shift
            green = ((0xff << shift) >> 8) & 0xff
        if shift == 8:
            green = 0xff
        if shift > 8 and shift < 16:
            green = 0xff >> (shift - 8)
            blue = ((0xff << (shift-8)) >> 8) & 0xff
        if shift == 16:
            blue = 0xff
        # data.append([red, green, blue])
        data[i] = [red, green, blue]


def build_red():
    data.clear()
    for i in range(0, num_pixels):
        data.append([0xff-(num_pixels-i)*2, 0x0, 0x0])


def build_green():
    data.clear()
    for i in range(0, num_pixels):
        data.append([0x00, 0xff-(num_pixels-i)*2, 0x0])


def build_pink():
    data.clear()
    for i in range(0, num_pixels):
        data.append([0xff, 0xc0, 0xcb])
"""
def sound_effect_up():
    for i in range(0, num_pixels):
        music.pitch(random.randint(i*20,1000+i*2),wait=False)
        # sleep(1)
def sound_effect_down():
    for i in range(num_pixels, 0, -1):
        music.pitch(random.randint(i*20,1000+i*2),wait=False)
        # sleep(1)
    
def sound_effect1():
    sound_effect_up()
    sound_effect_down()
    sound_effect_up()
    sound_effect_up()
    sound_effect_down()
    sound_effect_down()
    sound_effect_up()
    sound_effect_up()
    sound_effect_up()
    sound_effect_down()
    sound_effect_down()
    sound_effect_down()
    sound_effect_up()
    sound_effect_up()
    sound_effect_up()
    sound_effect_up()
    sound_effect_down()
    sound_effect_down()
    sound_effect_down()
    sound_effect_down()
    music.pitch(0, 1)
"""


up_down = 1
status = 1
build_red()
display.show(str(status))
glitter_timer_counter = random.randint(1000, 2000)
glitter_position = random.randint(0, 49)
wave_timer_counter = 3
while True:
    if up_down == 2:
        glitter_timer_counter = glitter_timer_counter - 1
        if glitter_timer_counter == 10:
            glitter_position = random.randint(0, 49)
            ring[glitter_position] = [0xff, 0xff, 0xff]
            ring.show()
        if glitter_timer_counter < 10:
            ring[glitter_position] = [0xff, 0xff, 0xff]
            ring.show()
        if glitter_timer_counter == 0:
            glitter_timer_counter = random.randint(1000, 2000)
#            for i in range(0, num_pixels):
#                ring[i] = data[i]
#            ring.show()
        wave_timer_counter = wave_timer_counter - 1
        if wave_timer_counter == 0:
            wave_timer_counter = random.randint(1, 10)
            tmp = data.pop(-1)
            data.insert(0,tmp)
            for i in range(0, num_pixels):
                ring[i] = data[i]
            ring.show()
        
    if button_b.was_pressed():
        for i in range(num_pixels, 0, -1):
            ring[i-1] = [0x0, 0x0, 0x0]
            ring.show()
#            music.pitch(random.randint(1000+i*50,1000+i*100),80,wait=False)
            sleep(2)
        up_down = 1
#        music.pitch(0, 100)
        if status == 1:
            build_green()
            status = 2
        elif status == 2:
            build_pink()
            status = 3
        elif status == 3:
            build_ranbow()
            status = 4
        elif status == 4:
            status = 5
        elif status == 5:
            for i in range(num_pixels, 0, -1):
                ring[i-1] = [0x0, 0x0, 0x0]
                ring.show()
#                music.pitch(random.randint(500,500+(20*i)))
                sleep(3)
            up_down = 1
#            music.pitch(0, 100)
            build_red()
            status = 1
        else:
            status = 1
        display.show(str(status))
        sleep(200)

    if button_a.is_pressed():
        if up_down == 1:
            # music.reset()
            for i in range(0, num_pixels):
                ring[i] = data[i]
                ring.show()
#                music.pitch(random.randint(1000+i*50,1000+i*100),40,wait=False)
                sleep(1)
            up_down = 2
#            music.pitch(0, 100)
        else:
            for i in range(num_pixels, 0, -1):
                ring[i-1] = [0x0, 0x0, 0x0]
                ring.show()
#                music.pitch(random.randint(1000+i*50,1000+i*100),80,wait=False)
                sleep(2)
            up_down = 1
#            music.pitch(0, 100)
        sleep(200)

    if status == 5:
        for i in range(0, num_pixels):
            for j in range(0, len(data[i:])):
                ring[j] = data[j+i]
            for j in range(0, len(data[:i])):
                ring[num_pixels-i+j] = data[j]
            ring.show()
            
"""
        music.pitch(random.randint(50, 60),wait=False)
        if accelerometer.was_gesture("shake"):
            for i in range(0, num_pixels):
                music.pitch(random.randint(3000+i*50,3000+i*100),10,wait=False)
                sleep(1)
        if accelerometer.was_gesture("up") or accelerometer.was_gesture("down") or accelerometer.was_gesture("left") or accelerometer.was_gesture("right"):
            sound_effect1()
        if accelerometer.was_gesture("face up") or accelerometer.was_gesture("face down"):
            sound_effect1()
"""
