from django.shortcuts import render
from .models import restaurant

# Create your views here.
def home(request):
    return render(request,'home.html'{'name':restaurant.name})