from nvd3 import pieChart
from django.shortcuts import render,render_to_response

# Open File to write the D3 Graph


def show_piechart(request):
	"""
    	pieChart page
    	"""
    	xdata = ["Apple", "Apricot", "Avocado", "Banana", "Boysenberries", "Blueberries", "Dates", "Grapefruit", "Kiwi", "Lemon"]
   	ydata = [52, 48, 160, 94, 75, 71, 490, 82, 46, 17]

    	color_list = ['#5d8aa8', '#e32636', '#efdecd', '#ffbf00', '#ff033e', '#a4c639',
                  '#b2beb5', '#8db600', '#7fffd4', '#ff007f', '#ff55a3', '#5f9ea0']
    	extra_serie = {
        	"tooltip": {"y_start": "", "y_end": " cal"},
        	"color_list": color_list
    	}
    	chartdata = {'x': xdata, 'y1': ydata, 'extra1': extra_serie}
    	charttype = "pieChart"
    	chartcontainer = 'piechart_container'  # container name

    	data = {
        	'charttype': charttype,
        	'chartdata': chartdata,
        	'chartcontainer': chartcontainer,
        	'extra': {
            		'x_is_date': False,
            		'x_axis_format': '',
            		'tag_script_js': True,
            		'jquery_on_ready': False,
        	}
    	}
    	return render(request, 'piechart.html', data)


