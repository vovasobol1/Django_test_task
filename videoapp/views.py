from django.shortcuts import render
from django.http import HttpResponse
import cv2
import numpy as np
import os

def generate_video(request):
    if request.method == 'POST':
        message = request.POST.get('message')

        if message:


        else:
            return HttpResponse("Пожалуйста, введите сообщение.")