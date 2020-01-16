import sys
import time
import logging
from eventhandler import ReportEventHandler
from watchdog.observers import Observer
from config import MonitorConfig
import glob

config=MonitorConfig()
path = config.DATAPATH

logging.basicConfig(level=logging.INFO,handlers=[
        logging.FileHandler("{0}/{1}.log".format("/logs", "eventhandler")),
        logging.StreamHandler()
        ],format='%(asctime)s - %(message)s',datefmt='%Y-%m-%d %H:%M:%S')

def markprocessing(self,filename):
        logging.info("Moving %s to PROCESSING", filename)
        shutil.move(config.DATAPATH+filename,config.PROCESSINGPATH+filename)        

def marksuccess(self, filename):
        logging.info("Moving %s to SUCCESS", filename)
        shutil.move(config.PROCESSINGPATH+filename, config.SUCCESSPATH+filename)

def markfail(self, filename):
        logging.info("Moving $s to FAILED", filename)
        shutil.move(config.PROCESSINGPATH+filename, config.FAILPATH+filename)

def create_job(self,filename):
        DATA=[{"filename":filename}]
        logging.info("Sending a new job with %s to %s", filename, config.CREATEJOB_URL)
        r = requests.post(url = config.CREATEJOB_URL, json  = DATA)
        # extracting results in json format
        try:
           data = r.json()
           logging.info("Reply received %s", data)
        except:
           logging.info("An error has occurred during CREATE JOB call")
           markfail(filename)

        if data['results']=='ok':
            marksucess(filename)

if __name__ == "__main__":
    config = MonitorConfig()
    path = config.DATAPATH
    logging.info("DATAPATH is {}".format(path))
    try:
        while True:
            logging.debug("Waiting for next interval of %s secs", config.CHECK_INTERVAL)
            time.sleep(int(config.CHECK_INTERVAL))
            import glob
            listoffiles = glob.glob(config.DATAPATH+"*")
            for filepath in listoffiles:
                logging.debug("Processing %s", filepath)
                filename=filepath.split("/")[-1]
                markprocessing(filename)
                #Send new job create, if success move file to processing folder
                logging.info("Sending to new job")
                create_job(filename)
                logging.info("Sent to create new job")     	
                          
    except KeyboardInterrupt:
        exit(0)