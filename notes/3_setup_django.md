### Start Django
Create Django proejct. 
```
$ django admin startproject chat_demo
```

That will create a directory **chat_demo**.
```
chat_demo - manage.py
          - chat_demo    - __init__.py
                         - asgi.py
                         - settings.py
                         - urls.py
                         - wsgi.py
```

### Modify database config on settings.py
chat_demo/chat_demo/settings.py
> Before
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
> After
```
DATABASES = {
    'default': {
        'ENGINE'  : 'django.db.backends.mysql',
        'NAME'    : 'backend',
        'USER'    : 'root',
        'HOST'    : '127.0.0.1',
        'PASSWORD': 'wpdlwl',
        'PORT'    : '33061',
    }
}
```

### DB migrate
```
$ python manage.py makemigrations
$ python manage.py migrate
```

```
$ docker exec -it maria bash
```

```
# mysql -u root -p
MariaDB [(none)]> use backend;
MariaDB [backend]> show tables;

+----------------------------+
| Tables_in_backend          |
+----------------------------+
| auth_group                 |
| auth_group_permissions     |
| auth_permission            |
| auth_user                  |
| auth_user_groups           |
| auth_user_user_permissions |
| django_admin_log           |
| django_content_type        |
| django_migrations          |
| django_session             |
+----------------------------+
10 rows in set (0.000 sec)

# exit
```

#### Open server port
```
$ firewall-cmd --permanent --zone=public --add-port=8000/tcp
$ firewall-cmd --reload
```

## Static
#### chat_demo/chat_demo/settings.py
``` 
TEMPLATES = [
    {
        'BACKEND' : 'django.template.backends.django.DjangoTemplates',
        'DIRS'    : [
            os.path.join(BASE_DIR, "static"),
        ],
        'APP_DIRS': True,
        'OPTIONS' : {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
```
then
``` 
$ python manage.py collectstatic
```

#### chat_demo/chat_demo/urls.py
```
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('chat', include('chat.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
```


## Start Django!
```
$ python manage.py runserver 0:8000
```
