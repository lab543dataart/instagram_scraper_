FROM python:3.9.0

WORKDIR /home/

RUN echo "testing"

RUN git clone https://github.com/jeongmin-bak/instagram_scraper_.git

WORKDIR /home/instagram_scraper_/

RUN pip install --upgrade pip

RUN echo "testing"

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

RUN echo "SECRET_KEY=django-insecure-6@&7*^y97x@@3k4-vf-+)5g^!q=z0lt*m9q)#nents+marm+x)" > .env

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["bash", "-c", "python manage.py migrate --settings=scraper.settings.deploy && gunicorn scraper.wsgi --env DJANGO_SETTINGS_MODULE=scraper.settings.deploy --bind 0.0.0.0:8000"]
