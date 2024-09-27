import cv2
import numpy as np

def create_video(text):
    width, height = 100, 100
    fps = 24
    duration = 3  # 3 секунды
    total_frames = duration * fps

    out = cv2.VideoWriter("output.mp4", cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))
    frame = np.zeros((height, width, 3), dtype=np.uint8)

    x = width
    y = height
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_thickness = 2
    font_color = (255, 255, 255)

    text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]

    for _ in range(total_frames):
        frame.fill(0)
        x -= 10  # Скорость бегущей строки

        if x + text_size[0] < 0:
            x = width

        cv2.putText(frame, text, (x, y), font, font_scale, font_color, font_thickness, lineType=cv2.LINE_AA)
        out.write(frame)

    out.release()


create_video("hello world")
