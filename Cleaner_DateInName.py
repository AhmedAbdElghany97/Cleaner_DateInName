#----------------------#
# This Script Created By: Ahmed Abd Elghany
# Contact Me: AhmedAbdElghany97.eg@gmail.com
#----------------------#
import os
from datetime import datetime, timedelta
import logging


#Put Jira & TFS path here:
pathToClean = "PATH_THAT_WANT_TO_CLEAN"


#This will list all files inside the path
pathToCleanDir = os.listdir(pathToClean)

#How many days do you want to keep?
dayToKeep = 5 #DAYS_WANT_TO_KEEP


#Date formate that included in a filename -- "%Y_%m_%d" means Year_Month_Day like 2022_08_01
dateFormat = "%Y_%m_%d" #DATE_IN_NAME_FORMAT


#File Name Example: backup_2022_08_01_060020.bak


#Create and configure logger 
stdFilePath = "PATH_FOR_LOGGER"
logging.basicConfig(filename=stdFilePath, 
					format='%(asctime)s %(message)s', 
					filemode='a') 
logger=logging.getLogger()  
logger.setLevel(logging.DEBUG)
logger.info("Script started.") 


def deleteFiles(day, origPath, fileName):
    deleteFile = False
    today = datetime.today()
    file = origPath + fileName
    for x in range(0, day, 1):
        daysBefore = today - timedelta(days=x)
        daysFormated = daysBefore.strftime(dateFormat)
        if os.path.isdir(file):
            deleteFile = False
            logger.info(file+" is a directory.") 
            break
        else:
            if daysFormated in fileName: 
                deleteFile = False
                break
            else:
                deleteFile = True
    if deleteFile == True:
        os.remove(file)
        logger.info("This file delected, it's older than "+str(day)+" days. --> "+file) 
    else:
        logger.info("This file didn't delete, it's within last "+str(day)+" days. --> "+file) 


#Loop all files in path and perform deleteFiles function
for arrItem in pathToCleanDir:
    deleteFiles(dayToKeep, pathToClean+"\\", arrItem)




