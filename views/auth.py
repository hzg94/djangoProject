import ujson
from django.core.cache import cache

from Sky_Django.admin import User_manager
from tools import message, token
from tools.Check import Check_Data, Check_method

mess = message.Class_message()

cookies = token.Token()


def login_api(request):
    @Check_method(request=request, method="POST")
    @Check_Data(request, ndata=['account', "password"])
    def main(request):
        data = ujson.loads(request.body.decode())
        account = User_manager.objects.filter(
            User_account=data["account"], User_Password=data["password"])
        if account.count() == 1:
            account = account.values()[0]
            string = cookies.encode(account=account['User_account'], id=account['User_id'])
            cache.set(account['User_id'], string, timeout=180000)
            return mess.get_message("登录成功", 200, {"token": string})
        else:
            return mess.get_message("账号不存在", 102, {})
    return main(request)

def resign_api(request):
    @Check_method(request=request, method="POST")
    @Check_Data(request=request, ndata=['account', "password", "zone", "mail", "username"])
    def main(request):
        data = ujson.loads(request.body.decode())
        if User_manager.objects.filter(
                User_account=data["account"], User_Password=data["password"]
        ).count() == 0:
            User_manager(
                User_name=data['username'],
                User_account=data['account'],
                User_Permission=0,
                User_mail=data['mail'],
                User_Zone=data['zone'],
                User_Password=data["password"]
            ).save()
            return mess.get_message("注册成功", 200, {})
    return main(request)
