from django.shortcuts import render
from django.http import HttpResponse
import os

def generate_video(request):
    if request.method == 'POST':
        message = request.POST.get('message')

        if message:
            return HttpResponse("Сообщение введено")



    return render(request, 'videoapp/generate_video.html')