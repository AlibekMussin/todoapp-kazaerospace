# todoapp-kazaerospace
Тестовое задание для КазАэро Space

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
 
 **Регистрация нового пользователя:**<br />
 username и email уникальны, password и password2 должны совпадать, так как это подтверждение введеного пароля<br />
 POST /api/v1/user/register/<br />
body_example:
```json
 { 
    "username":"user_1",
    "password":"Pass123!",
    "password2":"Pass123!",
    "email":"user1@gmail.com",
    "last_name":"Иванов",
    "first_name":"Иван"
 }
```
 ** Авторизация **<br />
 POST /api/v1/user/login/<br />
 body_example:
 ```json
 {
    "username":"user_1",
    "password":"Pass123!"
}
```
В результате выполнения запроса вы получите **access_token**<br />
Его надо будет скопировать и отправлять в других запросах к данным, ниже пример
<br /><br /><br />
 **Добавление новой задачи**<br /><br />
 POST /api/v1/cardlist/card/
 Authorization: Bearer - значение access_token 
 ```json
 {
    "subject": "Task 1 Subject",
    "description": "Task 1 Description",
    "status": "DOING",
    "executors": [
        {
            "executor": 4,
            "notifications": [
                {"notif_datetime": "2022-07-30"},
                {"notif_datetime": "2022-08-01"} 
            ]
        }
    ]
}
```
поле status можно не отправлять, тогда оно по умолчанию будет LATER<br /><br />
 Возможные значения - DOING, LATER, DONE