from django.shortcuts import render
from django.http import HttpResponse
from joblib import load

model = load('./model/data.pickle')
# Create your views here.


def Home(request):

    return render(request,'index.html')

def result(request):
    rainfall=request.POST["rainfal"]
    return render(request,'result.html',{'rainfall':rainfall})