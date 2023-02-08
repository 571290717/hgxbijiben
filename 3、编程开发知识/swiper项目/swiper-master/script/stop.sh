#!/bin/bash
#停止
PROJECT='/opt/swiper'

#关掉gunicorn
cat $PROJECT/logs/gunicorn.pid | xargs kill
