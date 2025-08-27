from django.shortcuts import render

# Create your views here.
def home(request):
  context={{
    'Restaurant_Name':'Vanilla_Bytes'
    'welcome_message':'We are delighted to serve you the finest Italian cuisine'
  }}
  info = Restaurant.objects.first()
  return render(request,'home.html',context,{restaurant:info})

