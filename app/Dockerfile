FROM python:3.8.2

LABEL Author="Andrii Porokhnavets"
LABEL E-mail="andrij843@gmail.com"
LABEL version="0.0.1"

ENV FLASK_APP "app.py"
ENV FLASK_ENV "development"
ENV FLASK_RUN_HOST 0.0.0.0

ADD . .

RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --dev --system --deploy --ignore-pipfile

EXPOSE 5000

CMD python init_db.py ; flask run