#!/bin/sh

HOME_DIR=/home/pi
ROOT_DIR=${HOME_DIR}/themostat
BIN_DIR=${ROOT_DIR}/bin
LOG_DIR=${ROOT_DIR}/log
PID_DIR=${ROOT_DIR}/pid
PID_FILE=themostat.pid

DAEMON=${ROOT_DIR}/manage.py
DAEMON_OPTS=""

#Service IP and Port 
IP_ADDR=0.0.0.0
PORT=8080


echo "THEMOSTAT SERVER RUNNING"
today=`date +'%Y%m%d%M%S'`


if [ ! -e ${PID_DIR} ];
then
    mkdir -p ${PID_DIR}
fi



if [ ! -e ${LOG_DIR} ];
then
    mkdir -p ${LOG_DIR}
fi


nohup python ${ROOT_DIR}/manage.py runserver ${IP_ADDR}:${PORT}  >> ${LOG_DIR}/${today}_themostat.log &


