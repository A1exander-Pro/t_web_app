FROM python:3

RUN mkdir /code

COPY requirements.txt /code

RUN pip install -r /code/requirements.txt

COPY . /code

ENV PRODUCTION TRUE

WORKDIR /code

ENTRYPOINT ["/code/entrypoint.sh"]





