from machine import Pin, SoftI2C, Pin, Timer, sleep
import time
import ssd1306
from utime import ticks_diff, ticks_us
from machine import PWM
from time import sleep_ms

buzzer_pin = Pin(18, Pin.OUT)
buzzer_pwm = PWM(buzzer_pin, freq=882, duty=900)

i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

juli = None
trig = Pin(15, Pin.OUT)
echo = Pin(2, Pin.IN)
trig.value(0)
echo.value(0)

def measure():
    global juli
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)

    while echo.value() == 0:
        t1 = time.ticks_us()
    while echo.value() == 1:
        t2 = time.ticks_us()
    print("---------------------")
    print(t1)
    print(t2)
    t3 = time.ticks_diff(t2, t1) / 10000
    print(t3, t2-t1)
    time.sleep(0.1)
    juli = t3 * 340 / 2
    return juli

def display_distance(distance):
    oled.fill(0)  # 清空屏幕
    oled.text("Distance:", 0, 0)  # 在 (0, 0) 位置显示文本
    oled.text("{:.2f} cm".format(distance), 0, 16)  # 在 (0, 16) 位置显示距离值
    oled.show()  # 更新屏幕显示

try:
    while True:
        measure()
        display_distance(juli)
        if juli is not None and juli > 350:
            pass

        elif juli is not None and 300 < juli < 350:
            buzz_freq = 441
            buzzer_pwm = PWM(buzzer_pin, freq=buzz_freq, duty=900)
            sleep_ms(500)
            buzzer_pwm = PWM(buzzer_pin, duty=0)
            sleep_ms(1000)

        elif juli is not None and 250 < juli < 300:
            buzz_freq = 556
            buzzer_pwm = PWM(buzzer_pin, freq=buzz_freq, duty=900)
            sleep_ms(500)
            buzzer_pwm = PWM(buzzer_pin, duty=0)
            sleep_ms(1000)

        elif juli is not None and 200 < juli < 250:
            buzz_freq = 833
            buzzer_pwm = PWM(buzzer_pin, freq=buzz_freq, duty=900)
            sleep_ms(500)
            buzzer_pwm = PWM(buzzer_pin, duty=0)
            sleep_ms(1000)

        elif juli is not None and 150 < juli < 200:
            buzz_freq = 882
            buzzer_pwm = PWM(buzzer_pin, freq=buzz_freq, duty=900)
            sleep_ms(500)
            buzzer_pwm = PWM(buzzer_pin, duty=0)
            sleep_ms(1000)

        elif juli is not None and 100 < juli < 150:
            buzz_freq = 990
            buzzer_pwm = PWM(buzzer_pin, freq=buzz_freq, duty=900)
            sleep_ms(500)
            buzzer_pwm = PWM(buzzer_pin, duty=0)
            sleep_ms(1000)

        elif juli is not None and 50 < juli < 100:
            buzz_freq = 1112
            buzzer_pwm = PWM(buzzer_pin, freq=buzz_freq, duty=900)
            sleep_ms(500)
            buzzer_pwm = PWM(buzzer_pin, duty=0)
            sleep_ms(1000)

        elif juli is not None and 5 < juli < 50:
            buzz_freq = 1178
            buzzer_pwm = PWM(buzzer_pin, freq=buzz_freq, duty=900)
            sleep_ms(500)
            buzzer_pwm = PWM(buzzer_pin, duty=0)
            sleep_ms(1000)

        elif juli is not None and 1 < juli < 5:
            buzz_freq = 1178
            buzzer_pwm = PWM(buzzer_pin, freq=buzz_freq, duty=900)
            sleep_ms(500)
            buzzer_pwm = PWM(buzzer_pin, duty=0)
            sleep_ms(100)

        elif juli is not None and 0.2 < juli < 1:
            buzz_freq = 1178
            buzzer_pwm = PWM(buzzer_pin, freq=buzz_freq, duty=900)
            sleep_ms(400)
            buzzer_pwm = PWM(buzzer_pin, duty=0)
            sleep_ms(80)

        elif juli is not None and 0 < juli < 0.2:
            buzz_freq = 1322
            buzzer_pwm = PWM(buzzer_pin, freq=buzz_freq, duty=900)
            sleep_ms(300)
            buzzer_pwm = PWM(buzzer_pin, duty=0)
            sleep_ms(50)

        elif juli is not None and juli == 0:
            buzz_freq = 1322
            buzzer_pwm = PWM(buzzer_pin, freq=buzz_freq, duty=900)
            sleep_ms(10)
            buzzer_pwm = PWM(buzzer_pin, duty=0)
            sleep_ms(10)
            time.sleep(0.2)

except KeyboardInterrupt:
    pass