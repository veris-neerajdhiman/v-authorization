FROM django

WORKDIR /v-authorization

ADD ./requirements/base.txt /v-authorization/requirements/base.txt


RUN apt-get update && apt-get install -y git
RUN pip install -r ./requirements/base.txt

ADD . /v-authorization
