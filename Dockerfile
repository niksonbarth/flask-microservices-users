FROM python:3.6.3

# install environment dependencies ***PROD***
#RUN apt-get update -yqq \
#  && apt-get install -yqq --no-install-recommends \
#    netcat \
#  && apt-get -q clean

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# add requirements (to leverage Docker cache)
ADD ./requirements.txt /usr/src/app/requirements.txt

# install requirements
RUN pip install -r requirements.txt

# add app
ADD . /usr/src/app

# run server
CMD python manage.py runserver -h 0.0.0.0
