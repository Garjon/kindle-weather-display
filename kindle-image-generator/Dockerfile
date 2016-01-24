FROM ubuntu:14.04

RUN apt-get update -qq && apt-get -y install python pngcrush
RUN apt-get -y install librsvg2-bin

COPY scripts /scripts
RUN chmod +x /scripts/weather-script.sh

WORKDIR /scripts
CMD ["./weather-script.sh"] 