"""
 2023/10/28
    リモコンの赤外線を感知すると反応します
2024/02/27  pi5のためgpiozeroに置き換え
"""

from gpiozero import Button
import time

iR = Button(4)

#read SW_PI_1's level
def ReadSW_1():
    if iR.is_pressed:
        sw_ = 'on'
    else:
        sw_ = 'off'
    return sw_

def main():
    print("赤外線を感知したら反応します。")
    print("stop to 'Ctrl+C' is pressed")
    sw_ago = "on"
    while True:
        sw_ = ReadSW_1()
        if sw_ago != sw_ :
            if sw_ == "on" :
                print("受信")
                time.sleep(1)
            sw_ago = sw_
        time.sleep(0.01)


# if run this script directly ,do:
if __name__ == '__main__':
    try:
        main()
    #when 'Ctrl+C' is pressed,child program destroy() will be executed.
    except KeyboardInterrupt:
        pass
    except ValueError as e:
        print(e)
