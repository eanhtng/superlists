Provisioning a new site
=======================

## Required packages:
* nginx
* Python 3.6
* virtualenv + pip
* Git

eg, on Ubuntu:
	
	sudo add-apt-repository pa:deadsnakes/ppa
	sudo apt update
	sudo apt install nginx git python36 python3.6-venv

## Nginx Virtual Host config

* see nginx.template.conf
* replace $DOMAIN with, e.g., superlists-staging.edu.solutions.com

## Systemd service

* see gunicorn-systemd.template.service
* replace $DOMAIN with, e.g., superlists-staging.edu.solutions.com

##  Folder structure

Assume we have a user account at /home/$USER

/home/username
|
------sites
	|------$DOMAIN1
	|	|------.env
	|	|------db.sqlite3
	|	|------mange.py etc
	|	|------static
	|	|------virtualenv
	|
	|------$DOMAIN2
		|------.env
		|------db.sqlite3
		|------etc
