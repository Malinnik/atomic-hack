:blush: #Определение дефектов сварных швов с помощью ИИ# :blush:

---
**Инструкции по развертыванию:**
- [README Frontend](https://github.com/Malinnik/atomic-hack/blob/main/frontend/README.md)
- [README Backend](https://github.com/Malinnik/atomic-hack/blob/main/backend/README.md)
- [README ML](https://github.com/Malinnik/atomic-hack/blob/main/ml/README.md)

### Быстрый запуск
Создайте `docker-compose.yaml`
```yaml
services:
  front:
    image: horaziy/atomic-hack-frontend:latest
    ports:
      - 3000:3000
    networks:
    - atomic
    restart: unless-stopped

  back:
    image: horaziy/atomic-hack-backend:latest
    ports:
      - 8080:8080
    networks:
      - atomic
    restart: unless-stopped

  nginx:
    image: nginx:latest
    environment:
      - PUID=1000
      - PGID=1000
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
    ports:
      - 80:80
      - 443:443
    restart: unless-stopped
    networks:
      - atomic

networks:
  atomic:
```

Рядом с этим файлом создайте nginx.conf
```conf
events {}
http {
    client_max_body_size 20m;

    server {
        listen 80;
        listen [::]:80;

        server_name localhost;

        location / {
            proxy_pass http://front:3000;
            proxy_set_header Host $Host;
            proxy_cache_bypass $http_upgrade;
        }
        location /api {
            proxy_pass http://back:8080/api;
        }
    }
}
```
Затем запустите, используя Docker Compose
```bash
docker compose up -d
```

Приложение разверентся за прокси и будет доступно на `http://locahost`. Если вы желаете изменить домен, замените `server_name` в `nginx.conf`.

---
**Постановка задачи:** требуется распознавать и определять виды дефектов сварочных швов.

Пример распознавания сварочного шва:
![Пример распознавания сварочного шва](https://github.com/Malinnik/atomic-hack/blob/main/docs/1%20(4).jpg)

Типы распознаваемых дефектов сварных швов:
- СИНИЙ - прилегающие дефекты
- КРАСНЫЙ - дефекты целостности
- ЗЕЛЕНЫЙ - дефекты геометрии
- ФИОЛЕТОВЫЙ - дефекты постобработки
- ЖЕЛТЫЙ - дефекты невыполнения

Для детекции использовалась модель [YOLOv8](https://github.com/ultralytics/ultralytics)

---

**Участники**
- Максим
- Адиль
- Софья
- Маша
