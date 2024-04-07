import time
import ujson
from django.core.cache import cache

from Sky_Django.admin import User_manager
from Sky_Django.models import Zone_Data, Knn_data, today_Data, noral_Data
from tools import message, token
from tools.Check import Check_Login, Check_method, Key_Refresh

mess = message.Class_message()
cookies = token.Token()


def normalModel(request):
    @Check_method(request=request, method="GET")
    @Check_Login(request=request)
    def main(request):
        token_data = request.META.get("HTTP_AUTHORIZATION")
        id = cookies.decode(token_data)['id']
        cache_Data = cache.get(id + "n")
        if cache_Data is None:
            now_Date = time.strftime("%m-%d", time.localtime())
            user_zone = User_manager.objects.filter(User_id=id).values()[0]["User_Zone"]
            back_data = noral_Data.objects.filter(New_city_id=user_zone).values()
            if len(back_data) > 0:
                redis_cache = ujson.dumps(back_data[0])
                cache.set(id + "n", redis_cache, timeout=18000)
                return mess.get_message("获取成功", 200, back_data[0])
            else:
                return mess.get_message("暂无数据", 200, {})
        else:
            return mess.get_message("获取成功", 200, ujson.loads(cache_Data))

    return main(request)


def KnnModel(request):
    @Check_method(request=request, method="GET")
    @Check_Login(request=request)
    def main(request):
        token_data = request.META.get("HTTP_AUTHORIZATION")
        id = cookies.decode(token_data)['id']
        cache_data = cache.get(id + "_ai")
        if cache_data is None:
            data = User_manager.objects.filter(User_id=id).values()[0]["User_Zone"]
            back_data = Knn_data.objects.filter(New_city_id=data).values()
            if len(back_data) > 0:
                cache.set(id + "_ai", ujson.dumps(back_data[0]), timeout=1800)
                return mess.get_message("ok", 200, back_data[0])
            else:
                return mess.warn_message("knn error")
        else:
            return mess.get_message("获取成功", 200, ujson.loads(cache_data))

    return main(request=request)


def zone_data(request):
    @Check_method(request=request, method="GET")
    def main(request):
        cache_data = cache.get("Zone_data")
        if cache_data is None:
            data = Zone_Data.objects.all().values_list()
            back_data = []
            for i in data:
                back_data.append({
                    "city_name": i[2],
                    "city_id": i[1]
                })
            cache.set("Zone_data", ujson.dumps(back_data))
            return mess.get_message("获取成功", 200, {"data": back_data})
        else:
            return mess.get_message("获取成功", 200, {"data": ujson.loads(cache_data)})

    return main(request)


def Get_User_Api(request):
    @Check_method(request=request, method="GET")
    @Check_Login(request)
    @Key_Refresh(request=request)
    def main(request):
        cookies_data = request.META.get("HTTP_AUTHORIZATION")
        id = cookies.decode(cookies_data).get("id")
        cache_data = cache.get(id + "_u")
        if cache_data is None:
            User_data = User_manager.objects.filter(User_id=id).values()[0]
            Zone_name = Zone_Data.objects.filter(New_city_id=User_data["User_Zone"]).values()[0]
            data = {
                "User_name": User_data["User_name"],
                "User_Zone": Zone_name["city_name"],
                "User_Permission": User_data["User_Permission"]
            }
            cache.set(id + "u", ujson.dumps(data), timeout=1800)
            return mess.get_message("获取成功", 200, data)
        else:
            return mess.get_message("获取成功", 200, ujson.loads(cache_data))

    return main(request)


def get_today_data(request):
    @Check_method(request=request, method="GET")
    @Check_Login(request=request)
    def main(request):
        token_data = request.META.get("HTTP_AUTHORIZATION")
        # now_Date = time.strftime("%Y-%m-%d", time.localtime())
        now_Date = '2022-09-14'
        id = cookies.decode(token_data)['id']
        cache_data = cache.get(id + "_w")
        if cache_data is None:
            data = User_manager.objects.filter(User_id=id).values()[0]["User_Zone"]
            data = today_Data.objects.filter(city_id=data, date=now_Date).values()
            if len(data) > 0:
                cache.set(id + "w", ujson.dumps(data[0]), timeout=1800)
                return mess.get_message("获取成功", 200, data[0])
            else:
                return mess.get_message("暂无数据", 500, {})
        else:
            return mess.get_message("获取成功", 200, ujson.loads(cache_data))

    return main(request)
