from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def test(request):
    line = ''
    for k, v in request.GET.items():
        line += "<p><strong>%s</strong>=<strong>%s</strong></p>" % (k, v)
    return HttpResponse(line)
