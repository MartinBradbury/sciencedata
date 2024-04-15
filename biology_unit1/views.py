from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def test(request):
    return render(
        request, 'biology_u1/biology_u1.html',
    )