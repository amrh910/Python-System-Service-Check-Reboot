import os

service_name = "mysql" #replace service_name with any service
action_abs_path = "/sbin/reboot" #sometimes you might need to replace with /sbin/reboot or otherwise depending on the OS action you want to execute

def checkService(service_name):
    status = os.system('systemctl status ' + service_name + ' > /root/pyrestart/null') #replace mysql with any service name
    return status

def main():
    if(checkService(service_name) == 0):
        print(service_name + "status: running...")
    else:
        print(service_name + "status: STOPPED!")
        os.system(action_abs_path) #if fails, give sudo privileges or replace with os.system('sudo *reboot_path*')

        #depending on the service, you might just need to restart service instead of system.
        #You may do these system call adjustments by changing variable action_abs_path at line 4

main()