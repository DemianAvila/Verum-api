package logger

import (
    "log"
    "os"
)

func LoggerInit() {
    // If the file doesn't exist, create it or append to the file
    file, err := os.OpenFile("/var/log/logs_backend.txt", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0666)
    if err != nil {
        log.Fatal(err);
    }
    log.SetOutput(file);
}

func LoggerType(logType string, message string){
	log.Println(logType+": "+message);
}