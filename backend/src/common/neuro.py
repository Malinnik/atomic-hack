from enum import Enum
import logging
import cv2

from cv2.typing import MatLike


BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PINK = (255, 20, 147)
VIOLET = (75, 0, 130)
WHITE =  (255, 255, 255)

async def process_image(img: MatLike, file_path: str):
    # img = cv2.imread('1 (1).jpg')
    #print(img)
    dh, dw, _ = img.shape

    file = open(file_path, 'r')
    logging.debug(f"{file=}")
    data = file.readlines()
    logging.debug(f"{data=}")
    file.close()

    for dt in data:

        # Split string to float
        type_defect, x, y, w, h = map(float, dt.split(' '))

        l = int((x - w / 2) * dw)
        r = int((x + w / 2) * dw)
        t = int((y - h / 2) * dh)
        b = int((y + h / 2) * dh)
        
        if l < 0:
            l = 0
        if r > dw - 1:
            r = dw - 1
        if t < 0:
            t = 0
        if b > dh - 1:
            b = dh - 1

        match type_defect:
            case 0: 
                cv2.rectangle(img, (l, t), (r, b), BLUE, 10)
            case 1:
                cv2.rectangle(img, (l, t), (r, b), RED, 10)
            case 2:
                cv2.rectangle(img, (l, t), (r, b), GREEN, 10)
            case 3:
                cv2.rectangle(img, (l, t), (r, b), GREEN, 10)
            case 4:
                cv2.rectangle(img, (l, t), (r, b), WHITE, 10)
    
    return img