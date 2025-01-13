from lib_AHTx0 import SensorAHTx0
from smbus2 import SMBus

bus_number = 1
i2c = SMBus(bus_number)
sensor = SensorAHTx0(i2c)
temperature, humidity = sensor.measure()
if temperature is not None and humidity is not None:
    print(f"Temperature: {temperature:.2f} °C, Humidity: {humidity:.2f} %")