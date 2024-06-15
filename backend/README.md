# Backend

## Описание
Сервис для обработки сварочных швов. Принимает фотографию сварочного шва и возвращает размеченное фото. Для создания данного сервиса используются библиотеки aiohttp, ultralytics, opencv-python, pyjwt, pydantic.

## Как начать
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
