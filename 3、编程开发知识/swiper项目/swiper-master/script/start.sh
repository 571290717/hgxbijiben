#!/bin/bash
#启动
PROJECT='/opt/swiper'

cd $PROJECT
source $PROJECT .venv/bin/activate
gunicorn -c swiper/gunicorn_config.py swiper.wsgi
deactivate
cd ~
