# todoapp-kazaerospace
тестовое задание для КазАэро Space

При первом запуске:
 - создать БД в Postgres
 - создать в корне приложения файл .env по образцу файла .env_example 
 - открыть проект в pyCharm ибо другой IDE
 - cd путь_до_проекта/todoapp-kazaerospace
 - python -m venv venv
 - если на Windows:
    - venv\Scripts\activate
 - если на Linux:
    - source env/bin/activate
 - когда окружение удачно активировалось устанавливаем зависимости: pip install - r requirements.txt
 - python manage.py migrate
 - python manage.py createsuperuser --username todo_admin --email anyemail@email.com
 - python manage.py autofill_groups
 - запускаем проект
 
 **Регистрация нового пользователя:**
 POST /api/v1/user/register/
body_example:
 { 
    "username":"user_1",
    "password":"Pass123!",
    "password2":"Pass123!",
    "email":"user1@gmail.com",
    "last_name":"Иванов",
    "first_name":"Иван",
 }