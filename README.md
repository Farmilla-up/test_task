# Task Manager API

Запуск тестов через pytest -v 

Простое Django + Django REST Framework приложение для управления задачами (CRUD) с помощью только одной view 

## 📌 Функционал
- Создание задач (Create)
- Получение одной задачи (Read)
- Список всех задач (List)
- Обновление задачи (Update)
- Удаление задачи (Delete)

Установка и запуск: 
docker-compose up --build 

Все действия проходят по одному url 

Получить список задач: curl http://127.0.0.1:8000/tasks/


Получить задачу по айди: curl http://127.0.0.1:8000/tasks/<uuid>/


Создать задачу: curl -X POST http://127.0.0.1:8000/api/v1/tasks/ \
  -H "Content-Type: application/json" \
  -d '{
        "title": "Тестовая задача",
        "description": "Описание для теста",
        "status": "created"
      }'


Обновить задачу: curl -X PUT http://127.0.0.1:8000/api/v1/tasks/<uuid>/ \
  -H "Content-Type: application/json" \
  -d '{
        "title": "Обновлённая задача",
        "description": "Новое описание",
        "status": "in_progress"
      }'


Удалить задачу: curl -X DELETE http://127.0.0.1:8000/api/v1/tasks/<uuid>/


