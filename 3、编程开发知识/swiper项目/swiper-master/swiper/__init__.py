import pymysql

from lib.db import patch_model

pymysql.install_as_MySQLdb()

# 首先加载__init__文件
patch_model()
