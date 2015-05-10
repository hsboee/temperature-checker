from django.shortcuts import render, render_to_response, redirect
from themocheck.models import Date, Theom
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,Http404,HttpResponseRedirect,HttpResponsePermanentRedirect
from django.core.urlresolvers import reverse
from nvd3 import pieChart
from forms import DateForm,SimpleForm
from django.contrib import messages
from django.contrib.messages import error
import datetime
import random
import time
import logging

logger = logging.getLogger(__name__)

# Create your views here.

@csrf_exempt
def get_dates(request):
	rec_date_list=Date.objects.all()
	context ={'rec_date_list' : rec_date_list}
	return render(request,'rec_date.html',context)
	


@csrf_exempt
def show_datepicker(request):
	
	if request.method == 'POST':
		
		postform=DateForm(request.POST)
		if postform.is_valid() :
			req_date=request.POST.get('date', None)
			request.session['date']=req_date
			return HttpResponseRedirect('/onedaytmp')
			#return HttpResponseRedirect(reverse('show_oneday_tmp', kwargs={'date': req_date}))
		else:
			messages.error(request, "Error")
			#return HttpResponseRedirect('/')

	form=DateForm()
	context={'form':form}
	return render(request, 'datepicker.html',context)




@csrf_exempt
def insert_tmp(request):

	reg_date=None

	if request.method != 'POST':
		raise Http404("POST message only")

	date=request.POST['date']
	time=request.POST['time']
	tmp=request.POST['tmp']

	if date is None or time is None or tmp is None:
		raise Http404("Bad Parameter")
	
	try:	
		reg_date=Date.objects.get(rec_date=date)
	
	except Date.DoesNotExist:
		reg_date=Date(rec_date=date)
		reg_date.save()
	finally:
	
		tmp_rec=Theom(degree=tmp, time=time, rec_date_index=reg_date)
		tmp_rec.save()
		return render(request,'rec_date.html',None)
		





 
def show_oneday_tmp(request):
	"""
	show one day temputerature statistics
	"""

	req_date=request.session['date']
	if req_date == None:
		error(request,'test')

	date_object = datetime.datetime.strptime(req_date,"%Y-%m-%d")

	start_time  = int(time.mktime(date_object.timetuple())*1000)
	extra_serie = {}

	
	xdata= []
	ydata= []
	thermolist=Theom.objects.filter(rec_date_index=req_date).order_by('time')

	index=0
	for each in thermolist:
		#minute=int(time.mktime(time.strptime(each,'%H:%M').timetuple())*1000)
		#minute=minute*50000
		xdata.append(index)
		logger.info(index)
 		ydata.append(each.degree)
		index+=1

	xdata_map = map(lambda x: start_time+x*50000, xdata)
	ydata_map = map(lambda y: y, ydata)

	linename=req_date
		
	chartdata = {
	    'x': xdata_map,
	    'name1': linename, 'y1': ydata_map, 'extra1': extra_serie,
	}

	charttype = "lineChart"
	chartcontainer = 'linechart_container' # container name
	data = {
	    'charttype': charttype,
	    'chartdata': chartdata,
	    'chartcontainer': chartcontainer,
	    'extra': {
		'x_is_date': True,
		'x_axis_format': '%H:%M',
		'tag_script_js': True,
		'jquery_on_ready': False,
	    }
	}
	
	return render_to_response('linechart.html', data)



