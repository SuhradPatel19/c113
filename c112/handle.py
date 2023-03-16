import shutil
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


from_dir = r"C:\Users\Suhrad.JPLENOVO\Downloads"
to_dir = r"D:\dev\python\to_dir"

dir_tree = {"Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'], "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p',
                                                                                       '.m4v', '.avi', '.mov'], "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'], "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']}


class Suhrad(FileSystemEventHandler):
    def on_created(self, event):

        print("The event is: ", event)
        time.sleep(1)

        print("The src_path is: ", event.src_path)
        time.sleep(1)

        name, extension = os.path.splitext(event.src_path)
        time.sleep(1)

        for i, j in dir_tree.items():
            time.sleep(1)

            if extension in j:
                filename = os.path.basename(event.src_path)
                print("Downloaded the file...")

                
                path1 = from_dir+"/"+filename
                print("Path 1: ", path1)

                
                path2 = to_dir+"/"+i
                print("Path 2: ", path2)

                
                path3 = to_dir+"/"+i+"/"+filename
                print("Path 3: ", path3)

                if os.path.exists(path2):
                    print("Dir Exists")
                    print("Moving...")
                    shutil.move(path1, path3)
                    time.sleep(1)
                else:
                    print("Making Dirs...")
                    os.makedirs(path2)
                    print("Moving...")
                    shutil.move(path1, path3)
                    time.sleep(1)


# inilatlize the event handler class
myEvent = Suhrad()

# inilatlize the observer class
myObserver = Observer()

myObserver.schedule(myEvent, from_dir, recursive=True)
myObserver.start()

while True:
    try:
        time.sleep(2)
        print("Running...")

    except KeyboardInterrupt:
        print("Stopped")
        myObserver.stop()
