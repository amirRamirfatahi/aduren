pipenv install

postgres: 
```bash
postgres=# create database aduren;
CREATE DATABASE
postgres=# create role aduren;
CREATE ROLE
postgres=# alter database aduren owner to aduren ;
ALTER DATABASE
postgres=# grant ALL on DATABASE aduren to aduren ;
GRANT
postgres=# alter role aduren with login ;
ALTER ROLE
postgres=# alter role aduren with encrypted password 'bFg7VFV8';
```

django
```bash
python manage.py migrate
python manage.py createsuperuser

```


