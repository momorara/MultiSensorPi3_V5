#!/usr/bin/env python3
"""
2026/09/30  iR信号を受信して、32ビット分複合化して表示　ファィル保存
            ファィルは　iR_code.txt　

"""

from gpiozero import DigitalInputDevice
import time

GPIO_PIN = 4
MAX_BITS = 100

ir = DigitalInputDevice(
    GPIO_PIN,
    pull_up=True
)
print("GPIO4 赤外線リモコン受信")
print("リモコンのボタンを1回押してください")
print()

try:
    while True:

        # ==================================
        # 信号が来るまで待つ
        # ==================================

        while ir.value == 1:
            time.sleep(0.0001)
        # LOWになったので測定開始
        last_time = time.monotonic()
        last_level = ir.value
        pulses = []


        # ==================================
        # 最大100ビット分のデータを取得
        # ==================================

        while len(pulses) < MAX_BITS * 2:
            level = ir.value
            if level != last_level:
                now = time.monotonic()
                duration = (now - last_time) * 1000000
                # 20ms以上の空白なら終了
                if duration > 20000:
                    break
                # パルスを保存
                pulses.append(duration)
                last_time = now
                last_level = level
            # 信号が20ms以上変化しなければ終了
            if (time.monotonic() - last_time) > 0.020:
                break
            time.sleep(0.00001)


        # ==================================
        # 受信パルスが少なければノイズとして無視
        # ==================================

        if len(pulses) < 20:
            continue
        print()
        print("受信開始")
        print("取得パルス数:", len(pulses))
        print()


        # ==================================
        # パルス表示
        # ==================================

        for i, p in enumerate(pulses):
            print(f"{i:3d}: {p:7.0f} us")


        # ==================================
        # ヘッダーを探す
        # ==================================

        start_index = -1
        for i in range(len(pulses) - 1):
            # 約9ms + 約4.5ms
            if (8000 <= pulses[i] <= 10000 and 3500 <= pulses[i + 1] <= 5500):
                start_index = i + 2
                break
        if start_index < 0:
            print()
            print("ヘッダーが見つかりません")
            print()
            continue
        print()
        print("データ開始位置:",start_index)


        # ==================================
        # 2パルス = 1ビットとして復号
        # ==================================

        bits = ""
        i = start_index
        while (i + 1 < len(pulses) and len(bits) < MAX_BITS ):
            p1 = pulses[i]
            p2 = pulses[i + 1]
            # 1個目は約560us
            if 400 <= p1 <= 800:
                # 560 + 560 → 0
                if 400 <= p2 <= 800:
                    bits += "0"
                # 560 + 1680 → 1
                elif 1300 <= p2 <= 1900:
                    bits += "1"
                i += 2
            else:
                i += 1


        # ==================================
        # 結果
        # ==================================

        print()
        print("================================")
        print("復号したビット列")
        print("================================")

        print(bits)
        with open("/home/pi/sensorHAT/" + 'iR_code.txt', mode='w') as f: #上書き
            f.write(bits)
            
        print()
        print("ビット数:", len(bits))

        print("================================")
        print()

        if bits:
            print("8ビット単位:")
            for i in range(0,len(bits),8):
                print(bits[i:i + 8],end=" ")
            print()
            print()
        print("次のボタンを押してください")
        print()


except KeyboardInterrupt:
    print("\n終了")
finally:
    ir.close()