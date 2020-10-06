#!/bin/bash

#This script creates a fucniton that will help in changing the subnet
#  created by : Rahul Kumar
#

SUBNET=${1}
changesubnet(){
  if grep -R -q "SUBNET" $path
  then
  sed -i 's/^.*SUBNET.*$/SUBNET='${SUBNET}'/' $path
  sed -i '/^$/d' $path
  echo "Your new SUBNET:- ${SUBNET}"
  else
  echo "SUBNET=${SUBNET}" >>$path
  echo "Your new SUBNET:- ${SUBNET}"
  fi
  
  # restarting newtwork

  echo "Network is restarting..."
  sleep 3
  sudo systemctl restart NetworkManager.service
}


changedsubnet(){
  path='/etc/sysconfig/network-scripts/ifcfg-enp0s3'
  if grep -q "BOOTPROTO" $path
  then
  sed -i 's/^.*BOOTPROTO.*$/BOOTPROTO=static/' $path
  sed -i '/^$/d' $path
  changesubnet
  else
  sed -i '/^$/d' $path
  echo "BOOTPROTO=static" >> $path
  changesubnet
  fi
}

if ipcalc -cs  $SUBNET
then
changedsubnet
else
 echo "Invalid Subnet"
 exit 1
