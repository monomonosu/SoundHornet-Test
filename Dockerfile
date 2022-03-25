FROM tiangolo/uwsgi-nginx-flask:python3.8
COPY /app /app

RUN RUN pip install SQLAlchemy
RUN pip install Flask-SQLAlchemy
RUN pip install flask-marshmallow 
RUN pip install marshmallow-sqlalchemy
RUN pip install Flask-Migrate 
