import ujson
from django.core.cache import cache
from ujson import JSONDecodeError

from tools import token, message

cookies = token.Token()

mess = message.Class_message()


class Check_method(object):
    def __init__(self, request, method):
        self.request = request
        self.method = method

    def __call__(self, func):
        def check_mehtod(*args, **kwargs):
            if self.request.method == self.method:
                return func(*args, **kwargs)
            else:
                return mess.warn_message("method error")

        return check_mehtod


class Check_Login(object):
    def __init__(self, request):
        self.request = request

    def __call__(self, func):
        def login_Check(*args, **kwargs):
            if "HTTP_AUTHORIZATION" in self.request.META:
                username = cookies.decode(token=self.request.META.get("HTTP_AUTHORIZATION"))["id"]
                if cache.get(username) is None:
                    return mess.warn_message("未登录")
            else:
                return mess.warn_message("token不存在")
            return func(*args, **kwargs)

        return login_Check


class Check_Data(object):
    def __init__(self, request, ndata: list):
        self.request = request
        self.ndata = ndata

    def __call__(self, func):
        def login_Check(*args, **kwargs):
            try:
                data = ujson.loads(self.request.body.decode())
                for i in self.ndata:
                    if i not in data and data[i] == '':
                        return mess.warn_message("参数出错")
            except JSONDecodeError:
                return mess.warn_message("Json格式出错")
            return func(*args, **kwargs)

        return login_Check


class Key_Refresh:
    def __init__(self, request):
        self.request = request

    def __call__(self, func):
        def main(*args, **kwargs):
            username = cookies.decode(token=self.request.META.get("HTTP_AUTHORIZATION"))["id"]
            cache.touch(username, 1800)
            return func(*args, **kwargs)

        return main
