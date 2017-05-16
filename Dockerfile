FROM django
ADD . /v-authorization

WORKDIR /v-authorization

#RUN apt-get update && apt-get install -y git
RUN pip install -r ./requirements/base.txt
