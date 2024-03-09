#!/usr/bin/python

"""
###########################################################################
Cdsの状態を確認する。

#Filename      :test_sw.py

#Update        :2019/11/02
2023/9/22   タクトスイッチ　ソフトプルダウンとする。
2024/02/27  pi5のためgpiozeroに置き換え
############################################################################
"""
from gpiozero import Button
import time

Cds = Button(21,pull_up=False)


#print message at the begining ---custom function
def print_message():
    print ('|********************************|')
    print ('|   Cds 監視　　　　　           |')
    print ('|********************************|\n')
    print ('Program is running...')
    print ('Please press Ctrl+C to end the program...')


#read SW_PI_1's level
def ReadSW_1():
    if Cds.is_pressed:
        sw_ = 'on'
    else:
        sw_ = 'off'
    return sw_


#main function
def main():
    print("stop to 'Ctrl+C' is pressed")
    loop_n = 0
    #print info
    sw_ = 'off'
    print_message()
    while True:
        sw_ = ReadSW_1()
        if sw_ =='off':
            print('dark')
        else:
            print('bright')
        time.sleep(1)
    pass

#
# if run this script directly ,do:
if __name__ == '__main__':
    try:
            main()
    #when 'Ctrl+C' is pressed,child program destroy() will be executed.
    except KeyboardInterrupt:
        pass
    except ValueError as e:
        print(e)

   
