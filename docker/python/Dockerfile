FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /hammer

COPY requirements.txt ./requirements_kvartirka.txt

RUN pip install -r requirements_kvartirka.txt

COPY . .

EXPOSE 8000

RUN python3 src/manage.py collectstatic --noinput

CMD python3 src/manage.py migrate && gunicorn kvartika.wsgi --chdir src --bind 0.0.0.0 --preload --log-file -
