import json

from asgiref.sync import async_to_sync

from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer


class Chat_Consumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_{}'.format(self.room_name)

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data = None, bytes_data = None):
        receive_data = json.loads(text_data)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type'      : 'chat_message',
                'talk_uq_id': receive_data.get('talk_uq_id'),
                'message'   : receive_data.get('message'),
            }
        )

    async def chat_message(self, event):
        message = event.get('message')
        talk_uq_id = event.get('talk_uq_id')

        await self.send(text_data = json.dumps({
            'talk_uq_id': talk_uq_id,
            'message'   : message
        }))

# class Chat_Consumer(WebsocketConsumer):
#
#     def connect(self):
#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#         self.room_group_name = 'chat_{}'.format(self.room_name)
#
#         async_to_sync(self.channel_layer.group_add)(
#             self.room_group_name,
#             self.channel_name
#         )
#
#         self.accept()
#
#     def disconnect(self, close_code):
#         async_to_sync(self.channel_layer.group_discard)(
#             self.room_group_name,
#             self.channel_name
#         )
#
#     def receive(self, text_data = None, bytes_data = None):
#         text_data = json.loads(text_data)
#         message = text_data.get('message')
#
#         async_to_sync(self.channel_layer.group_send)(
#             self.room_group_name,
#             {
#                 'type'   : 'chat_message',
#                 'message': message
#             }
#         )
#
#     def chat_message(self, event):
#         message = event['message']
#
#         self.send(json.dumps({
#             'message': message
#         }))
