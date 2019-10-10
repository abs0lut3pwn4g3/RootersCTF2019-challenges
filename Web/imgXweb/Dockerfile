FROM python:3

WORKDIR /usr/src/app

COPY app ./
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080
RUN useradd env
RUN chown env:env /usr/src/app -R
# RUN chown env:env -R static
# RUN chmod 777 site.db
# RUN chmod 777 static -R
# RUN chown env:env site.db
CMD su env -c "gunicorn -w 4 -b 0.0.0.0:8080 app:app"
