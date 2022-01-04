#!/usr/bin/env python3

import pywhatkit
import pyautogui as pg
import os
import sys
import time

def send_message(number):
    os.environ["DISPLAY"] = ":0"
    pywhatkit.sendwhatmsg_instantly(number, "Good Morning!", 60, False)
    pg.press("tab")
    pg.press("tab")
    pg.press("tab")
    pg.press("tab")
    pg.press("tab")
    pg.press("tab")
    pg.press("enter")
    time.sleep(60) # Sleep for 1 minute
    pg.hotkey("ctrl", "w") # close the tab



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: ./send_gm.py <Whatsapp Mobile Number")
        exit(-1)
    send_message(sys.argv[1].strip())

