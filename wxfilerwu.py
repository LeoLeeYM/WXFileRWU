import os
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            # 获取新创建文件的完整路径
            file_path = event.src_path
            print(file_path)
            # 修改文件权限为可读，可写，可执行
            try:
                os.chmod(file_path, 0o777)
            except:
                pass

    def on_modified(self, event):
        if not event.is_directory:
            # 获取被修改文件的完整路径
            file_path = event.src_path
            print(file_path,'修改')
            # 修改文件权限为可读，可写，可执行
            try:
                os.chmod(file_path, 0o777)
            except:
                pass

if __name__ == "__main__":
    c_drive = os.getenv("SystemDrive")

    with open(os.path.join(c_drive, "/wxfilerwu.ini"), "r", encoding="utf-8") as file:
        path = file.read()

    path = path
    
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
