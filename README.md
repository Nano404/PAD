# Project Agile Development(PAD)

Deze repo wordt gebruikt voor een school project genaamd Agile Development a.k.a PAD in het kort

## Starten

1. Haal de bestanden op via `git clone https://gitlab.com/ic1010c5/PAD.git`
2. Gebruik `cd` om in de map te komen van het opgehaalde bestand
3. Run de container door `docker-compuse up` te gebruiken 

## Docker containers gebruikt

- mariadb:laatste
- ninoanthonie/pad:laatste
- phpmyadmin:laatste

## Challenges

In de volgende tabs worden de challenges uitgelegd

### Challenge 1: Insecure Login Form

Deze challenge bevat het volgende:

Je moet proberen de inlog gegevens van een user te vinden. Wanneer deze gevonden zijn kan je bij het login form de gegevens in vullen. Na een succesvolle inlog poging komt er een pop-up dat laat zien dat je succesvol ingelogd bent.

### Challenge 2: URL Manipulation

Sites laten soms bij een installatie bestanden achter zonder te verwijderen. 
Hier kan je soms waardevolle informatie uithalen...

### Challenge 3: Cookie Manipulation

Een website kan cookies gebruiken of je een admin bent of niet.

## Documentatie

Programs: Apache2, python3, mariadb-server, modcgi, docker, docker-compose
Problems: 
- Python code wilde niet exec dit kwam omdat hij een CRLF(win-files) was dit moest naar LF(unix)
- httpd prebuilt container kreeg cgi niet aan de praat uiteindelijk zelf een docker container gebouwd zie Dockerfile
- De cookies en python deze kregen we alleen werkend met 2 simpele javascripts
- CGITB liet geen errors zien hij moet blijkbaar echt helemaal boven in het document staan
Directorys: 
- /var/www/html/
- /usr/lib/cgi-bin/
- /etc/apache2/sites-enabled/000-default.conf

### Docker

### Database Structuur

Database naam: pad

- **form_requests**
   _idform_requests_ int(11),
   _form_comment_ mediumtext,
   _form_email_ varchar(45),
   _form_name_ varchar(45)
- **ip**
    _id_ int(11),
    _ip_ int(11)
- **login**
    _id_ int(11),
    _username_ varchar(45),
    _password_ varchar(45),
    _user_id_ int(11)
- **rollen**
    _id_ int(11),
    _rol_naam_ varchar(45)
- **user**
    _id_ int(11),
    _rol_ varchar(45),
    _email_ varchar(45)

## Python Scripts

### Ip Ban

- /cgi/ipban.py

Bij de exec van dit bestand wordt het Ip gebanned van een specifieke user

### Restart Apache

- /cgi/reload.py

Bij het runnen van dit script wordt de Apache gerestart.

### Log

- /cgi/log.py

laat de error logs zien van de website

### form_request

- /cgi/form_request.py

Als deze wordt uitgevoert na het verzenden van je comment/email alles toevoegen aan de database en daarna het bericht terug lezen
