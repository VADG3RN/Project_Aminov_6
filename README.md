# Project_Aminov_6
RESTful API туристического агентства на Django REST Framework (JWT, PostgreSQL, Docker).
## Запуск в Docker Desktop

1. Клонируй: 
`git clone https://github.com/VADG3RN/Project_Aminov_6.git`
2. Перейди в папку:
`cd Project_Aminov_6`
3. Создай .env в корне.
`cp .env.example .env`
5. В терминале проекта запусти:
`docker-compose up --build`
Миграции базы данных применятся автоматически при первом запуске.
6. Создай superuser:
`docker-compose exec web python manage.py createsuperuser`
Открой Swagger-документацию: http://localhost:8000/api/swagger/
Админка: http://localhost:8000/admin/ (логин/пароль от superuser)
Останови:
`docker-compose down`.

## Получение JWT-токена

В Swagger открой POST /api/register/ → создай пользователя.
Выполните POST-запрос на /api/token/.
Тело запроса:
{ 
"username": "ваш_логин", 
"password": "ваш_пароль" 
}
В ответе будет поле access — это ваш JWT-токен.
Откройте http://localhost:8000/api/swagger/
В правом верхнем углу нажмите зелёную кнопку Authorize
В поле вставьте: Bearer ваш_токен_из_поля_access (обязательно слово Bearer + пробел + токен)
Нажмите Authorize → Close
Теперь все запросы в Swagger отправляются с авторизацией.

## Полезные команды

Остановить контейнеры (данные в PostgreSQL сохранятся): docker-compose down
Перезапустить контейнеры: 
`docker-compose restart`
Посмотреть логи сервера: 
`docker-compose logs -f web`

Основные эндпоинты API
- /api/countries/ — страны (чтение без авторизации, создание/изменение/удаление — с JWT)
- /api/tours/ — туры (чтение без авторизации, создание/изменение/удаление — с JWT)
- /api/bookings/ — бронирования (только авторизованные пользователи, видны только свои)
- /api/register/ — регистрация нового пользователя
- /api/token/ — получение JWT-токена
- /api/token/refresh/ — обновление токена

GitHub: https://github.com/VADG3RN/Project_Aminov_6
