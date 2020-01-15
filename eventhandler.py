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
        self.logging.info("Moved %s to PROCESSING", filename)
        shutil.move(self.config.DATAPATH+filename,self.config.PROCESSINGPATH+filename)        

    def marksuccess(self, filename):
        self.logging.info("Moved %s to SUCCESS", filename)
        shutil.move(self.config.PROCESSINGPATH+filename, self.config.SUCCESSPATH+filename)

    def markfail(self, filename):
        self.logging.info("Moved $s to FAILED", filename)
        shutil.move(self.config.SUCCESSPATH+filename, self.config.FAILPATH+filename)

    def create_job(self,filename):
        DATA={"filename":filename}
        self.logging.info("Sending a new job with %s to %s", filename, self.config.CREATEJOB_URL)
        r = requests.post(url = self.config.CREATEJOB_URL, json  = DATA)
        # extracting results in json format
        try:
           data = r.json()
           self.logging.info("Reply received %s", data)
        except:
           self.logging.info("An error has occurred during CREATE JOB call")
           markfail(filename)

        if data['message']=='ok':
            marksucess(filename)

    def on_moved(self, event):
        pass

    def on_created(self, event):
        filename=event.src_path.split("/")[-1]
        what = 'directory' if event.is_directory else 'file'
        if what == 'file':      
           self.logging.info("New file %s: %s", what, event.src_path)
           self.markprocessing(filename)
           #Send new job create, if success move file to processing folder
           self.create_job(filename)
           self.logging.info("Sent to create new job")

    def on_deleted(self, event):
        pass

    def on_modified(self, event):
        self.on_created(event) 
