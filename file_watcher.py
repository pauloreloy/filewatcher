import sys
import time
from watchdog.observers import Observer
from classes.Eventwatcher import EventWatcher
from classes.Filehandler import Filehandler

path = "/opt/apl/files/"

if __name__ == "__main__":
    
    event_watcher = EventWatcher(path, Filehandler().handler)
    obs = Observer()
    obs.schedule(event_watcher, path, recursive=False)
    obs.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        obs.unschedule(event_watcher)
        obs.stop()
    obs.join()