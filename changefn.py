import subprocess
import os
ethh= "enp0s3" #adapter name
stringg=""

#This function will check if string in present in file or not.
# if present then it will print the line but don't remove it

def check_if_string_in_file(file_name, string_to_search):
    """ Check if any line in the file contains given string """
    with open(file_name, 'r') as read_obj:
        for line in read_obj:
            if string_to_search in line:
                return line
    return False

# This removeline fn will remove line with the help of given searched string
# resulted by the check_if_string_in_file fn

def removeline(stringg):
    with open("/etc/sysconfig/network-scripts/ifcfg-{}".format(ethh), "r+") as f:
        d = f.readlines()
        f.seek(0)
        for i in d:
            if i != stringg:
                f.write(i)
        f.truncate()

# this function will change ip address when bootproto in static mode.

def changeip(ethh):
        stringg=check_if_string_in_file("/etc/sysconfig/network-scripts/ifcfg-{}".format(ethh), 'IPADDR=')
        removeline(stringg)
        if stringg == False:
            stringg="None"
        else:
            stringg=stringg[7:]
        ipv4=input("\nEnter your New Ipv4 address :\n")
        file_object = open("/etc/sysconfig/network-scripts/ifcfg-{}".format(ethh), 'a')
        file_object.write("IPADDR={}\n".format(ipv4))
        file_object.close()
        print("network is restarting please wait...\n")
        subprocess.call("sudo systemctl restart network", shell= True)
        print("your IPv4 is successfully changed from {} to {}".format(stringg,ipv4))
        return "IPv4 successfully configured and restarted network"

# this function will change subnet(netmask) address when bootproto in static mode.
def changesubnet(ethh):
        stringg=check_if_string_in_file("/etc/sysconfig/network-scripts/ifcfg-{}".format(ethh), 'NETMASK')
        removeline(stringg)
        if stringg == False:
            stringg="None"
        else:
            stringg=stringg[8:]
        netmask=input("\nEnter your New Subnet(NETMASK) :\n")
        file_object = open("/etc/sysconfig/network-scripts/ifcfg-{}".format(ethh), 'a')
        file_object.write("NETMASK={}\n".format(netmask))
        file_object.close()
        print("network is restarting please wait...\n")
        subprocess.call("sudo systemctl restart network", shell= True)
        print("your subnet(netmask) is successfully changed from {} to {}".format(stringg,netmask))
        return "netmask (subnet) successfully configured and restarted network"

# this function will change Gateway address when bootproto in static mode.
def changegateway(ethh):
        stringg=check_if_string_in_file("/etc/sysconfig/network-scripts/ifcfg-{}".format(ethh), 'GATEWAY')
        removeline(stringg)
        if stringg == False:
            stringg="None"
        else:
            stringg=stringg[8:]
        gateway=input("\nEnter your New Gateway Address :\n")
        file_object = open("/etc/sysconfig/network-scripts/ifcfg-{}".format(ethh), 'a')
        file_object.write("GATEWAY={}\n".format(gateway))
        file_object.close()
        print("network is restarting please wait...\n")
        subprocess.call("sudo systemctl restart network", shell= True)
        print("your gateway is successfully changed from {} to {}".format(stringg,gateway))
        return "gateway successfully configured and restarted network"
def help(x):
        print("\n\n")
        print("changeip\t\t\t => change IP ")
        print("changegateway  \t\t\t => change Gateway")
        print("changesubnet  \t\t\t => change subnet")
        print("\n\n")
mapper={
    'help':help,
    'changeip':changeip,
    'changesubnet':changesubnet,
    'changegateway':changegateway
}
def process(command):
    try:
        funtion=mapper[command]
        funtion(ethh)
    except KeyError :
        print("!!! Invalid Command !!!")
while (True):
        command=input("xyzpromt#: ")
        process(command)
