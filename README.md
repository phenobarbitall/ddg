Реализовать основу для небольшого сервиса - блога с регистрацией и парой API эндпоинтов:
 
1. /total-users - выдает, сколько всего зарегистрировано
2. /user-list - выдает список зарегистрированных юзернеймов
3. /user-profile/{id} - выдает информацию из профиля определенного пользователя
4. /user-profiles - выдает список профилей всех пользователей
 
Фреймворк: Django (версия не имеет значения)
Фронт не обязателен, оцениваться будет сам код
Разрешены любые подключаемые плагины и модули



Запуск проекта

git clone https://github.com/phenobarbitall/ddg.git

cd ddg/

source venv/bin/activate

python manage.py runserver
