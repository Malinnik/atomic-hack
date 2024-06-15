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
VIOLET = (75, 0, 130)
YELLOW = (255,255, 0)

label_to_color = {
    0: BLUE,
    1: RED,
    2: GREEN,
    3: VIOLET,
    4: YELLOW,
}

class_to_text = {
    0: "adj",
    1: "int",
    2: "geo",
    3: "pro",
    4: "non"
}

async def bbox(img: MatLike, cls, box, conf, use_label, show_conf):
    annotator = Annotator(img)

    conf = f"{int(conf*100)}%"

    b = box.xyxy[0]
    c = box.cls

    if not use_label and not show_conf:
        annotator.box_label(b, '', label_to_color[int(cls)])    
    else:
        annotator.box_label(b, 
            f'{class_to_text[int(cls)] if use_label else ""} {conf if show_conf else ""}',
            label_to_color[int(cls)])

    img = annotator.result()

    return img
        



async def predict_image(img: MatLike, model: YOLO = YOLO('best.pt'), conf: float = 0.02, use_label: bool = False, show_conf: bool = False):
    result = model.predict(img, conf=conf)

    classes = result[0].boxes.data[:, -1]

    confs = result[0].boxes.data[:, -2]

    for i in range(len(classes)):
        img = await bbox(img, classes[i], box=result[0].boxes[i], conf=confs[i], use_label=use_label, show_conf=show_conf)

    return img
