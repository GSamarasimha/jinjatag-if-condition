from multiprocessing import Condition
from django.shortcuts import render

# Create your views here.
def ifcondition(request):
    dict={'a':90}
    return render(request,'condition.html',dict)