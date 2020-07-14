# Django App 

#### create app folder
```
$ python manage.py startapp chat
```
That will create a directory **chat**.
```
chat  - mirgations 
      - admin.py
      - apps.py
      - models.py
      - tests.py
      - views.py
```

## Hello Django!
###  sample/settings.py
Add address.
```
ALLOWED_HOSTS = [
    '192.168.10.213',
]
```

Add apps created **chat**.
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'chat',
]
```

### chat/urls.py
Add route.
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('chat/', include('chat.urls'))
]
```

### chat/urls.py
Create a file **urls.py** in app directory.
```
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
]
```
index
```
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello Django')
```
