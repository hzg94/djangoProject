import jwt
import random
import time
from django.conf import settings


class Token:
    def __init__(self):
        self.timestamp = int(time.time())
        self.secert = settings.TOKEN_SECRET
    def encode(self, account, id):
        return jwt.encode({
            "account": account,
            "id": str(id),
            "random": random.sample("abcdefghijklmnopqrstuvwxyz!@#$%^&*()", 12)
        }, self.secert, algorithm=settings.TOKEN_SECRET_MODE)
    def decode(self, token):
        decode_res = jwt.decode(token, self.secert, algorithms=settings.TOKEN_SECRET_MODE)
        return decode_res
