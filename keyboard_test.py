import keyboard
import time
import os
from os.path import expanduser

PWD = os.getcwd()
HOME_DIR = expanduser("~")
RIYOUSYA_LIST_KEYWORD = "riyousya_list"


def copy_and_paste():
    #コピペ操作
    keyboard.press_and_release('windows+e')
    time.sleep(5)
    keyboard.press_and_release('ctrl+l, backspace')
    time.sleep(5)
    keyboard.write(HOME_DIR+"\Downloads")
    keyboard.press_and_release('enter')
    time.sleep(5)
    keyboard.press_and_release('ctrl+l')
    keyboard.press_and_release('tab')
    time.sleep(5)
    keyboard.write(RIYOUSYA_LIST_KEYWORD)
    time.sleep(5)
    keyboard.press_and_release('enter')
    time.sleep(5)
    keyboard.press_and_release('tab,down,up')
    #利用者一括ファイルのコピー
    keyboard.press_and_release('ctrl+c')
    keyboard.press_and_release('ctrl+l, backspace')
    time.sleep(5)
    keyboard.write(PWD+"\work")
    keyboard.press_and_release('enter')
    time.sleep(5)
    keyboard.press_and_release('ctrl+l')
    time.sleep(5)
    keyboard.press_and_release('tab')
    time.sleep(3)
    keyboard.press_and_release('tab')
    time.sleep(3)
    keyboard.press_and_release('tab')
    time.sleep(3)
    keyboard.press_and_release('ctrl+v')

if __name__ == '__main__':
    copy_and_paste()