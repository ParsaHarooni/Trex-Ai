import time

from PIL import ImageGrab, ImageOps
import pyautogui
from numpy import *


class Cordinates:
    replay = (340, 390)
    dino = (169, 396)
    # change to your own pixels | you can get it via photoshop or other image editing tools


def restart_game():
    pyautogui.click(Cordinates.replay[0], Cordinates.replay[1])


def pressSpace():
    pyautogui.keyDown("space")
    print("Jumped")
    time.sleep(0.1)
    pyautogui.keyUp("space")


def image_grab():
    box = (Cordinates.dino[0] + 40, Cordinates.dino[1], Cordinates.dino[0] + 135, Cordinates.dino[1] + 30)
    image = ImageGrab.grab(box)
    gray_image = ImageOps.grayscale(image)
    a = array(gray_image.getcolors())
    print("Color: ", a.sum())
    return a.sum()


restart_game()
time.sleep(0.3)
jump_color = image_grab()
while True:

    if image_grab() != jump_color:
        pressSpace()
