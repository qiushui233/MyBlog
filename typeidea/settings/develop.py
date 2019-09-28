from .base import *
import pymysql
DEBUG = True

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# pymysql.install_as_MySQLdb()
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',   # 数据库引擎
#         'NAME': 'typeidea',         # 你要存储数据的库名，事先要创建之
#         'USER': 'root',         # 数据库用户名
#         'PASSWORD': '1234',     # 密码
#         'HOST': 'localhost',    # 主机
#         'PORT': '3306',         # 数据库使用的端口
#     }
# }