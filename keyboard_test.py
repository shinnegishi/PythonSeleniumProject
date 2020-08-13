import keyboard
import time

from os.path import expanduser

PWD = os.getcwd()
HOME_DIR = expanduser("~")
RIYOUSYA_LIST_KEYWORD = "riyousha_list"


def copy_and_paste():
    #コピペ操作
    keyboard.press_and_release('wondows+e, ctrl+l, backspace')
    time.sleep(5)
    keyboard.write(HOME_DIR+"\Downloads")
    keyboard.press_and_release('enter')
    time.sleep(5)
    keyboard.press_and_release('tab')
    keyboard.write(RIYOUSYA_LIST_KEYWORD)
    keyboard.press_and_release('enter')
    time.sleep(5)
    keyboard.press_and_release('tab,tab')
    keyboard.press_and_release('ctrl+c')
    keyboard.press_and_release('ctrl+l, backspace')
    time.sleep(5)
    keyboard.write(PWD+"\work")
    keyboard.press_and_release('enter')
    keyboard.press_and_release('tab,tab')
    time.sleep(5)
    keyboard.press_and_release('ctrl+v')
    print("Finished!!!")

if __name__ == '__main__':
    copy_and_paste()