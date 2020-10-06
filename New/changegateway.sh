#!/bin/bash

#This script creates a fucniton that will help in changing the GATEWAY
#
#  created by : Rahul Kumar
#

GATEWAY=${1}
changeGATEWAY(){

  if grep -R -q "GATEWAY" $path
  then
  sed -i 's/^.*GATEWAY.*$/GATEWAY='${GATEWAY}'/' $path
  sed -i '/^$/d' $path
  echo "Your new GATEWAY:- ${GATEWAY}"
  else
  echo "GATEWAY=${GATEWAY}" >>$path
  echo "Your new GATEWAY:- ${GATEWAY}"
  fi
  
  # restarting newtwork

  echo "Network is restarting..."
  sleep 3
  sudo systemctl restart NetworkManager.service
}


changedGATEWAY(){
  path='/etc/sysconfig/network-scripts/ifcfg-enp0s3'
  if grep -q "BOOTPROTO" $path
  then
  sed -i 's/^.*BOOTPROTO.*$/BOOTPROTO=static/' $path
  sed -i '/^$/d' $path
  changeGATEWAY
  else
  sed -i '/^$/d' $path
  echo "BOOTPROTO=static" >> $path
  changeGATEWAY
  fi
}

if ipcalc -cs $GATEWAY
then
  changedGATEWAY
else
  echo "Invalid Gateway"
  exit 1
fi
