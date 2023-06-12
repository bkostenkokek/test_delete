FROM python:3.9

ENV DJANGO_SETTINGS_MODULE=delete_django.settings.production

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "delete_django.wsgi", "--bind", "0.0.0.0:8000"]
