class MonitorConfig():
    
    DATAPATH="/shareddata/new/"
    PROCESSINGPATH="/shareddata/processing/"
    SUCCESSPATH="/shareddata/success/"
    FAILPATH="/shareddata/fail/"
    CREATEJOB_URL="http://jobsvc:9891/create_job"
    SETREPORTSTATUS_URL="http://savesvc:9891/setreportstatus"
    CHECK_INTERVAL=10
