from watchdog.events import FileSystemEventHandler

class EventWatcher(FileSystemEventHandler):
    
    def __init__(self, path, hook) -> None:
        super().__init__()
        self.path = path
        self.hook = hook
    
    def catch_all_handler(self, event):
        pass

    def on_created(self, event):
        self.hook(event)
        self.catch_all_handler(event)