#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
HY-SRF05超音波距離センサモジュールを使い、距離を測定します。

0.5秒毎に10回計測して、表示

計測距離はmax 100cmが標準だが、3メーターにしている

by.kawabata

2024/03/09  
2024/03/10  max=3M
'''


from gpiozero import DistanceSensor
from time import sleep


def main():
    sensor = DistanceSensor(echo=23, trigger=24, max_distance=3)
    for i in range(10):
        dist = int(sensor.distance * 100 * 10) / 10
        print('Distance: ', dist,"cm")
        sleep(0.5)
    print("最終距離",int(sensor.distance * 100 * 10) / 10,"cm")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("key入力がありましたので、プログラム停止" )
    except ValueError as e:
        print(e)
