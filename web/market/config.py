import os
project_dir = os.path.dirname(os.path.abspath(__file__))

DEV_DB = 'sqlite:///' + os.path.join(project_dir,'web', 'market', 'instance', 'market.db')

pg_user = 'admin'
pg_pass = 'admin'
pg_db = 'market'
pg_host = 'db'
pg_port = 5432

PROD_DB = f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}'