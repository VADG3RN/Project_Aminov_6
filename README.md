# Project_Aminov_6
1. Клонировать проект
git clone https://github.com/ваш-username/LR6-Django-API.git

cd LR6-Django-API/myproject

2. Создать и заполнить .env
copy .env.example .env

3. Запустить контейнеры
docker compose up --build

4. Применить миграции
docker compose exec web python manage.py migrate

5. Создать суперпользователя
docker compose exec web python manage.py createsuperuser

6. Готово!
API-документация: http://localhost:8000/swagger/

Админка: http://localhost:8000/admin/

Получение токена: POST → http://localhost:8000/api/token/

Использование Swagger
Открой http://localhost:8000/swagger/

Нажми Authorize

Вставь: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.xxxxxxxxxx

(токен из поля access при POST /api/token/)

Теперь все запросы авторизованы!

Полезные команды
Остановить всё (данные сохранятся)

docker compose down

Перезапустить

docker compose restart

Посмотреть логи

docker compose logs -f web

Эндпоинты API
/api/users/ — пользователи

/api/profiles/ — профили

/api/matches/ — совпадения

/api/messages/ — сообщения

/api/token/ — получение JWT

/api/token/refresh/ — обновление токена
