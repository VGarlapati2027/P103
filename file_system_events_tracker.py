import sys 
import time 
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "Downloads"
to_dir = "Document_Files"

dir_tree = {
    
    "Image _Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt','.docx','.doc'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']

}

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(event)
        print(event.src_path)
        name,extension = os.path.splitext(event.src_path)
        time.sleep(1)
        for key,value in dir_tree.items():
            time.sleep(1)
            if(extension in value):
                fileName = os.path.basename(event.src_path)
                path1 = from_dir+'/'+fileName
                path2 = to_dir+'/'+key
                path3 = to_dir+'/'+key+'/'+fileName
                if(os.path.exists(path2)):
                    shutil.move(path1,path3)
                else:
                    os.mkdir(path2)
                    shutil.move(path1,path2)
    def on_modified(self, event):
        print(event)
        print(event.src_path)
        name,extension = os.path.splitext(event.src_path)
        time.sleep(1)
        for key, value in dir_tree.items():
            time.sleep(1)
            if(extension in value):
                fileName = os.path.basename(event.src_path)
                path1 = from_dir+'/'+fileName
                path2 = to_dir+'/'+key
                path3 = to_dir+'/'+key+'/'+fileName
                if(os.path.exists(path2)):
                    shutil.move(path1,path3)
                else: os.mkdir(path2)
                shutil.move(path1, path2)
    def on_moved(self, event):
        print(event)
        print(event.src_path)
        name,extension = os.path.splitext(event.src_path)
        time.sleep(1)
        for key, value in dir_tree.items():
            time.sleep(1)
            if(extension in value):
                fileName = os.path.basename(event.src_path)
                path1 = from_dir+'/'+fileName
                path2 = to_dir+'/'+key
                path3 = to_dir+'/'+key+'/'+fileName
                if(os.path.exists(path2)):
                    shutil.move(path1,path3)
                else: os.mkdir(path2)
                shutil.move(path1, path2)
    def on_deleted(self, event):
        print(event)
        print(event.src_path)
        name,extension = os.path.splitext(event.src_path)
        time.sleep(1)
        for key, value in dir_tree.items():
            time.sleep(1)
            if(extension in value):
                fileName = os.path.basename(event.src_path)
                path1 = from_dir+'/'+fileName
                path2 = to_dir+'/'+key
                path3 = to_dir+'/'+key+'/'+fileName
                if(os.path.exists(path2)):
                    shutil.move(path1,path3)
                else: os.mkdir(path2)
                shutil.move(path1, path2)


event_handler = FileEventHandler()

observer = Observer()

observer.schedule(event_handler, from_dir, recursive=True)

observer.start()

try:
    while True:
        time.sleep(2)
        print("running.......") 
except:observer.stop()
                



