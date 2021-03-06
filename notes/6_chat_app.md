# Chat app

### static/chat/room.html

web socket url 중 '/ws/' 가 있는데 이는 HTTP 요청과 web socket 의 요청을 구분하기 위한 좋은 방법.
HTTP 요청은 uWSGI, WebSocket 요청은 ASGI 로 처리.
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Chat room</title>

    {% load static %}
    <link rel="icon" href="{% static 'comm/ozoz.ico' %}">

    <script src={% static 'comm/jquery_3.4.1.js' %}></script>

    <script>
        var CHAT_SOCKET;

        function fn_chat_on_message()
        {
            CHAT_SOCKET.onmessage = function (e) {
                var data = JSON.parse(e.data);

                var obj_chat_log = $(".chat-log");
                obj_chat_log.val(obj_chat_log.val() + '\n' + data['message'])
            };
        }

        function fn_chat_on_close()
        {
            CHAT_SOCKET.onclose = function (e) {
                console.error('CHAT_SOCKET is closed with error : ' + e)
            };
        }


        function fn_enter_chat_message()
        {
            $(".text-message").keypress(function (e) {
                if (e.keyCode === 13) {
                    CHAT_SOCKET.send(JSON.stringify({
                        'message': this.value,
                    }));

                    this.value = ''
                }
            });
        }

        $(document).ready(function () {
            CHAT_SOCKET = new WebSocket('ws://' + location.host + '/ws/chat/' + {{ room_name_json }})

            fn_chat_on_message();
            fn_chat_on_close();
            fn_enter_chat_message();
        });
    </script>
</head>
<body>

<label>
    <textarea class="chat-log" cols="100" rows="20"></textarea>
</label><br>

<label>
    <input class="text-message" size="100">
</label>

</body>
</html>
```

### chat/views.py
```
import json

from django.shortcuts import render
from django.utils.safestring import mark_safe

def index(request):
    return render(request, template_name = 'chat/index.html')

def room(request, room_name):
    return render(request, template_name = 'chat/room.html', context = {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
```

### chat/urls.py
```
from django.urls import path

from chat import views

urlpatterns = [
    path('', views.index),
    path('<str:room_name>', views.room),
]
```