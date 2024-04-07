from django.utils.deprecation import MiddlewareMixin

from tools.message import Class_message


class auth_midden(MiddlewareMixin):
    def __init__(self, get_response):
        super().__init__(get_response)
        self.url_list = ["set_password", "set_name", "set_zone"]
    def process_request(self, request):
        message = Class_message()
        url = request.path.split("/")[2]
        if url in self.url_list:
            if "HTTP_AUTHORIZATION" in request.META:
                return message.get_message("登录失效", 104, {})
