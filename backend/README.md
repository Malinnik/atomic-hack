# Backend

## Описание
Сервис для обработки сварочных швов. Принимает фотографию сварочного шва и возвращает размеченное фото. Для создания данного сервиса используются библиотеки aiohttp, ultralytics, opencv-python, pyjwt, pydantic, poetry.

Важно, для запуска приложения требуются веса нейронной сети. Скачайте их с [Гугл Диска](https://drive.google.com/drive/folders/1tO5DBqqsoYEGXi1onDy0QUNKL2OuQNsd). Положите в ту папку, из которой будете запускать проект и назовите best.pt

## Запуск приложения
Для контроля зависимостей в проекте используется poetry. 

### Установка Poetry

Linux, macOS, Windows (WSL)
```bash
curl -sSL https://install.python-poetry.org | python3 -
```
Windows (Powershell)
```bash
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

### Установка зависимостей
Для установки основных зависимостей воспользуйтесь командой
```bash
poetry install --only main
```

### Запуск
Для запуска выполните команду
```bash
poetry run py .\src\main.py 
```

!!Очень важно. Для запуска приложения требуются веса нейронной сети. Их требуется положить туда, откуда запускается приложение, а также назвать `best.pt`


## Запуск в Docker
Для запуска приложения можно использовать Docker

### Запуск через команду
```bash
docker run horaziy/atomic-hack-backend -p 8080:8080
```
### Для запуска через Docker Compose
```bash
docker compose up
```


## Сборка проекта
Скачайте проект
```bash
git clone https://github.com/Malinnik/atomic-hack.git
cd atomic-hack/backend
```
Соберите проект используя Docker
```bash
docker build -t atomic-hack-backend
```
Запустите проект
```bash
docker run atomic-hack-backend -p 8080:8080
```
