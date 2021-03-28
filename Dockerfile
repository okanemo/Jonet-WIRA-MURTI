FROM python:3
ENV PYTHONUNBUFFERED=1
COPY ./wait-for-it.sh /wait-for-it.sh
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt
RUN mkdir /app
WORKDIR /app
COPY ./app /app