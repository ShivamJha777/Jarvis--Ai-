from time import sleep
from pynput.keyboard import Key,Controller
keyboard = Controller()
def volumeup(percentage):
    number_of_times = percentage/2
    number_of_times = int(number_of_times)
    for i in range(number_of_times):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.1)
def volumedown(percentage):
    number_of_times = percentage/2
    number_of_times = int(number_of_times)
    for i in range(number_of_times):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        sleep(0.1)
