import tkinter as tk
import os
from PIL import ImageTk, Image
import subprocess
import signal
import shutil
from threading import Thread
from queue import Empty, Queue
import platform

image_path = os.path.join(os.path.dirname(__file__), "./assets/NewBanner.jpg")
min_width = 600
min_height = 630
videos_path = os.path.join(os.path.dirname(__file__), "videos")
def_output_folder = "out"
os_name = platform.system()


class GUI:
    def __init__(self):
        self.root = tk.Tk()

        self.root.mainloop()

GUI()