import threading
import time

class FlameDetector(threading.Thread):

    def __init__(self, i):
        threading.Thread.__init__(self)
        self.h = i

    def run(self):
        while True:
            print("ping")
            time.sleep(2)

