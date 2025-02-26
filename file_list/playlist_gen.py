import re
import os
from tkinter import filedialog
from mutagen.mp3 import MP3


def get_mp3_duration(file_path):
    audio = MP3(file_path)
    return audio.info.length  # Returns duration in seconds

path = filedialog.askdirectory()
print(path)
# print(os.listdir(path))
target = filedialog.asksaveasfilename()
with open(target, mode='a') as tf:
    for file in os.listdir(path):
        file_path = path+"/"+file
        track_length_in_sec = str(int(get_mp3_duration(file_path)))
        print(track_length_in_sec)
        tf.writelines(f"#EXTINF:{track_length_in_sec},{file[:-4]}\n")
        tf.writelines(path + "\\" + file + "\n")