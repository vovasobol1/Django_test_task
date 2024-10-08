from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import cv2
import numpy as np
import os

from videoapp.models import VideoRequest

def homePage(request):
    return render(request, 'videoapp/home.html')


def generate_video(request):
    if request.method == 'POST':
        message = request.POST.get('message')

        if message:
            # Сохраняем запрос в базе данных
            video_request = VideoRequest(message=message)
            video_request.save()

            width, height = 100, 100
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            video_filename = message + '_ouput.mp4'
            out = cv2.VideoWriter(video_filename, fourcc, 24, (width, height))

            # Создаем кадр с черным фоном
            frame = np.zeros((height, width, 3), dtype=np.uint8)

            # Начальные координаты для бегущей строки
            x = width

            # Установим параметры шрифта
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 1
            font_thickness = 2
            font_color = (255, 255, 255)  # Белый цвет текста

            total_frames = 3 * 24
            # Получаем размер текста
            text_size = cv2.getTextSize(message, font, font_scale, font_thickness)[0]
            text_width = text_size[0]
            speed = (text_width + width) / total_frames

            # Создаем видео с бегущей строкой
            for _ in range(3*24):
                # Очистка кадра
                frame.fill(0)

                # Новые координаты для бегущей строки
                x -= speed  # Скорость бегущей строки

                # Если текст выходит за пределы экрана, начинаем с правого края
                if x < -text_width:
                    x = width

                # Добавляем текст
                cv2.putText(frame, message, (int(x), height // 2 + text_size[1] // 2), font, font_scale, font_color,
                            font_thickness)

                # Записываем кадр
                out.write(frame)

            # Закрываем видеопоток
            out.release()

            # Возвращаем сгенерированное видео для скачивания
            with open(video_filename, 'rb') as video_file:
                response = HttpResponse(video_file.read(), content_type='video/mp4')
                response['Content-Disposition'] = f'attachment; filename="{video_filename}"'
                response['Content-Length'] = os.path.getsize(video_filename)

            # Удаляем файл после отправки
            os.remove(video_filename)


            return response


    return render(request, 'videoapp/generate_video.html')


def get_all_requests(request):
    if request.method == 'GET':
        requests = VideoRequest.objects.all()
        return render(request, 'videoapp/history.html', {'requests': requests})


