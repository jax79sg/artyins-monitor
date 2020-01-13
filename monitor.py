import sys
import time
import logging
from eventhandler import ReportEventHandler
from watchdog.observers import Observer
from config import MonitorConfig

if __name__ == "__main__":
    config = MonitorConfig()
    logging.basicConfig(level=logging.INFO,handlers=[
        logging.FileHandler("{0}/{1}.log".format(".", "log")),
        logging.StreamHandler()
    ],
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = ReportEventHandler(config)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
