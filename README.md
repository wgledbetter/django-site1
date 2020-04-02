# django-site1
Learning django by building a personal website

Personal Notes:

    python3 manage.py runserver 0.0.0.0:8080  # on AWS Cloud9
    docker run -it -p 8080:8080 wgledbetter/django-site1 bash

    docker-compose build
    docker-compose up -d
    docker-compose exec web bash

    mysqldump -uroot -p djangosite1 > /home/djangosite1_dump.sql
    mysql -uroot -p djangosite1 < /home/djangosite1_dump.sql
    
    sqlite3 storage.sqlite .dump > output_before.sql
