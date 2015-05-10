# temperature-checker

This project is for the inital django web server on the raspberry PI platform.

And also it is comprised of 2 programs which are thermometer program and thermostat web server program respectively.


1) Thermometer

  How to run..
   $ project_root/thermometer/bin/start-gague-therm.sh

  How to check 
   $ cat project_root/thermometer/log/log.out
   
2) Themostat

   How to run
   $ project_root/themostat/bin/run_thermostat.sh
   
   How to check whether it runs properly
   $ cat project_root/themostat/log/{now}_themostat.log
