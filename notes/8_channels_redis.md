# Channels redis

```
$ pip install channels_redis

Installing collected packages: async-timeout, hiredis, aioredis, msgpack, channels-redis
Successfully installed aioredis-1.3.1 async-timeout-3.0.1 channels-redis-3.0.0 hiredis-1.0.1 msgpack-1.0.0
```

#### chat_demo/settings.py
```
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG' : {
            'hosts': [('127.0.0.1', 63791)],
        },
    }
}
```

Test
```
$ python3 manage.py shell

>>> import channels.layers
>>> channel_layer = channels.layers.get_channel_layer()
>>> from asgiref.sync import async_to_sync
>>> async_to_sync(channel_layer.send)('test_channel', {'type': 'hello'})
>>> async_to_sync(channel_layer.receive)('test_channel')
{'type': 'hello'}
```

#### chat/consumers.py
```
import json

from asgiref.sync import async_to_sync

from channels.generic.websocket import WebsocketConsumer


class Chat_Consumer(WebsocketConsumer):

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_{}'.format(self.room_name)

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data = None, bytes_data = None):
        text_data = json.loads(text_data)
        message = text_data.get('message')

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type'   : 'chat_message',
                'message': message
            }
        )

    def chat_message(self, event):
        message = event['message']

        self.send(json.dumps({
            'message': message
        }))
```