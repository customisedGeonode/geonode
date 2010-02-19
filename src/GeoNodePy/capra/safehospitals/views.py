# Create your views here.
from django.shortcuts import render_to_response 
from django.template import RequestContext
from django.conf import settings

try:
    import json
except ImportError:
    print "using simplejson instead of json"
    import simplejson as json



def index(request):
    return render_to_response('safehospitals/index.html', RequestContext(request, {
        'config': 'config',
        'bg': json.dumps(settings.MAP_BASELAYERS)
    }))