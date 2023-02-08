#!/bin/bash
#代码发布更新
LOCAL_DIR='./'
REMOTE_DIR='/opt/swiper'

USER='root'
HOST='127.0.0.1' # 域名

#上传代码
rsync -crnpP --exclude={.git, .venv, logs, __pycache__} $LOCAL_DIR $USER@HOST:$REMOTE_DIR/

#远程重启
ssh $USER@HOST '$REMOTE_DIR/script/restart.sh'
