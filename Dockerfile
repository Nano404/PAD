#Deze Dockerfile staat de website op voor onze pad project dit is heel wat makkelijker dan de httpd/apache container te configureren 
#Note to self: De CGI/WSGI/FLASK Moet nog worden enabled
FROM debian:buster-slim
RUN apt-get update
RUN apt-get -y install apache2 python3 python3-pip nano
COPY 000-default.conf /etc/apache2/sites-enabled/
RUN a2dismod mpm_event && a2enmod mpm_prefork cgi
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
EXPOSE 80