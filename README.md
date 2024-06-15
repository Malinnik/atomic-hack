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
    image: atomic-front:latest
    ports:
      - 3000:3000

  back:
    image: atomic-back:latest
    ports:
      - 8080:8080
    
```
Запустите, используя Docker Compose
```bash
docker compose up
```

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
