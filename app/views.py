from django.shortcuts import render

# Create your views here.
def loop(request):
    d={'name':'sai shankar'}
    return render(request,'loop.html',d)

def ifloop(request):
    d={'d':''}
    return render(request,'ifloop.html',d)