from argparse import ArgumentParser
import glob
import os
from tqdm import tqdm
import pandas as pd
import numpy as np

from ultralytics import YOLO

parser = ArgumentParser()
parser.add_argument('--input_path', type=str, required=True, help='Путь к папке с картинками')
parser.add_argument('--model_path', type=str, required=True, help='Путь к модели на диске')
parser.add_argument('--output_path', type=str, required=False, default='submission.csv', help='Путь к csv на выход')
args = parser.parse_args()

model = YOLO(args.model_path)

def process_directory(model, directory, submission, conf):
    lst = []
    for file in tqdm(glob.glob(os.path.join(directory, "*.jpg"))):
        prediction = model.predict(file, conf=conf, verbose=False)

        classes = prediction[0].boxes.data[:, -1]
        tensors = prediction[0].boxes.xywhn
        for cls, xywh in zip(classes, tensors):
            lst.append([os.path.basename(file), int(cls)] + [float(a) for a in xywh])
    pd.DataFrame(lst, columns=['filename', 'class_id', 'rel_x', 'rel_y', 'width', 'height']).to_csv(submission, index=False, sep=';')
    print(f'Saved to {submission}')

process_directory(model, args.input_path, args.output_path, conf=0.25)
