#!/bin/bash

# Ative o ambiente virtual
source /home/deploy/env-hospital/bin/activate

# Inicie o Gunicorn
gunicorn --config /home/deploy/hospital-panel/src/conf/gunicorn_config.py --chdir /home/deploy/hospital-panel/src/ painel_hegv.wsgi:application --workers=2 --threads=2 --worker-class=gthread

