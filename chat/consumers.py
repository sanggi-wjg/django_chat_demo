import json

from channels.generic.websocket import WebsocketConsumer


class Chat_Consumer(WebsocketConsumer):

    def connect(self):
        self.accept()

    def disconnect(self, code):
        pass

    def receive(self, text_data = None, bytes_data = None):
        text_data = json.loads(text_data)
        message = text_data.get('message')

        self.send(json.dumps({
            'message': message
        }))
