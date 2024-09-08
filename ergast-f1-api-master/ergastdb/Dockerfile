FROM mysql:latest

RUN echo "Downloading database dump"
RUN curl https://ergast.com/downloads/f1db.sql.gz -o f1db.sql.gz

RUN echo "Extracting database dump"
RUN gzip -dc f1db.sql.gz > f1db.sql

ENV MYSQL_ROOT_PASSWORD=ergastdb
ENV MYSQL_DATABASE=f1db