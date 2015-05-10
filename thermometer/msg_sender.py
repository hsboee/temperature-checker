import httplib,urllib
from datetime import datetime
import time
import errno
from socket import error as socket_error

target = "127.0.0.1:8080"
url    = "/insert_tmp"


def sendpost(host,url, tmp, date, time):
	
	#print("%s %s %f" % (host, url, tmp))
		
	conn=httplib.HTTPConnection(host)
	
	data=dict(tmp=tmp, date=date, time=time)
	#print(data)
	
	params = urllib.urlencode(data)
	headers ={"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

	res=conn.request("POST", url, params, headers)

	#res=conn.request("GET",url)
	#print(conn.getresponse().read())

       	conn.close()
"""
try:
	sendpost(target, url, 23.11, "2015-03-20", "21:00:10")
except socket_error, err:
	print err
"""
