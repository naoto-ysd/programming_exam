FROM ubuntu:precise

ENV DEBIAN_FRONTEND noninteractive

RUN mkdir -p /usr/src/app
ENV APP_ROOT /usr/src/app
ENV TZ 'Asia/Tokyo'
WORKDIR $APP_ROOT

# refer : https://qiita.com/ytyng/items/76784390a538bbb5117e
RUN sed -i -e 's/archive.ubuntu.com\|security.ubuntu.com/old-releases.ubuntu.com/g' /etc/apt/sources.list

RUN apt-get update && apt-get install -y build-essential ruby rubygems libpq-dev zlib1g-dev libxml2-dev libxslt1-dev
RUN gem install bundler -v 1.0.22
ADD . $APP_ROOT
RUN bundle install --binstubs

#Omit 'bundle exec'
ENV PATH $APP_ROOT/bin:$PATH

