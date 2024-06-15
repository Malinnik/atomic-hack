from enum import Enum
import logging
import cv2

from cv2.typing import MatLike
import numpy as np
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PINK = (255, 20, 147)
VIOLET = (75, 0, 130)
YELLOW = (255,255, 0)
WHITE =  (255, 255, 255)

label_to_color = {
    0: BLUE,
    1: RED,
    2: GREEN,
    3: VIOLET,
    4: YELLOW,
}



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
                cv2.rectangle(img, (l, t), (r, b), VIOLET, 10)
            case 4:
                cv2.rectangle(img, (l, t), (r, b), WHITE, 10)
    
    return img

async def process(img: MatLike, cls, tensor):
    dh, dw, _ = img.shape
    
    print(f"""
        {dh=}
        {dw=}
""")

    x = tensor[0]
    y = tensor[1]
    w  = tensor[2]
    h = tensor[3]

    l = int((x - w / 2) * dw)
    r = int((x + w / 2) * dw)
    t = int((y - h / 2) * dh)
    b = int((y + h / 2) * dh)


    print(f"""
        {x=}
        {y=}
        {w=}
        {h=}
""")

    if l < 0:
            l = 0
    if r > dw - 1:
        r = dw - 1
    if t < 0:
        t = 0
    if b > dh - 1:
        b = dh - 1

    print(f"""
        {l=}
        {r=}
        {t=}
        {b=}
""")

    match cls:
        case 0: 
            cv2.rectangle(img, (l, t), (r, b), BLUE, 10)
        case 1:
            cv2.rectangle(img, (l, t), (r, b), RED, 10)
        case 2:
            cv2.rectangle(img, (l, t), (r, b), GREEN, 10)
        case 3:
            cv2.rectangle(img, (l, t), (r, b), VIOLET, 10)
        case 4:
            cv2.rectangle(img, (l, t), (r, b), WHITE, 10)
    
    cv2.putText(img, f"{cls} {0.2}", (l,t+1), cv2.FONT_HERSHEY_SIMPLEX,  2, VIOLET, 4)

    return img


async def bbox(img: MatLike, cls, box, use_label: bool = True):
    annotator = Annotator(img)

    b = box.xyxy[0]
    c = box.cls

    if use_label:
        annotator.box_label(b, f'{cls}', label_to_color[int(cls)])
    else:
        annotator.box_label(b, "", label_to_color[int(cls)])

    img = annotator.result()

    return img
        



async def predict_image(img: MatLike, model: YOLO = YOLO('best.pt'), conf: float = 0.02):
    result = model.predict(img, conf=0.02)

    classes = np.argmax(result[0].boxes.data, axis=1)
    tensors = result[0].boxes.xywhn

    # # confs = np.max(result[0].boxes.data)
    # print(f"{confs=}")

    # logging.debug(f"{classes=}")
    # logging.debug(f"{tensors=}")


    # for i in range(len(classes)):
        # img = await process(img, classes[i], tensors[i])

    for i in range(len(classes)):
        img = await bbox(img, classes[i], box=result[0].boxes[i], use_label=False)

    return img
