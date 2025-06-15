Открыть терминал в папке rbauto
Активировать окружение .\Scripts\activate
Перейти в папку с проектом rbauto
Указать данные для подключения к постгресу в rbauto/settings.py
Запустить миграции python manage.py migrate
Создать суперадмина python manage.py createsuperuser
Запустить локальный сервер python manage.py runserver
+ добавить данные в админке /admin

(В случае чего, установить зависимости)
pip install django
pip install psycopg