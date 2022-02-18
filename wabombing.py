#  Message Bombing
import pyautogui
import time

time.sleep(5)
i = 1

while True:
    if i == 51:
        print("Done!")
        break
    else:
        pyautogui.typewrite(f"{str(i)} Message Bombing Activate!!!")
        pyautogui.hotkey('enter')
        time.sleep(0.001)
        i += 1

