# ML часть решения команды "Эльза и генг"

В нашем решении были дообучены нейронные сети YOLOv8x и YOLOv10x.

## Инференс

Сначала нужно скачать веса обученной модели из [гугл диска](https://drive.google.com/drive/folders/1tO5DBqqsoYEGXi1onDy0QUNKL2OuQNsd?usp=sharing).

```bash
python ml/inference.py --model_path=yolo8_100_best.pt --input_path=folder_with_images
```
где *folder_with_images* - папка с jpg картинками.

## Обучение

Код обучения представлен в ноутбуках *train_yolo8.ipynb* и *train_yolo10.ipynb*.
