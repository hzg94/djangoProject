import ujson

from Sky_Django.admin import User_manager
from Sky_Django.models import Zone_Data
from tools import message, token
from tools.Check import Check_Login, Check_Data

mess = message.Class_message()
cookies = token.Token()
def xg_password(request):
    @Check_Data(request=request, ndata=['password'])
    @Check_Login(request=request)
    def main(request):
        token_Data = cookies.decode(request.COOKIES['token'])
        data = ujson.loads(request.body.decode())
        User_manager.objects.filter(User_account=token_Data['account']).update(User_Password=data['password'])
        return mess.get_message("修改成功", 200, {})
    return main(request)
def set_name(request):
    @Check_Data(request=request, ndata=['username'])
    @Check_Login(request=request)
    def main(request):
        token_Data = cookies.decode(request.COOKIES['token'])
        data = ujson.loads(request.body.decode())
        User_manager.objects.filter(User_account=token_Data['account']).update(User_name=data['username'])
        return mess.get_message("修改成功", 200, {})
    return main(request)
def set_zone(request):
    @Check_Data(request=request, ndata=['zone'])
    @Check_Login(request=request)
    def main(request):
        token_Data = cookies.decode(request.COOKIES['token'])
        data = ujson.loads(request.body.decode())
        list1 = Zone_Data.objects.filter(New_city_id=data['zone']).values()
        if len(list1) == 1:
            User_manager.objects.filter(User_account=token_Data['account']).update(User_Zone=data['zone'])
            return mess.get_message("修改成功", 200, {})
        else:
            return mess.warn_message("地区不存在")
    return main(request)
