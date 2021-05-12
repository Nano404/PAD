#Deze Dockerfile staat de website op voor onze pad project dit is heel wat makkelijker dan de httpd/apache container te configureren 
#Note to self: De CGI/WSGI/FLASK Moet nog worden enabled
FROM debian:buster-slim
RUN apt-get update
RUN apt-get -y install apache2
WORKDIR /var/www/html
ADD Website .
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
EXPOSE 80