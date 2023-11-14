import subprocess
import os
import shutil
import argparse
import threading
parser = argparse.ArgumentParser(description='Inference Running')
parser.add_argument('--videos', nargs='*', type=str, help="the list of videos to process")
parser.add_argument('--model', type=str, help="the model doing the inference (.pt file)")
vids = []
choice = ""
output_folder = "./output"
def_output_folder = "out"
full_output_path = ""
yolo_output_path_log = "output_path_log.txt"
event = threading.Event()
args = parser.parse_args()
vids = args.videos

def determine_output_folder(): #returns path of new output folder
  output_list = os.listdir(output_folder)
  max = 0
  for folder in output_list:
      if folder.startswith(def_output_folder): 
        if len(folder) == len(def_output_folder):
            if max < 2:
              max = 2
        else:
            folder_num = int(folder[3:len(folder)])
            if folder_num >= max:
              max = folder_num + 1
  if max == 0:
      new_output_folder = os.path.join(output_folder,def_output_folder)
  else:
      new_output_folder = os.path.join(output_folder, def_output_folder + str(max))
  return new_output_folder
def processing_block():
  model = os.path.join("./iterations/", args.model)
  if len(vids) > 0:
    for video in vids:
      print("Current Video: " + video)
      # running detection process: –save-txt option allows yolov5 to write individual detections to .txt files, which the logging 
      # script uses to log to excel
      proc1 = subprocess.Popen(['python', 'detect.py', '--weights', model, '--source', os.path.join("videos/", video), '--save-txt'])
      proc1.communicate()
      # running logging process
      proc2 = subprocess.Popen(['python', 'dataExp.py'])
      proc2.communicate()
  event.set()
if __name__ == "__main__":
  thread_one = threading.Thread(target=processing_block) #we need to make sure this runs before anything else
  thread_one.start()
  thread_one.join()
  # post processing
  if len(vids) > 0:
    if os.path.exists(output_folder) == False:
      os.mkdir(output_folder)
    full_output_path = determine_output_folder()
    os.mkdir(full_output_path)
    print("OUTPUT FOLDER: " + full_output_path)
    # moving appropriate files
    shutil.move("detections.xlsx", full_output_path)
    folders = []
    with open(yolo_output_path_log, 'r') as yolo_output:
      for line in yolo_output.readlines():
          folders.append(line.strip())
    os.remove(yolo_output_path_log)
    for i in range(len(folders)):
        if len(folders[i]) > 0: # should not run until processing is finished
          vid = os.path.join(folders[i], os.listdir(folders[i])[0])
          shutil.move(vid, full_output_path)
          os.rmdir(folders[i])
  if os.path.exists("runs"):
    shutil.rmtree("runs")