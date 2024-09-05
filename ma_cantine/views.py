from django.shortcuts import render

# Create your views here.

def ma_cantine(request):
    return render(request, 'index.html')