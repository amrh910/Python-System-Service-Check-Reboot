# Python-System-Service-Check-Reboot

This is a simple python script that checks the status of a system service.

This is similar to running ```systemctl status [service-name]``` in the terminal.

## This script is tested and functional on Ubuntu
While this script is compatible with the majority of Linux systems that can check status of a service via ```systemctl```, it has only been tested on Ubuntu. You may adjust the script by simply replacing the system service checker command syntax at line 7. 

## Usage
This script is defaulted to MySQL service. You can however change it to whichever service you would need. Simply open ```restartchck.py``` and replace the value for ```service_name``` at line 3. 

To use this script, navigate to the directory in which the script is stored and run it by typing ```python restartchk.py``` in your terminal.

## Cronjob
To convert this script to a cronjob,
1. Login to your server as root
2. Place this script in your server's /root directory
3. open terminal and enter ```crontab -e```.
4. Append to the crontab by adding after the last line the following statement:
	```* * * * * /usr/bin/python /root/restartcheck.py```

	Cronjobs are formatted as follow: ```[cronjob frequency] [compiler abs path] [script abs path]```
	I like to use [crontab.guru](https://crontab.guru/) to save time when it comes to the cronjob frequency.
5. Save and exit. 
6. Confirm your cronjob was created by typing ```crontab -l``` and reviewing the output.
