import subprocess
import os
ethh= "enp0s3" #adapter name
stringg=""
booto=""


def changedtos(ethh):
    booto=check_if_string_in_file("/etc/sysconfig/network-scripts/ifcfg-{}".format(ethh), 'BOOTPROTO')
    removeline(booto)
    file_object = open("/etc/sysconfig/network-scripts/ifcfg-{}".format(ethh), 'a')
    file_object.write("BOOTPROTO=static\n")
    file_object.close()

def check(ethh):
     if check_if_string_in_file_t("/etc/sysconfig/network-scripts/ifcfg-{}".format(ethh), 'BOOTPROTO=static'):
        return True



def check_if_string_in_file_t(file_name, string_to_search):
    """ Check if any line in the file contains given string """
    # Open the file in read only mode
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            if string_to_search in line:
                return True
    return False


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
        print("changeip\t\t\t => to change IP ")
        print("changegateway  \t\t\t => to  change Gateway")
        print("changesubnet  \t\t\t => to change subnet")
        print("showip\t\t\t => to Show IP ")
        print("showgateway\t\t\t => to show gateway ")
        print("showsubnet\t\t\t => to show subnet ")

        print("\n\n")


def showip(ethh):
    ip=check_if_string_in_file("/etc/sysconfig/network-scripts/ifcfg-{}".format(ethh), 'IPADDR=')
    if ip:
        print("your current Ip address is {}".format(ip[7:]))
    else:
        print("no ip address is set please use command changeip")


def showgateway(ethh):
    gateway=check_if_string_in_file("/etc/sysconfig/network-scripts/ifcfg-{}".format(ethh), 'GATEWAY=')
    if gateway:
        print("your current gateway is {}".format(gateway[8:]))
    else:
        print("no gateway is set please use command changegateway")


def showsubnet(ethh):
    subnet=check_if_string_in_file("/etc/sysconfig/network-scripts/ifcfg-{}".format(ethh), 'NETMASK=')
    if subnet:
        print("your current subnet is {}".format(subnet[8:]))
    else:
        print("no subnet is set please use command changesubnet")




mapper={
    'help':help,
    'changeip':changeip,
    'changesubnet':changesubnet,
    'changegateway':changegateway,
    'showip':showip,
    'showgateway': showgateway,
    'showsubnet': showsubnet
}

def process(command):
    try:
        funtion=mapper[command]
        funtion(ethh)
    except KeyError :
        print("!!! Invalid Command !!!")



# main  work

while True:
    if check(ethh):
        pass
    else:
        changedtos(ethh)
    command=input("u.trust.cli #: ")
    process(command)
