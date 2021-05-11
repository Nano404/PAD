FROM debian:stable
RUN apt-get update
RUN apt-get -y install apache2
EXPOSE 80 
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]