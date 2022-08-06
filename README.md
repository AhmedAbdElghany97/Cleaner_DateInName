# Cleaner_DateInName Script
 
A simple cleaner for specific path with a files that include a date in its name.

## Description

This is a simple cleaner script that cleans a specific path for files that include a date in its name with the number of days you want to keep.
Give it a path that you want to clean and days that you want to keep. It will loop throw all files and extract a date that is included in the filename with given format and compare it with today's date and finally clean. All these steps will be logged in a logger in a path you set. 

## Getting Started

### Dependencies

* [Python 3](https://www.python.org/downloads)

### Installing

* Install [Python 3](https://www.python.org/downloads) in your OS (Windows, Linux, etc.)
* Download Cleaner_DateInName Script:
  From here: https://github.com/AhmedAbdElghany97/Cleaner_DateInName.git
Or you can use this command:
  ```
  git clone https://github.com/AhmedAbdElghany97/Cleaner_DateInName.git
  ```
* Set variables with specific values:
Replace following variable with a path you need to clean.
  ```python
  pathToClean = "PATH_THAT_WANT_TO_CLEAN"
  ```
  Replace following variable with a days that you want to keep.
  ```python
  dayToKeep = 5
  ```
  Replace following variable with a format of date that included in a filename.
  ```python
  dateFormat = "%Y_%m_%d"
  ```
  Replace following variable with a path you need to store the log file.
  ```python
  stdFilePath = "PATH_FOR_LOGGER"
  ```
  
### Executing program
* You can simply run it by Terminal using this command:
  ```
  py Cleaner_DateInName.py
  ```
* You can also schedule it using Task Schecdular on Windows or using crontab on Linux.

## Author

Created by [@Ahmed Abd Elghany](https://www.linkedin.com/in/ahmedabdelghany97) - contact me!

