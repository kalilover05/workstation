#!/bin/bash

# this script is for  mapping one shell script file with different shell scripts
#  created by : Rahul Kumar
#

COMMAND=${1}

echo $COMMAND
if [[ ${COMMAND} == changeip ]]
then

bash changeip.sh ${2}
elif [[ ${COMMAND} == changesubnet ]]
then
bash changesubnet.sh ${2}
elif [[ ${COMMAND} == changegateway ]]
then
bash changegateway.sh ${2}
else
  echo "Invalid command"
fi
