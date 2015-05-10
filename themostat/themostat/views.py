from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse


def index(request):
	return HttpResponseRedirect(reverse('themocheck:dates'))
	
