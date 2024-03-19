import ctypes
import random
import os
def wallpaper_changer(folder):
    try:
        wallpaper_file = [file for file in os.listdir(folder) if file.lower().endswith(('.jpg', '.jpeg', '.png'))]
        wallpaper_path = os.path.join(folder,random.choice(wallpaper_file))
        ctypes.windll.user32.SystemParametersInfoW(20,0,wallpaper_path,3)
        print('Wallpaper changed successfully!')
    except Exception as e:
        print(f'Error while changing:{e}')