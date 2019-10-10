FROM python:3

WORKDIR /usr/src/app

COPY app ./
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080
RUN useradd env
#RUN python manager.py db init && python manager.py db migrate && python manager.py db upgrade
CMD su env -c "gunicorn -w 4 -b 0.0.0.0:8080 application:app"
