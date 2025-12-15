# README для Project_Aminov_6

## Инструкция по запуску проекта

1. **Клонировать проект**
git clone https://github.com/VADG3RN/Project_Aminov_6.git
cd Project_Aminov_6
. **Создать и заполнить .env**
cp .env.example .env
По умолчанию значения в `.env` подходят для локального запуска. При необходимости отредактируйте файл.

3. **Запустить контейнеры**
docker-compose up --build
Миграции базы данных применятся автоматически при первом запуске.

4. **Создать суперпользователя** (для доступа в админку)
docker-compose exec web python manage.py createsuperuser
Введите username (например, `admin`), email (можно пропустить) и пароль.

5. **Готово!**
- API-документация (Swagger): **http://localhost:8000/api/swagger/**
- Админка Django: **http://localhost:8000/admin/** (логин/пароль от суперпользователя)

### Получение JWT-токена
POST → **http://localhost:8000/api/token/**  

Тело запроса:
{
"username": "ваш_логин",
"password": "ваш_пароль"
}
В ответе получите поле access — это ваш JWT-токен.

Использование Swagger
Откройте http://localhost:8000/api/swagger/
Нажмите зелёную кнопку Authorize в правом верхнем углу
В поле вставьте:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.xxxxxxxxxx(слово Bearer + пробел + токен из поля access)
Нажмите Authorize → Close

Теперь все запросы в Swagger будут авторизованными!
Полезные команды

Остановить всё (данные в PostgreSQL сохранятся):docker-compose down
Перезапустить контейнеры:docker-compose restart
Посмотреть логи сервера:docker-compose logs -f web

Эндпоинты API

/api/countries/ — страны (чтение без авторизации, запись/изменение/удаление — с JWT)
/api/tours/ — туры (чтение без авторизации, запись/изменение/удаление — с JWT)
/api/bookings/ — бронирования (только для авторизованных пользователей, видны только свои)
/api/register/ — регистрация нового пользователя
/api/token/ — получение JWT-токена
/api/token/refresh/ — обновление токена
