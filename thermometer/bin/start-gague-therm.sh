# !/bin/sh

HOME_DIR=$HOME
ROOT_DIR=${HOME_DIR}/thermometer
LOG_DIR=${ROOT_DIR}/log


if [ ! -e ${LOG_DIR} ];
then
   echo "Create Log directory"
   mkdir -p ${LOG_DIR}
fi

nohup python ${ROOT_DIR}/thermometer.py  >>  ${LOG_DIR}/log.out  &

