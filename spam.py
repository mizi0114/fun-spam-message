import time
import pyautogui

time.sleep(0)
f = open("spam.txt")

for line in f:
    pyautogui.typewrite(line)
    pyautogui.press('enter')



