import hashlib
import sys
import threading
import datetime
import os

class Watcher:

    def __init__(self,file_name):
        self.file_name = file_name
        self.original_hash = self.read_and_hash_file()
        self.delay = 10
        self.timer()

    def timer(self):
        current_hash = self.read_and_hash_file()
        if current_hash == self.original_hash:
            print("Not Changed At Time : " + datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y"))
        else:
            print("Changed At Time     : " + datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y"))
            self.original_hash = current_hash
        threading.Timer(self.delay,self.timer).start()

    def read_and_hash_file(self):
        try:
            file = open(self.file_name,"r")
            hsh = hashlib.md5()
            text_in_file = file.read().encode('UTF-8')
            file.close()
            hsh.update(text_in_file)
            return hsh.hexdigest()
        except FileNotFoundError as e:
            print(e)

if __name__ == "__main__":
    file_name = sys.argv[1]
    os.popen(file_name)
    Watcher(file_name)

