# Setup Chat app
```
$ pip install -U channels

Installing collected packages: txaio, six, pycparser, cffi, cryptography, autobahn, zope.interface, constantly, incremental, attrs, Automat, idna, hyperlink, PyHamcrest, pyopenssl, pyasn1, pyasn1-modules, service-identity, twisted, daphne, channels
Successfully installed Automat-20.2.0 PyHamcrest-2.0.2 attrs-19.3.0 autobahn-20.6.2 cffi-1.14.0 channels-2.4.0 constantly-15.1.0 cryptography-2.9.2 daphne-2.5.0 hyperlink-19.0.0 idna-2.10 incremental-17.5.0 pyasn1-0.4.8 pyasn1-modules-0.2.8 pycparser-2.20 pyopenssl-19.1.0 service-identity-18.1.0 six-1.15.0 twisted-20.3.0 txaio-20.4.1 zope.interface-5.1.0
```

### chat_demo/routing.py
```
from channels.routing import ProtocolTypeRouter

application = ProtocolTypeRouter({
    # Django views is added by default
})
```

### chat_demo/settings.py
충돌방지를 위해 channels 를 위로 
```
INSTALLED_APPS = [
    'channels', 
    'chat',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Channels
ASGI_APPLICATION = 'chat_demo.routing.application'
```

### Start django
ASGI/Channels 로 개발서버가 시작됨
```
$ python manage.py runserver 0:8000

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
July 14, 2020 - 02:41:00
Django version 3.0.8, using settings 'chat_demo.settings'

** Starting ASGI/Channels version 2.4.0 development server at http://0:8000/ **

Quit the server with CONTROL-C.
```


### static/chat/index.html
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Chat index</title>

    {% load static %}
    <link rel="icon" href="{% static 'comm/ozoz.ico' %}">

    <script src={% static 'comm/jquery_3.4.1.js' %}></script>

    <script>
        function fn_enter_room()
        {
            $(".text-room-name").keypress(function (e) {
                if (e.keyCode === 13) {
                    console.log(this.value)
                    location.pathname = '/chat/' + this.value;
                }
            })
        }

        $(document).ready(function () {
            fn_enter_room();
        });
    </script>

</head>
<body>

<label>
    <input type="text" class="text-room-name" value="">
</label>

</body>
</html>
```

### chat/views.py
```
from django.shortcuts import render


def index(request):
    return render(request, template_name = 'chat/index.html')
```