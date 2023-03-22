import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CommunityDraw.settings")

import django
django.setup()

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from rest_framework.authtoken.models import Token


@database_sync_to_async
def get_user(token):
    try:
        user = Token.objects.get(key=token).user
        return user
    except:
        return None


class PixelConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('pixels', self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("pixels", self.channel_name)

    async def receive(self, text_data):
        json_data = json.loads(text_data)
        if 'token' in json_data:
            self.scope['user'] = await get_user(json_data['token'])

    async def send_message(self, event):
        if self.scope['user'] != None:
            await self.send(text_data=json.dumps(event["text"]))
