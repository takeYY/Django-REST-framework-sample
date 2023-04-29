FROM nginx:stable-alpine

ARG ROOTDIR="/usr/share/nginx/html/static"
ARG IODIR="./"
ARG TZ="Asia/Tokyo"

RUN mkdir -p ${ROOTDIR}
COPY ${IODIR} ${ROOTDIR}/
COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ./nginx_default.conf /etc/nginx/conf.d/default.conf
COPY ./nginx_status.conf /etc/nginx/conf.d/status.conf

ENV TZ=${TZ}
