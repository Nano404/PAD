# Project Agile Development(PAD)

This repo is used for a school project Project Agile Pevelopment PAD for short

## Getting started

1. Pull down the repository `git clone https://gitlab.com/ic1010c5/PAD.git`
2. `cd` into the directory where `docker-compose.yml` is
3. to run the container `docker-compose up`

## Docker containers Used

- mariadb:latest
- ninoanthonie/pad:latest
- phpmyadmin:latest

## Challanges

In the following tabs we will explain what the challanges are about

### Challange 1: Insecure Login Form

This challange consists of the following:

You need to try login/find the credentials for a user. When the credenstials are found put them into the login form, you will get a pop-up that shows if you where successful or not.

### Challange 2: URL Manipulation

Sites laten soms bij een installatie bestanden achter zonder te verwijderen. 
Hier kan je soms waardevolle informatie uithalen

### Challange 3: Cookie Manipulation

A website can use cookies to check if your an admin or not 

## Documentatie

Programs: Apache2, python3, mariadb-server, modcgi, docker, docker-compose
Problems: 
- Python code wilde niet exec dit kwam omdat hij een CRLF(win-files) was dit moest naar LF(unix)
- httpd prebuilt container kreeg cgi niet aan de praat uiteindelijk zelf een docker container gebouwd zie Dockerfile
- De cookies en python deze kregen we alleen werkend met 2 simpele javascripts
Directorys: 
- /var/www/html/
- /usr/lib/cgi-bin/
- /etc/apache2/sites-enabled/000-default.conf

### Docker


### Ip Ban

- /py/ipban.py

Bij de exec van dit bestand wordt het Ip gebanned van een specifieke user
