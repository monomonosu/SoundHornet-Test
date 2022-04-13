FROM tiangolo/uwsgi-nginx-flask:python3.8
COPY /app /app

RUN pip install SQLAlchemy
RUN pip install Flask-SQLAlchemy
RUN pip install flask-marshmallow 
RUN pip install marshmallow-sqlalchemy
RUN pip install Flask-Migrate

# RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
# RUN npm install
# RUN npm run build
