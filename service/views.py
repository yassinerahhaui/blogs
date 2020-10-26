from django.shortcuts import render
from .models import Service
# Create your views here.
def all_service(request):
    all_service = Service.objects.all()
    context = {
        'services':all_service,
    }
    return render(request,'all_service.html',context)

def service(request,id):
    service = Service.objects.get(id=id)
    context = {
        'service':service,
    }
    return render(request,'service.html',context)