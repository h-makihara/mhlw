#FROM alpine:latest
FROM mysql:5.7

ARG MYSQL_ROOT_PASSWORD

RUN chown -R mysql /var/lib/mysql
RUN mkdir -p /var/lib/mysql-files
RUN mkdir -p /etc/mysql/conf.d
COPY ./my.cnf /etc/mysql/my.cnf
COPY ./mysql.cnf /etc/mysql/conf.d/mysql.cnf
