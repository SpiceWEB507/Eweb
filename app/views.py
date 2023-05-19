from django.shortcuts import render
from django.views import View
# Create your views here.
from .models import Contact
from django.contrib import messages

def home_view(request):
    return render(request, 'app/index.html')

def about_view(request):
    return render(request, 'app/about.html')

def contact_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()
        messages.success(request,"Data Inserted Successfully")
    return render(request, 'app/contact.html')

def product_view(request):
    return render(request, 'app/product.html')


def computer_view(request):
    return render(request, 'app/computer.html')

def cpu_view(request):
    return render(request, 'app/cpu.html')

def monitor_view(request):
    return render(request, 'app/monitor.html')

def ups_view(request):
    return render(request, 'app/ups.html')

def networkswitch_view(request):
    return render(request, 'app/networkswitch.html')

class LaptopView(View):
    def get(self, request):
        return render(request, 'app/laptop.html')
   

        