import smbus
import time
import sys
from datetime import datetime
from msg_sender import sendpost, target, url
		

bus = smbus.SMBus(1)
address = 0x48


#set TMP175 resolution 0.0625
def adjust_temp_resolution(addr):
	try:
        	val=bus.read_byte_data(addr,0x01)
		if val != 0x60:
			#print "Setting",
			bus.write_byte_data(addr,0x01,0x60)
			#progress_dot()

		return 0;

	except IOError, err:
		print(err)
		return -1

    

#get temperture from TMP175
def gathering_temp(addr):
	tmp=bus.read_word_data(addr,0)
	Lo = (tmp & 0xff00)>>8
        Hi = (tmp & 0x00ff)
        temp = (((Hi*256)+ Lo)>>4)*0.0625  
	return temp



#add animation effect
def progress_dot():
	cnt=0;
	while cnt != 5:
		print ".",
		sys.stdout.flush()
		time.sleep(0.2)
                cnt+=1
	print(" ")


#entry point
try:
	
	if adjust_temp_resolution(address) != 0:
		print("[ERROR] Fail to set up resolution")
	else:
		#wait until setting up
		time.sleep(1)
 		todate=datetime.now()
		tmp=gathering_temp(address)
                cur_date=str(todate.strftime("%Y-%m-%d"))
		cur_time=str(todate.strftime("%H:%M:%S"))
        	print "{'date' :'%s', 'time':'%s', 'tmp':'%f'}" % (cur_date, cur_time, tmp)
		sendpost(target, url, tmp, cur_date, cur_time)
except IOError, err:
	print(err)
 
    
