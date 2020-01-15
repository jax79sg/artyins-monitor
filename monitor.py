import sys
import time
import logging
from eventhandler import ReportEventHandler
from watchdog.observers import Observer
from config import MonitorConfig

if __name__ == "__main__":
    config = MonitorConfig()
    path = config.DATAPATH
    logging.basicConfig(level=logging.INFO,handlers=[
        logging.FileHandler("{0}/{1}.log".format("/logs", "monitor")),
        logging.StreamHandler()
    ],
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logging.info("DATAPATH is {}".format(path))
    event_handler = ReportEventHandler(config, logging)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
