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

import customtkinter


#style adapted from https://www.youtube.com/watch?v=iM3kjbbKHQU

# # Here's what you should aim to have done by Sunday:
# - Be able to select the video to process
# - Be able to change the model you're using (make a variable called model_path or smth like that)
# - Be able to hit a button & have the model process the video
#     - The detect script from yolo should already throw this in an output folder automatically so I don't think you'll have to worry about that
#     - Don't worry about any spreadsheet stuff or anything, as long as the model processes the video and outputs a video with bounding boxes we're good
# - Don't worry about streaming terminal output or anything like that, as long as you get this functionality and make it look semi-nice, we're golden

# # How will you acheive this?
# - hook a button up in the UI to the detect.py script (don't worry about master_detect_data or dataExp, for all intents & purposes that's specific to last year's project')
# - and like I said, detect.py should automatically handle where there output video gets put after processing
# - I provided some basic UI components for you down below, but it's on you to use your resources to get the rest of the components that you need, I linked the YT video that I used and there's lots of documentation online so I think you should be fine

# # Some notes
# - its good to maybe download a really short, like 20 second video to test that this frontend works since processing a regular 5-min video will take a while 
# - after you establish that this works, then you can throw one of the big videos (provided for you in the videos folder) into the model for processing & see the real output (be ready for some serious overfitting)

class GUI:
    def __init__(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_appearance_mode("dark-blue")
        root = customtkinter.CTk()
        root.geometry("600x400")

        frame = customtkinter.CTkFrame(master=root)
        frame.pack(pady=20, padx=60, fill="both")
        #everything before this is boilerplate setup

        # note that saying master=x is specifying the parent component - the rest of the fields are specific to the component we're defining
        label = customtkinter.CTkLabel(master=frame, text="2024 ML Challenge!", font=("Roboto", 24)) 
        label.pack(pady=12, padx=10)

        entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="example of a text box")
        entry1.pack(pady=12, padx=10)

        checkbox = customtkinter.CTkCheckBox(master=frame, text="Checkbox")
        checkbox.pack(pady=12, padx=10)

        # Dropdown menu (you'll need this for choosing videos to process potentially)
        checklist_var = tk.StringVar()
        checklist_var.set("Select Items")  # Default text when no items are selected

        items = ["Item 1", "Item 2", "Item 3"]
        checklist = customtkinter.CTkOptionMenu(master=frame, variable=checklist_var, values=items)
        checklist.pack(pady=12, padx=10)


        root.mainloop() # you need this line to make the frame actually appear - MAKE SURE IT'S THE LAST LINE IN THE RENDERING LOGIC

GUI()