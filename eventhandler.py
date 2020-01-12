import requests
import os
import shutil
from watchdog.events import FileSystemEventHandler
class ReportEventHandler(FileSystemEventHandler):

    def __init__(self,config):
        self.config=config
        super().__init__()

    def markprocessing(self,filename):
        shutil.move(config.NEW_PATH+filename,config.PROCESSING_PATH+filename)        

    def create_job(self,srcpath):
        filename=srcpath.split("/")[-1]
        DATA={"filename":filename}
        r = requests.post(url = self.config.CREATEJOB_URL, json  = DATA)
        print(r)
        # extracting results in json format
        data = r.json()
        if data['message']=='ok':
            markprocessing(filename)

    def on_moved(self, event):
        pass

    def on_created(self, event):

        what = 'directory' if event.is_directory else 'file'
        if what == 'file':      
           #Send new job create, if success move file to processing folder
           self.create_job(event.src_path)
        logging.info("Created %s: %s", what, event.src_path)

    def on_deleted(self, event):
        pass

    def on_modified(self, event):
        self.on_created(event) 
