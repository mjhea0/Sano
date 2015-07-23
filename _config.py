import os
2
3  # grab the folder where this script lives
4 basedir = os.path.abspath(os.path.dirname(__file__))
5
6 DATABASE = 'database.db'
7 USERNAME = 'admin'
8 PASSWORD = 'admin'
9 WTF_CSRF_ENABLED = True
10 SECRET_KEY = 'my_precious'
11
12  # define the full path for the database
13 DATABASE_PATH = os.path.join(basedir, DATABASE)
