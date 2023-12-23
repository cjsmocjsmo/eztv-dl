FROM debian:bullseye-slim

RUN \
	apt-get update && \
	apt-get dist-upgrade -y && \
	apt-get autoclean -y && \
	apt-get autoremove -y && \
	apt-get install --no-install-recommends -y \
		build-essential \
		python3-dev \
        python3-setuptools \
        python3-wheel \
		python3-pip \
		python3-feedparser \
		python3-requests \
		python3-bs4 \
		cron

RUN mkdir /home/logs
COPY EZtv.py /home/
COPY eztvlib.py /home/
COPY rss.py /home/ 
COPY TGtv.py /home/
COPY mycrontab /etc/cron.d/mycrontab

RUN chmod 0644 /etc/cron.d/mycrontab &&\
    crontab /etc/cron.d/mycrontab


ENTRYPOINT ["cron", "-f"] 
