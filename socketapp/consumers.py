import json

from time import sleep
from datetime import datetime

from channels.generic.websocket import WebsocketConsumer


class ws_consumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        while True:
            now = datetime.now()
            self.send(json.dumps({'timeValue': now.strftime("%H:%M:%S")}))
            sleep(1)
