FROM python:3

RUN apt-get update

# We copy just the requirements.txt first to leverage Docker cache

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt && pip install python-dotenv

COPY . /app

EXPOSE 5000

RUN export FLASK_ENV=development

ENTRYPOINT [ "python" ]


CMD flask run --host 0.0.0.0
CMD [ "restapi.py" ]