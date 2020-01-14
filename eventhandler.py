import requests
import os
import shutil
from watchdog.events import FileSystemEventHandler
class ReportEventHandler(FileSystemEventHandler):

    def __init__(self,config,logging):
        self.config=config
        self.logging = logging
        super().__init__()

    def markprocessing(self,filename):
        shutil.move(config.DATAPATH+filename,config.PROCESSINGPATH+filename)        

    def marksuccess(self, filename):
        shutil.move(config.PROCESSINGPATH+filename, config.SUCCESSPATH+filename)

    def markfail(self, filename):
        shutil.move(config.SUCCESSPATH+filename, config.FAILPATH+filename)

    def create_job(self,filename):
        DATA={"filename":filename}
        r = requests.post(url = self.config.CREATEJOB_URL, json  = DATA)
        print(r)
        # extracting results in json format
        try:
           data = r.json()
        except:
           markfail(filename)

        if data['message']=='ok':
            marksucess(filename)

    def on_moved(self, event):
        pass

    def on_created(self, event):
        self.logging.info("Created %s: %s", what, event.src_path)
        filename=event.src_path.split("/")[-1]
        what = 'directory' if event.is_directory else 'file'
        if what == 'file':      
           self.markprocessing(filename)
           self.logging.info("Moved file")
           #Send new job create, if success move file to processing folder
           self.create_job(filename)
           self.logging.info("Sent to create new job")

    def on_deleted(self, event):
        pass

    def on_modified(self, event):
        self.on_created(event) 
