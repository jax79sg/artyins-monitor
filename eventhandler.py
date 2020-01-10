import requests
import os
import shutil

class ReportEventHandler():

    def markprocessing(filename):
        shutil.move(config.NEW_PATH+filename,config.PROCESSING_PATH+filename)        

    def create_job(filename):
        r = requests.post(url = config.CREATEJOB_URL, json  = DATA)
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
        logging.info("Created %s: %s", what, event.src_path)

    def on_deleted(self, event):
        pass

    def on_modified(self, event):
        pass
