# kvartirka.com тестовое задание

тг: @dane4kq email: zanzydnd@gmail.com

## Запуск приложения docker-compose

Надо создать файл .env.docker в src - пример лежит там же

``
docker-compose up --build -d
``

## Запуск приложения python src/manage.py runserver

1. Ставим виртуальное окружение `python3 -m venv env`
2. Входим в виртуальное окружение `source env/bin/activate`
3. Устанавливаем пакеты `pip install -r requirements.txt`
4. Если необходимо поднимаем базу через compose (Не забываем прописать .env файл в src)
5. Прогоняем миграции `python src/manage.py migrate`
6. Поднимаем приложение `python src/manage.py runserver`

## 127.0.0.1:8000

документация - /api/v1/swagger/ \
апи - /api/v1/