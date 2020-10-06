
#!/bin/bash

#This script creates a fucniton that will help in changing the ip
#  created by : Rahul Kumar
#
IPADDR=$1
changeip(){


  if grep -R -q "IPADDR" $path
  then
  sed -i 's/^.*IPADDR.*$/IPADDR='${IPADDR}'/' $path
  sed -i '/^$/d' $path
  echo "Your new IPADDR:- ${IPADDR}"
  else
  echo "IPADDR=${IPADDR}" >>$path
  echo "Your new IP Address:- ${IPADDR}"
  fi
  
  # restarting newtwork

  echo "Network is restarting..."
  sleep 3
  sudo systemctl restart NetworkManager.service
}


changedip(){
  path='/etc/sysconfig/network-scripts/ifcfg-enp0s3'
  if grep -q "BOOTPROTO" $path
  then
  sed -i 's/^.*BOOTPROTO.*$/BOOTPROTO=static/' $path
  sed -i '/^$/d' $path
  changeip
  else
  sed -i '/^$/d' $path
  echo "BOOTPROTO=static" >> $path
  changeip
  fi
}

if ipcalc -cs $IPADDR
then
	changedip
else
    echo "Invalid IP"
    exit 1
fi
