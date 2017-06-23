FROM django

WORKDIR /v-auth


ADD ./requirements/base.txt /v-auth/requirements/base.txt


RUN apt-get update && apt-get install -y git
RUN pip install -r ./requirements/base.txt

ADD . /v-auth

EXPOSE 80

COPY ./config/docker/docker-entrypoint.sh /
ENTRYPOINT ["./config/docker/docker-entrypoint.sh"]