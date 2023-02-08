#!/bin/bash
#重启
PROJECT='/opt/swiper'

cat $PROJECT/logs/gunicorn.pid | xargs kill -HUP
